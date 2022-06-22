from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register, name="register"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("messages/<str:to>", views.messages, name="messages"),
    path("search", views.search, name="search"),
    path("reviews", views.reviews, name="reviews"),
    path("page/<str:university>", views.page, name="page"),
    path("delete/<int:id>", views.delete_review, name="delete_review"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("save/<str:title>", views.save_watchlist, name="save_watchlist"),
    path("delete/<str:title>", views.delete_watchlist, name="delete_watchlist"),
    path("modules", views.modules, name="modules"),
    path("planner/<int:id>", views.planner, name="planner"),
    path("delete_shortlist/<str:mod>", views.delete_shortlist, name="delete_shortlist"),
    path("forum", views.forum, name="forum"),
    path("view_review/<int:id>", views.view_review, name="view_review"),
    path("new_discussion", views.new_discussion, name="new_discussion")
]
