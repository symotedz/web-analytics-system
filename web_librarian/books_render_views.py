from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from . models import *
from . forms import *
from web_super_admin.models import *
from web_super_admin.forms import *

def book_render_create(request):
    form = BookRenderForm(request.POST)
    if request.method == 'POST':
        form = BookRenderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = BookRenderForm(request.POST)
    context = {
        'form' : form
    }
    return render(request, 'library/index.html', context)

def book_render_update(request, pk):
    book_render = get_object_or_404(request.POST, pk=pk)
    form = BookRenderForm(request.POST)
    if request.method == 'POST':
        form = BookRenderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = BookRenderForm(request.POST)
    context = {
        'form' : form,
    }
    return render(request, 'library/index.html', context)


def book_render_delete(request, pk):
    book_render = get_object_or_404(Books, pk=pk)
    book_render.delete()
    return redirect('/')

def books_render_delete(request):
    books_render = Books.objects.all()
    books_render.delete()
    return redirect('/')


def books_render_detail(request):
    books = Books.objects.all()
    context = {
        'books' : books
    }
    return render(request, 'librarian/index.html', context)

def book_render_detail(request, pk):
    book = get_object_or_404(Books, pk=pk)
    context = {
        'book' : book
    }
    return render(request, "librarian/index.html", context)

