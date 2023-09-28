from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    if request.method == "POST":
        return redirect('super_admin/')
    return render(request, "login.html")
