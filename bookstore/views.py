import json, itertools, requests
from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from bookstore.models import Book, Comment

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
    book = Book.objects.filter(isbn=isbn)[0]
    if book:
        # Call Google Book api for book cover
        res = requests.get(f"https://www.googleapis.com/books/v1/volumes", params={"q": f"isbn:{book.isbn}"})
        imgsrc = res.json()['items'][0]['volumeInfo']['imageLinks']['thumbnail']

        # If there is a new comment
        if request.method == "POST":
            new_cmt = Comment(
                user=User.objects.get(username=request.POST['input-username']),
                book=Book.objects.get(isbn=isbn),
                content=request.POST['content']
            )
            new_cmt.save()
        
        # Get comments on this book
        cmts = Comment.objects.filter(book__isbn__contains=isbn)[::-1]
        # cmts = Comment.objects.first()
        print(cmts)
        context = {"book": book, "imgsrc": imgsrc, "cmts": cmts}
        return render(request, "bookstore/item.html", context)
    else:
        return render(request, "bookstore/notfound.html")

def login(request):
    return render(request, "bookstore/login.html")

def register(request):
    return render(request, "bookstore/register.html")

def profile(request):
    return render(request, "bookstore/profile.html")
