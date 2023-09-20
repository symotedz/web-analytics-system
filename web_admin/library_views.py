from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from web_super_admin.forms import *
from web_super_admin.models import *

# view for creating new library
def library_create(request):
    form = LibraryItemForm(request.POST)
    if request.method == 'POST':
        form = LibraryItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/web_admin/librarys_detail/')
    else:
        form = LibraryItemForm(request.POST)
    context = {
        'form' : form
    }
    return render(request, 'webadmin/library_create.html', context)

# view for reading all librarys
def librarys_detail(request):
    librarys = LibraryItem.objects.all()
    context = {
        'librarys' : librarys
    }
    return render(request, 'webadmin/librarys_detail.html', context)

# view for reading a single user

def library_detail(request, pk):
    library = get_object_or_404(LibraryItem, pk=pk)
    context = {
        'library' : library
    }
    return render(request, 'webadmin/library_detail.html', context)

# view for updating a single user
def library_update(request, pk):
    library = get_object_or_404(LibraryItem, pk=pk)
    form = LibraryItemForm(request.POST, instance = library)
    if request.method == 'POST':
        form = LibraryItemForm(request.POST, instance = library)
        if form.is_valid():
            form.save()
            return redirect('/web_admin/librarys_detail/')
    else:
        form = LibraryItemForm(request.POST, instance = library)
    context = {
        'form' : form,
        'library' : library
    }
    return render(request, 'webadmin/library_update.html', context)

#view for deleting a single user
def library_delete(request, pk):
    library = get_object_or_404(LibraryItem, pk=pk)
    library.delete()
    return redirect('/web_admin/librarys_detail/')

# view for deleting all users
def librarys_delete(request):
    library =LibraryItem.objects.all()
    library.delete()
    return redirect('/web_admin/library_detail/')

        
    