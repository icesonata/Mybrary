import json
from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages

from bookstore.models import Book
from .forms import CreateUserForm

def index(request):
    return render(request, "bookstore/index.html")

def search(request):
    return render(request, "bookstore/search.html")

def item(request, isbn):
    return render(request, "bookstore/item.html")

def loginPage(request):
    #form = AuthenticationForm()
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, username + "was successfully login to account")
            return HttpResponseRedirect(reverse('bookstore:index'))
        else:
            return render (request, "bookstore/login.html")

    return render (request, "bookstore/login.html")

def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form =CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get("username")
            #messages.success(request, user + "was successfully create an account")
            return HttpResponseRedirect("login")
        else:
            messages.info(request, "Username or password is in correct")

    context = {"form":form}
    return render(request, "bookstore/register.html", context)

def profile(request):
    return render(request, "bookstore/profile.html")
