from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from web_super_admin.forms import *
from web_super_admin.models import *

# view for creating new ELearning
def ELearning_create(request):
    form = ELearningForm(request.POST)
    if request.method == 'POST':
        form = ELearningForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/web_admin/%20ELearnings_detail/')
    else:
        form = ELearningForm(request.POST)
    context = {
        'form' : form
    }
    return render(request, 'webadmin/ELearning_create.html', context)

# view for reading all ELearnings
def ELearnings_detail(request):
    eLearnings = ELearning.objects.all()
    context = {
        'eLearnings' : eLearnings
    }
    return render(request, 'webadmin/ELearnings_detail.html', context)

# view for reading a single user

def ELearning_detail(request, pk):
    eLearning = get_object_or_404(ELearning, pk=pk)
    context = {
        'eLearning' : eLearning
    }
    return render(request, 'webadmin/ELearning_detail.html', context)

# view for updating a single user
def ELearning_update(request, pk):
    eLearning = get_object_or_404(ELearning, pk=pk)
    form = ELearningForm(request.POST, instance = eLearning)
    if request.method == 'POST':
        form = ELearningForm(request.POST, instance = eLearning)
        if form.is_valid():
            form.save()
            return redirect('/web_admin/%20ELearnings_detail/')
    else:
        form = ELearningForm(request.POST, instance = eLearning)
    context = {
        'form' : form,
        'eLearning' : eLearning
    }
    return render(request, 'webadmin/ELearning_update.html', context)

#view for deleting a single user
def ELearning_delete(request, pk):
    eLearning = get_object_or_404(ELearning, pk=pk)
    eLearning.delete()
    return redirect('/web_admin/%20ELearnings_detail/')

# view for deleting all users
def ELearnings_delete(request):
    eLearnings = ELearning.objects.all()
    eLearnings.delete()
    return redirect('/web_admin/%20ELearnings_detail/')

        
    