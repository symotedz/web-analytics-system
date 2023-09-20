from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from web_super_admin.forms import *
from web_super_admin.models import *

# view for creating new assignment
def assignment_create(request):
    form = AssignmentForm(request.POST)
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/web_admin/assignments_detail/')
    else:
        form = AssignmentForm(request.POST)
    context = {
        'form' : form
    }
    return render(request, 'webadmin/assignment_create.html', context)

# view for reading all assignments
def assignments_detail(request):
    assignments = Assignment.objects.all()
    context = {
        'assignments' : assignments
    }
    return render(request, 'webadmin/assignments_detail.html', context)

# view for reading a single user

def assignment_detail(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk)
    context = {
        'assignment' : assignment
    }
    return render(request, 'webadmin/assignment_detail.html', context)

# view for updating a single user
def assignment_update(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk)
    form = AssignmentForm(request.POST, instance = assignment)
    if request.method == 'POST':
        form = AssignmentForm(request.POST, instance = assignment)
        if form.is_valid():
            form.save()
            return redirect('/web_admin/assignments_detail/')
    else:
        form = AssignmentForm(request.POST, instance = assignment)
    context = {
        'form' : form,
        'assignment' : assignment
    }
    return render(request, 'webadmin/assignment_update.html', context)

#view for deleting a single user
def assignment_delete(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk)
    assignment.delete()
    return redirect('/web_admin/assignments_detail/')

# view for deleting all users
def assignments_delete(request):
    assignment =Assignment.objects.all()
    assignment.delete()
    return redirect('/web_admin/assignment_detail/')

        
    