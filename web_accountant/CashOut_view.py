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
    
def CashOutUpdate(request, pk):
    cashout = get_object_or_404(CashOut, pk=pk)
    form  = CashOutForm(request.POST, instance = cashout)
    if request.method == "POST":
        form = form 
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = form
        context = {
            "form" : form
        }
        return render(request, "index.html", context)
    
def CashOutDelete(request, pk):
    cashout = get_object_or_404(CashOut, pk=pk)
    cashout.delete()
    return redirect('/')

def CashOutDeletes(request):
    cashout = CashOut.objects.all()
    cashout.delete()
    return redirect('/')

def cashoutdetail(request, pk):
    cashout = get_object_or_404(CashOut, pk=pk)
    context = {
        'cashout' : cashout
    }
    return render(request, "index.html", context)