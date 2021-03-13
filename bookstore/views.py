import json
from django.core import serializers
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from bookstore.models import Book
from .forms import CreateUserForm, UserUpdateForm, ProfileUpdateForm

def index(request):
    # if not request.user.is_authenticated:
    username = request.user.username
    context = {"username": username}
    return render(request, "bookstore/index.html", context)

def search(request):
    return render(request, "bookstore/search.html")

def item(request, isbn):
    return render(request, "bookstore/item.html")

def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form =CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get("username")
            # messages.success(request, f'Account created for {username}!')
            return redirect("/login")
        # else:
        #     messages.info(request, "Username or password is in correct")
    else:
        form = CreateUserForm()
    context = {"form":form}
    return render(request, "bookstore/register.html", context)

@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect("/profile")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, "bookstore/profile.html", context)
    

# def loginPage(request):
#     #form = AuthenticationForm()
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect(reverse('bookstore:index'))
#         else:
#             return render (request, "bookstore/login.html")

#     return render (request, "bookstore/login.html")

# def logoutPage(request):
#     return render(request, "bookstore/logout.html")