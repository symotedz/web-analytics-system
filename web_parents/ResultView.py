import datetime as datetime

from django.shortcuts import render, redirect, get_object_or_404

from web_super_admin.models import *
from web_super_admin.forms import *

def exam_result_view(request, pk):
    exam_result = get_object_or_404(ExamResult, pk=pk)
    context = {
        'exam_result': exam_result,
    }
    return render(request, 'index.html', context)

