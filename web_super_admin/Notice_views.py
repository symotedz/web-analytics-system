from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from . models import *
from . forms import *

# view for creating new notice
def notice_create(request):
    form = NoticeForm(request.POST)
    if request.method == 'POST':
        form = NoticeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/super_admin/notices_detail/')
    else:
        form = NoticeForm(request.POST)
    context = {
        'form' : form
    }
    return render(request, 'Dashboard/notice_create.html', context)

# view for reading all notices
def notices_detail(request):
    notices = Notice.objects.all()
    context = {
        'notices' : notices
    }
    return render(request, 'Dashboard/notices_detail.html', context)

# view for reading a single user

def notice_detail(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    context = {
        'notice' : notice
    }
    return render(request, 'Dashboard/notice_detail.html', context)

# view for updating a single user
def notice_update(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    form = NoticeForm(request.POST, instance = notice)
    if request.method == 'POST':
        form = NoticeForm(request.POST, instance = notice)
        if form.is_valid():
            form.save()
            return redirect('/super_admin/notices_detail/')
    else:
        form = NoticeForm(request.POST, instance = notice)
    context = {
        'form' : form,
        'notice' : notice
    }
    return render(request, 'Dashboard/notice_update.html', context)

#view for deleting a single user
def notice_delete(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    notice.delete()
    return redirect('/super_admin/notices_detail/')

# view for deleting all users
def notices_delete(request):
    notices = Notice.objects.all()
    notices.delete()
    return redirect('/super_admin/notices_detail/')

        
    