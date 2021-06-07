from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

app_name = "bookstore"
urlpatterns = [
	path('/', views.index, name="index_deploy"),
    	path("", views.index, name="index"),
    	path("login", auth_views.LoginView.as_view(template_name="bookstore/login.html"), name="login"),
 	path("/login", auth_views.LoginView.as_view(template_name="bookstore/login.html"), name="login_deploy"),
	path("logout", auth_views.LogoutView.as_view(template_name="bookstore/logout.html"), name="logout"),
    	path("/logout", auth_views.LogoutView.as_view(template_name="bookstore/logout.html"), name="logout_deploy"),
	path("register", views.register, name="register"),
	path("/register", views.register, name="register_deploy"),
	path("search", views.search, name="search"),
	path("/search", views.search, name="search_deploy"),
	path("profile", views.profile, name="profile"),
    	path("/profile", views.profile, name="profile_deploy"),
	path("item/<str:isbn>", views.item, name="item"),
	path("/item/<str:isbn>", views.item, name="item_deploy"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
