from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from web_super_admin.models import Assignment
from web_super_admin.forms import AssignmentForm

# view for creating new assignment


# view for reading all assignments
def assignments_detail(request):
    assignments = Assignment.objects.all()
    context = {
        'assignments' : assignments
    }
    return render(request, 'Dashboard/assignments_detail.html', context)

# view for reading a single user

def assignment_detail(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk)
    context = {
        'assignment' : assignment
    }
    return render(request, 'Dashboard/assignment_detail.html', context)

# view for updating a single user




        
    