from datetime import datetime 

from django.shortcuts import render, redirect, get_object_or_404

from web_super_admin.models import *
from web_super_admin.forms import *

def exam_result_view(request, pk):
    examResult = get_object_or_404(ExamResult);
    context = {
        examResult : "examResult"
    }
