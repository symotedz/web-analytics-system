from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def system_admin_index(request):
    return HttpResponse("hello system admin index")
