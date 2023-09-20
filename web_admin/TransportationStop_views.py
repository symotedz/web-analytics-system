from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from web_super_admin.forms import *
from web_super_admin.models import *

# view for creating new TransportationStop
def TransportationStop_create(request):
    form = TransportationStopForm(request.POST)
    if request.method == 'POST':
        form = TransportationStopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/web_admin/TransportationStops_detail/')
    else:
        form = TransportationStopForm(request.POST)
    context = {
        'form' : form
    }
    return render(request, 'webadmin/TransportationStop_create.html', context)

# view for reading all TransportationStops
def TransportationStops_detail(request):
    transportationStops = TransportationStop.objects.all()
    context = {
        'transportationStops' : transportationStops
    }
    return render(request, 'webadmin/TransportationStops_detail.html', context)

# view for reading a single user

def TransportationStop_detail(request, pk):
    TransportationStop = get_object_or_404(TransportationStop, pk=pk)
    context = {
        'TransportationStop' : TransportationStop
    }
    return render(request, 'webadmin/TransportationStop_detail.html', context)

# view for updating a single user
def TransportationStop_update(request, pk):
    transportationStop = get_object_or_404(TransportationStop, pk=pk)
    form = TransportationStopForm(request.POST, instance = transportationStop)
    if request.method == 'POST':
        form = TransportationStopForm(request.POST, instance = transportationStop)
        if form.is_valid():
            form.save()
            return redirect('/web_admin/TransportationStops_detail/')
    else:
        form = TransportationStopForm(request.POST, instance = transportationStop)
    context = {
        'form' : form,
        'transportationStop' : transportationStop
    }
    return render(request, 'webadmin/TransportationStop_update.html', context)

#view for deleting a single user
def TransportationStop_delete(request, pk):
    transportationStop = get_object_or_404(TransportationStop, pk=pk)
    transportationStop.delete()
    return redirect('/web_admin/TransportationStops_detail/')

# view for deleting all users
def TransportationStops_delete(request):
    transportationStop =TransportationStop.objects.all()
    transportationStop.delete()
    return redirect('/web_admin/TransportationStop_detail/')

        
    