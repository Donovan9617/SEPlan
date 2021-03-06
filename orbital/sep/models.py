from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields.related import ForeignKey

class User(AbstractUser):
    faculty = models.CharField(max_length=120)
    year = models.IntegerField(blank=True, null=True)
    major = models.CharField(max_length=120)
    sep = models.BooleanField(blank=True, null=True)
    picture = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.username

class Chat(models.Model):
    fromAddress = models.CharField(max_length=120)
    toAddress = models.CharField(max_length=120)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return f'From: {self.fromAddress} To: {self.toAddress} Text: {self.text} Date: {str(self.date)}'

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    university = models.CharField(max_length=120)
    date = models.DateTimeField(auto_now_add=True)
    review = models.TextField(blank=True, null=True)
    period = models.TextField(blank=True, null=True)
    modules = models.TextField(blank=True, null=True)
    living = models.TextField(blank=True, null=True)
    prepare = models.TextField(blank=True, null=True)
    attachments = models.URLField(blank=True, null=True)

    def __str__(self):
        return f'Reviewer: {self.user} University: {self.university} Date: {str(self.date)} Review: {self.review} Period: {self.period} Modules: {self.modules} Living: {self.living} Prepare: {self.prepare} Attachments: {self.attachments}'

# For site administrator
class Opening(models.Model):
    title = models.CharField(max_length=120)
    text = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}: {self.text}"

class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    opening = models.ForeignKey(Opening, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} placed {self.opening} on watchlist."

class PartnerUniversity(models.Model):
    forfaculty = models.CharField(max_length=120)
    puname = models.CharField(max_length=120)
    pumodule = models.CharField(max_length=120)
    pumodulecode = models.CharField(max_length=120)
    nusmodule = models.CharField(max_length=120)
    nusmodulecode = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.pumodulecode} in {self.puname} maps to {self.nusmodulecode} in NUS."

class Shortlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    partneruniversity = models.ForeignKey(PartnerUniversity, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} placed {self.partneruniversity} on watchlist."

class Forum(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    date = models.DateTimeField(auto_now_add=True)
    title = models.TextField(blank=True, null=True)
    query = models.TextField(blank=True, null=True)
    attachments = models.URLField(blank=True, null=True)

    def __str__(self):
        return f'User: {self.user} Date: {str(self.date)} Query: {self.query} Attachments: {self.attachments}'

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Forum, on_delete=models.CASCADE, related_name="comments")
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'User: {self.user} Date: {str(self.date)} Post: {self.post} Comment: {self.comment}'