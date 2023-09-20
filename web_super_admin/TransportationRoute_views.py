from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from web_super_admin.models import *
from web_super_admin.forms import *

# view for creating new TransportationRoute
def TransportationRoute_create(request):
    form = TransportationRouteForm(request.POST)
    if request.method == 'POST':
        form = TransportationRouteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/web_admin/TransportationRoutes_detail/')
    else:
        form = TransportationRouteForm(request.POST)
    context = {
        'form' : form
    }
    return render(request, 'webadmin/TransportationRoute_create.html', context)

# view for reading all TransportationRoutes
def TransportationRoutes_detail(request):
    transportationRoutes = TransportationRoute.objects.all()
    context = {
        'transportationRoutes' : transportationRoutes
    }
    return render(request, 'webadmin/TransportationRoutes_detail.html', context)

# view for reading a single user

def TransportationRoute_detail(request, pk):
    transportationRoute = get_object_or_404(TransportationRoute, pk=pk)
    context = {
        'transportationRoute' : transportationRoute
    }
    return render(request, 'webadmin/TransportationRoute_detail.html', context)

# view for updating a single user
def TransportationRoute_update(request, pk):
    transportationRoute = get_object_or_404(TransportationRoute, pk=pk)
    form = TransportationRouteForm(request.POST, instance = transportationRoute)
    if request.method == 'POST':
        form = TransportationRouteForm(request.POST, instance = transportationRoute)
        if form.is_valid():
            form.save()
            return redirect('/web_admin/TransportationRoutes_detail/')
    else:
        form = TransportationRouteForm(request.POST, instance = transportationRoute)
    context = {
        'form' : form,
        'transportationRoute' : transportationRoute
    }
    return render(request, 'webadmin/TransportationRoute_update.html', context)

#view for deleting a single user
def TransportationRoute_delete(request, pk):
    transportationRoute = get_object_or_404(TransportationRoute, pk=pk)
    transportationRoute.delete()
    return redirect('/web_admin/TransportationRoutes_detail/')

# view for deleting all users
def TransportationRoutes_delete(request):
    transportationRoute =TransportationRoute.objects.all()
    transportationRoute.delete()
    return redirect('/web_admin/TransportationRoute_detail/')

        
    