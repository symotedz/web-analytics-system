from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def dataAnalysis_Index(request):
    return HttpResponse("Hello Data Analysis")
