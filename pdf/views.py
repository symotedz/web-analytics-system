from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def pdf_index(request):
    return HttpResponse('Hello pdf generator')
