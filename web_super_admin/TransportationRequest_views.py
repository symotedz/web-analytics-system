from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# view for creating new TransportationRequest
def TransportationRequest_create(request):
    form = TransportationRequestForm(request.POST)
    if request.method == 'POST':
        form = TransportationRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/super_admin/TransportationRequests_detail/')
    else:
        form = TransportationRequestForm(request.POST)
    context = {
        'form' : form
    }
    return render(request, 'Dashboard/TransportationRequest_create.html', context)

# view for reading all TransportationRequests
def TransportationRequests_detail(request):
    transportationRequests = TransportationRequest.objects.all()
    context = {
        'transportationRequests' : transportationRequests
    }
    return render(request, 'Dashboard/TransportationRequests_detail.html', context)

# view for reading a single user

def TransportationRequest_detail(request, pk):
    transportationRequest = get_object_or_404(TransportationRequest, pk=pk)
    context = {
        'transportationRequest' : transportationRequest
    }
    return render(request, 'Dashboard/TransportationRequest_detail.html', context)
                                                                                    
# view for updating a single user
def TransportationRequest_update(request, pk):
    transportationRequest = get_object_or_404(TransportationRequest, pk=pk)
    form = TransportationRequestForm(request.POST, instance = transportationRequest)
    if request.method == 'POST':
        form = TransportationRequestForm(request.POST, instance = transportationRequest)
        if form.is_valid():
            form.save()
            return redirect('/super_admin/TransportationRequests_detail/')
    else:
        form = TransportationRequestForm(request.POST, instance = transportationRequest)
    context = {
        'form' : form,
        'transportationRequest' : transportationRequest
    }
    return render(request, 'Dashboard/TransportationRequest_update.html', context)

#view for deleting a single user
def TransportationRequest_delete(request, pk):
    transportationRequest = get_object_or_404(TransportationRequest, pk=pk)
    transportationRequest.delete()
    return redirect('/super_admin/TransportationRequests_detail/')

# view for deleting all users
def TransportationRequests_delete(request):
    transportationRequest =TransportationRequest.objects.all()
    transportationRequest.delete()
    return redirect('/super_admin/TransportationRequest_detail/')



        
    