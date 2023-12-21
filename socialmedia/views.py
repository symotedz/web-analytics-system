from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def social_media_index(request):
    return HttpResponse("Hello Social Media Platform")
