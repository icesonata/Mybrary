import json, itertools
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
    books = None
    if request.method == "POST":
        usr_input = "|".join(request.POST["search"].split())
        # Get results from three different fields by applying regex
        result_1 = Book.objects.filter(title__iregex=rf"{usr_input}")
        result_2 = Book.objects.filter(author__iregex=rf"{usr_input}")
        result_3 = Book.objects.filter(isbn__iregex=rf"{usr_input}")
        
        # Combine and remove duplicate from three result lists
        books = list(set(itertools.chain(result_1, result_2, result_3)))
    else:
        books = Book.objects.all()[:50]
        
    return render(request, "bookstore/search.html", {
        "books": books
    })

def item(request, isbn):
    book = Book.objects.filter(isbn=isbn)
    if book:
        return render(request, "bookstore/item.html", {"book": book})
    else:
        return render(request, "bookstore/item.html", {"message": "Not Found"})

def login(request):
    return render(request, "bookstore/login.html")

def register(request):
    return render(request, "bookstore/register.html")

def profile(request):
    return render(request, "bookstore/profile.html")
