from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from . models import *
from web_super_admin.forms import *
from web_super_admin.models import *

# view for creating new subject
def subject_create(request):
    form = SubjectForm(request.POST)
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/web_admin/subjects_detail/')
    else:
        form = SubjectForm(request.POST)
    context = {
        'form' : form
    }
    return render(request, 'webadmin/subject_create.html', context)

# view for reading all subjects
def subjects_detail(request):
    subjects = Subject.objects.all()
    context = {
        'subjects' : subjects
    }
    return render(request, 'webadmin/subjects_detail.html', context)

# view for reading a single user

def subject_detail(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    context = {
        'subject' : subject
    }
    return render(request, 'webadmin/subject_detail.html', context)

# view for updating a single user
def subject_update(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    form = SubjectForm(request.POST, instance = subject)
    if request.method == 'POST':
        form = SubjectForm(request.POST, instance = subject)
        if form.is_valid():
            form.save()
            return redirect('/web_admin/subjects_detail/')
    else:
        form = SubjectForm(request.POST, instance = subject)
    context = {
        'form' : form,
        'subject' : subject
    }
    return render(request, 'webadmin/subject_update.html', context)

#view for deleting a single user
def subject_delete(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    subject.delete()
    return redirect('/web_admin/subjects_detail/')

# view for deleting all users
def subjects_delete(request):
    staffs =Subject.objects.all()
    staffs.delete()
    return redirect('/web_admin/staffs_detail/')

        
    