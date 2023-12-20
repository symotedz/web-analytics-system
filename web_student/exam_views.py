from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from web_super_admin.models import Exam




# view for reading all exams
def exams_detail(request):
    exams = Exam.objects.all()
    context = {
        'exams' : exams
    }
    return render(request, 'Dashboard/exams_detail.html', context)

# view for reading a single user

def exam_detail(request, pk):
    exam = get_object_or_404(Exam, pk=pk)
    context = {
        'exam' : exam
    }
    return render(request, 'Dashboard/exam_detail.html', context)


        
    