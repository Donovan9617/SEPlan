from datetime import date
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.core.paginator import Paginator
from django.core.files.storage import FileSystemStorage
import time

from .models import Forum, User, Chat, Review, Opening, Watchlist, PartnerUniversity, Shortlist

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    openings = Opening.objects.all().order_by("-date")
    numOfItemsPerPage = 2
    paginator = Paginator(openings, numOfItemsPerPage)
    lst = []
    watchlist = Watchlist.objects.filter(user=request.user)
    for item in watchlist:
        lst.append(item.opening.title)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    shortlist = Shortlist.objects.filter(user=request.user)
    lst2 = []
    for item in shortlist:
        if item.partneruniversity.puname not in lst2:
            lst2.append(item.partneruniversity.puname)
    time.sleep(0.5)
    return render(request, "sep/index.html", {
        "openings": page_obj, "watchlist": lst, "shortlist": shortlist, "lst2": lst2
    })

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        major = request.POST['major']
        year = request.POST['year']
        faculty = request.POST['faculty']
        email = request.POST['email']
        password = request.POST['password']
        confirmation = request.POST['confirmation']
        if password != confirmation:
            return render(request, "sep/register.html", {
                "message": "*Error: Please ensure password and confirmation password is the same!"
            })
        try:
            user = User.objects.create_user(username=username, major=major, year=year, faculty=faculty, email=email, password=password)
            user.save()
        except IntegrityError:
            return render(request, "sep/register.html", {
                "message": "*Error: This username has already been taken, please choose another username!"
            })
        login(request, user)
        time.sleep(1)
        return HttpResponseRedirect(reverse("index"))
    return render(request, "sep/register.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, "sep/login.html", {
                "message": "*Error: Invalid username and password or account does not exist!"
            })
    return render(request, "sep/login.html")


def messages(request, to):
    if request.method == "POST":
        fromAddress = request.user.username
        toAddress = to
        text = request.POST["text"]
        chat = Chat.objects.create(fromAddress=fromAddress, toAddress=toAddress, text=text)
        chat.save()
        return HttpResponseRedirect(reverse('messages', args=[to]))

    message = Chat.objects.filter(toAddress=request.user.username) | Chat.objects.filter(fromAddress=request.user.username)
    message = list(message.order_by('date'))
    lst = []
    for item in message:
        if item.toAddress != request.user.username:
            if item.toAddress not in lst:
                lst.append(item.toAddress)
        if item.fromAddress != request.user.username:
            if item.fromAddress not in lst:
                lst.append(item.fromAddress)
    pm = Chat.objects.filter(fromAddress=request.user.username, toAddress=to) | Chat.objects.filter(fromAddress=to, toAddress=request.user.username)
    pm = pm.order_by('date')
    to = User.objects.get(username=to)
    return render(request, "sep/messages.html", {
        "messages": lst, "pm": pm, "to": to
    })

def search(request):
    searchTerm = request.POST['student']
    users = User.objects.all()
    for user in users:
        if user.username == searchTerm:
            return HttpResponseRedirect(reverse('messages', args=[user.username]))
    return HttpResponseRedirect(reverse('messages', args=[request.user.username]))

def reviews(request):
    if request.method == "POST":
        uni = request.POST['university']
        review = request.POST['review']
        period = request.POST['period']
        modules = request.POST['modules']
        living = request.POST['living']
        prepare = request.POST['prepare']

        if request.FILES['attachments']:
            myfile = request.FILES['attachments']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            url = fs.url(filename)

        review = Review(user=request.user, university=uni, review=review,
        period=period, modules=modules,
        living=living, prepare=prepare, attachments=url)
        review.save()
        time.sleep(1.5)
        return HttpResponseRedirect(reverse('reviews'))
    history = Review.objects.filter(user=request.user).order_by('-date')
    reviews = list(Review.objects.all())
    lst = []
    for item in reviews:
        if item.university not in lst:
            lst.append(item.university)
    return render(request, "sep/reviews.html", {
        "reviews": lst, "history": history
    })

def page(request, university):
    reviews = Review.objects.filter(university=university).order_by('-date')
    numOfItemsPerPage = 1
    paginator = Paginator(reviews, numOfItemsPerPage)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'sep/page.html', {
        "reviews": page_obj, "university": university, "count": reviews.count
    })

def delete_review(request, id):
    r = Review.objects.filter(id=id).first()
    r.delete()
    time.sleep(1.5)
    return reviews(request)

def watchlist(request):
    watchlist = Watchlist.objects.filter(user=request.user).order_by('-id')
    return render(request, "sep/watchlist.html", {
        "watchlist": watchlist
    })

def save_watchlist(request, title):
    opening = Opening.objects.filter(title=title).first()
    w = Watchlist(user=request.user, opening=opening)
    w.save()
    return index(request)

def delete_watchlist(request, title):
    opening = Opening.objects.filter(title=title).first()
    w = Watchlist.objects.filter(user=request.user, opening=opening)
    w.delete()
    return watchlist(request)

def modules(request):
    if request.method == "POST":
        faculty = request.user.faculty
        module = request.POST['module']
        search = True
        mappable = PartnerUniversity.objects.filter(forfaculty=faculty, nusmodulecode=module)
        shortlist = Shortlist.objects.filter(user=request.user)
        added = []
        for item in shortlist:
            added.append(item.partneruniversity.nusmodulecode)
        time.sleep(1.5)
        return render(request, "sep/modules.html", {
            "mappable": mappable, "module": module, "search": search, "added": added
        })
    search = False
    return render(request, "sep/modules.html", {
        "search": search
    })

def planner(request, id):
    partneruniversity = PartnerUniversity.objects.filter(id=id).first()
    shortlist = Shortlist(user=request.user, partneruniversity=partneruniversity)
    shortlist.save()
    time.sleep(1)
    return HttpResponseRedirect(reverse('index'))

def delete_shortlist(request, mod):
    partneruniversity=PartnerUniversity.objects.get(nusmodulecode=mod)
    shortlist=Shortlist.objects.get(user=request.user, partneruniversity=partneruniversity)
    shortlist.delete()
    time.sleep(1)
    return HttpResponseRedirect(reverse('index'))

def forum(request):
    if request.method == "POST":
        title = request.POST['title']
        query = request.POST['query']

        if request.FILES['attachments']:
            myfile = request.FILES['attachments']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            url = fs.url(filename)

        new_post = Forum(user=request.user, query=query, attachments=url)
        new_post.save()
        time.sleep(1.5)
        return HttpResponseRedirect(reverse('forum'))
    history = Forum.objects.all().order_by('-date')
    queries = list(Forum.objects.all())
    lst = []
    for item in queries:
        if item not in lst:
            lst.append(item)
    return render(request, "sep/forum.html", {
        "queries": lst, "history": history
    })