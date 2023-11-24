from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from . models import *
from . forms import *

from web_super_admin.models import *
from web_super_admin.forms import *


# view for reading all students
def students_detail(request):
    students = Student.objects.all()
    context = {
        'students' : students
    }
    return render(request, 'Dashboard/students_detail.html', context)

# view for reading a single user

def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    context = {
        'student' : student
    }
    return render(request, 'Dashboard/student_detail.html', context)
