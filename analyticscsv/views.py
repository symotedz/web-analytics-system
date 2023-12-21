from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def analyticscsv_index(request):
    return HttpResponse('Hello Analytics Csv')
