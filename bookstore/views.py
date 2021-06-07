import json, itertools, requests
from django.core import serializers
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from bookstore.models import Book, Comment
from .forms import CreateUserForm, UserUpdateForm, ProfileUpdateForm

def index(request):
    # if not request.user.is_authenticated:
    username = request.user.username
    context = {"username": username}
    return render(request, "bookstore/index.html", context)

def search(request):
    books = None
    if request.method == "POST":
        usr_input = "|".join(request.POST["search"].split())
        # Get results from three different fields by applying regex
        result_1 = Book.objects.filter(title__iregex=str(usr_input))
        result_2 = Book.objects.filter(author__iregex=str(usr_input))
        result_3 = Book.objects.filter(isbn__iregex=str(usr_input))
        
        # Combine and remove duplicate from three result lists
        books = list(set(itertools.chain(result_1, result_2, result_3)))
    else:
        books = Book.objects.all()[:50]
        
    return render(request, "bookstore/search.html", {
        "books": books
    })

def item(request, isbn):
    username = 'anonymous'      # Default username
    book = Book.objects.filter(isbn=isbn)[0]
    if book:
        # Call Google Book api for book cover
        res = requests.get("https://www.googleapis.com/books/v1/volumes", params={"q": "isbn:{}".format(book.isbn)})
        try:
            imgsrc = res.json()['items'][0]['volumeInfo']['imageLinks']['thumbnail']
        except Exception:
            imgsrc = None
            
        # Check and get user's username
        if request.user.is_authenticated:
            username = request.user.username

        # If there is a new comment
        if request.method == "POST":
            new_cmt = Comment(
                user=User.objects.get(username=username),
                book=Book.objects.get(isbn=isbn),
                content=request.POST['content']
            )
            new_cmt.save()
        
        # Get comments on this book
        cmts = Comment.objects.filter(book__isbn__contains=isbn)[::-1]

        context = {"book": book, "imgsrc": imgsrc, "cmts": cmts, "username": username}
        return render(request, "bookstore/item.html", context)
    else:
        return render(request, "bookstore/notfound.html")

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
    

# Login page
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
