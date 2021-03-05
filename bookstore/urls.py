from django.urls import path
from . import views

app_name = "bookstore"
urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    path("register", views.register, name="register"),
    path("search", views.search, name="search"),
    path("profile", views.profile, name="profile"),
    path("item/<str:isbn>", views.item, name="item"),
]