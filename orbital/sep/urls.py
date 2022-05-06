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
    path("delete/<str:title>", views.delete_watchlist, name="delete_watchlist")
]
