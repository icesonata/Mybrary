import json
from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from bookstore.models import Book

def index(request):
    return render(request, "bookstore/index.html")

def search(request):
    return render(request, "bookstore/search.html")

def item(request, isbn):
    return render(request, "bookstore/item.html")

def login(request):
    return render(request, "bookstore/login.html")

def register(request):
    return render(request, "bookstore/register.html")

def profile(request):
    return render(request, "bookstore/profile.html")
