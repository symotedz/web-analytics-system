from datetime import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from web_super_admin.models import CashOut
from .forms import CashOutForm

def CashOutCreate(request):
    if request.method == 'POST':
        form = CashOutForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = CashOutForm(request.POST)
        context = {
            "form" : form
        }
        return render(request, "index.html", context)
    