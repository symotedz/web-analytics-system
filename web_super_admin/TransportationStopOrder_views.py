from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# view for creating new TransportationStopOrder
def TransportationStopOrder_create(request):
    form = TransportationStopOrderForm(request.POST)
    if request.method == 'POST':
        form = TransportationStopOrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/super_admin/TransportationStopOrders_detail/')
    else:
        form = TransportationStopOrderForm(request.POST)
    context = {
        'form' : form
    }
    return render(request, 'Dashboard/TransportationStopOrder_create.html', context)

# view for reading all TransportationStopOrders
def TransportationStopOrders_detail(request):
    transportationStopOrders = TransportationStopOrder.objects.all()
    context = {
        'transportationStopOrders' : transportationStopOrders
    }
    return render(request, 'Dashboard/TransportationStopOrders_detail.html', context)

# view for reading a single user

def TransportationStopOrder_detail(request, pk):
    TransportationStopOrder = get_object_or_404(TransportationStopOrder, pk=pk)
    context = {
        'TransportationStopOrder' : TransportationStopOrder
    }
    return render(request, 'Dashboard/TransportationStopOrder_detail.html', context)

# view for updating a single user
def TransportationStopOrder_update(request, pk):
    transportationStopOrder = get_object_or_404(TransportationStopOrder, pk=pk)
    form = TransportationStopOrderForm(request.POST, instance = transportationStopOrder)
    if request.method == 'POST':
        form = TransportationStopOrderForm(request.POST, instance = transportationStopOrder)
        if form.is_valid():
            form.save()
            return redirect('/super_admin/TransportationStopOrders_detail/')
    else:
        form = TransportationStopOrderForm(request.POST, instance = transportationStopOrder)
    context = {
        'form' : form,
        'transportationStopOrder' : transportationStopOrder
    }
    return render(request, 'Dashboard/TransportationStopOrder_update.html', context)

#view for deleting a single user
def TransportationStopOrder_delete(request, pk):
    transportationStopOrder = get_object_or_404(TransportationStopOrder, pk=pk)
    transportationStopOrder.delete()
    return redirect('/super_admin/TransportationStopOrders_detail/')

# view for deleting all users
def TransportationStopOrders_delete(request):
    transportationStopOrder =TransportationStopOrder.objects.all()
    transportationStopOrder.delete()
    return redirect('/super_admin/TransportationStopOrder_detail/')

        
    