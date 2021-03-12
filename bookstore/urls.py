from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

app_name = "bookstore"
urlpatterns = [
    path("", views.index, name="index"),
    path("login", auth_views.LoginView.as_view(template_name="bookstore/login.html"), name="login"),
    path("logout", auth_views.LogoutView.as_view(template_name="bookstore/logout.html"), name="logout"),
    path("register", views.register, name="register"),
    path("search", views.search, name="search"),
    path("profile", views.profile, name="profile"),
    path("item/<str:isbn>", views.item, name="item"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
