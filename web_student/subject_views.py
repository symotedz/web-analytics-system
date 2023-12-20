from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from web_super_admin.models import Subject



# view for reading all subjects
def subjects_detail(request):
    subjects = Subject.objects.all()
    context = {
        'subjects' : subjects
    }
    return render(request, 'Dashboard/subjects_detail.html', context)

# view for reading a single user

def subject_detail(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    context = {
        'subject' : subject
    }
    return render(request, 'Dashboard/subject_detail.html', context)


        
    