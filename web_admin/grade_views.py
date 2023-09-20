from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from web_super_admin.forms import *
from web_super_admin.models import *

# view for creating new grade
def grade_create(request):
    form = GradeForm(request.POST)
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/web_admin/grades_detail/')
    else:
        form = GradeForm(request.POST)
    context = {
        'form' : form
    }
    return render(request, 'webadmin/grade_create.html', context)

# view for reading all grades
def grades_detail(request):
    grades = Grade.objects.all()
    context = {
        'grades' : grades
    }
    return render(request, 'webadmin/grades_detail.html', context)

# view for reading a single user

def grade_detail(request, pk):
    grade = get_object_or_404(Grade, pk=pk)
    context = {
        'grade' : grade
    }
    return render(request, 'webadmin/grade_detail.html', context)

# view for updating a single user
def grade_update(request, pk):
    grade = get_object_or_404(Grade, pk=pk)
    form = GradeForm(request.POST, instance = grade)
    if request.method == 'POST':
        form = GradeForm(request.POST, instance = grade)
        if form.is_valid():
            form.save()
            return redirect('/web_admin/grades_detail/')
    else:
        form = GradeForm(request.POST, instance = grade)
    context = {
        'form' : form,
        'grade' : grade
    }
    return render(request, 'webadmin/grade_update.html', context)

#view for deleting a single user
def grade_delete(request, pk):
    grade = get_object_or_404(Grade, pk=pk)
    grade.delete()
    return redirect('/web_admin/grades_detail/')

# view for deleting all users
def grades_delete(request):
    grade =Grade.objects.all()
    grade.delete()
    return redirect('/web_admin/grade_detail/')

        
    