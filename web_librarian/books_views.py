from django.http import HttpResponse
from web_super_admin.models import *
from web_super_admin.forms import *
from django.shortcuts import render, redirect, get_object_or_404
from . models import *
from . forms import *


def Books_create(request):
    form = BookForm(request.post)
    if request.method == 'POST':
        form = BookForm(request.post)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = BookForm(request.post)
    context = {
        "form" : form
    }
    return render(request, "librarian/index.html")

def Books_Detail(request):
    books = Books.objects.all()
    context = {
        'books' : books
    }
    return render(request, "librarian/index.html", context)

def Book_Detail(request, pk):
    book = get_object_or_404(Books, pk=pk)
    context = {
        'book' : book
    }
    return render(request, "librarian/index.html", context)

def Book_Update(request, pk):
    book = get_object_or_404(Books, pk=pk)
    form = BookForm(request.POST)
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = BookForm(request.POST)
    context = {
        'form' : form
    }
    return render(request, 'librarian/index.html', context)


def Book_delete(request, pk):
    book = get_object_or_404(Books, pk)
    book.delete()

def Books_delete(request):
    books = Books.objects.all()
    books.delete()    
