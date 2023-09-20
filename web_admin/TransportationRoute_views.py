from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from web_super_admin.forms import *
from web_super_admin.models import *

# view for creating new TransportationRoute
def TransportationRoute_create(Route):
    form = TransportationRouteForm(Route.POST)
    if Route.method == 'POST':
        form = TransportationRouteForm(Route.POST)
        if form.is_valid():
            form.save()
            return redirect('/super_admin/TransportationRoutes_detail/')
    else:
        form = TransportationRouteForm(Route.POST)
    context = {
        'form' : form
    }
    return render(Route, 'Dashboard/TransportationRoute_create.html', context)

# view for reading all TransportationRoutes
def TransportationRoutes_detail(Route):
    transportationRoutes = TransportationRoute.objects.all()
    context = {
        'transportationRoutes' : transportationRoutes
    }
    return render(Route, 'Dashboard/TransportationRoutes_detail.html', context)

# view for reading a single user

def TransportationRoute_detail(Route, pk):
    transportationRoute = get_object_or_404(TransportationRoute, pk=pk)
    context = {
        'transportationRoute' : transportationRoute
    }
    return render(Route, 'Dashboard/TransportationRoute_detail.html', context)

# view for updating a single user
def TransportationRoute_update(Route, pk):
    transportationRoute = get_object_or_404(TransportationRoute, pk=pk)
    form = TransportationRouteForm(Route.POST, instance = transportationRoute)
    if Route.method == 'POST':
        form = TransportationRouteForm(Route.POST, instance = transportationRoute)
        if form.is_valid():
            form.save()
            return redirect('/super_admin/TransportationRoutes_detail/')
    else:
        form = TransportationRouteForm(Route.POST, instance = transportationRoute)
    context = {
        'form' : form,
        'transportationRoute' : transportationRoute
    }
    return render(Route, 'Dashboard/TransportationRoute_update.html', context)

#view for deleting a single user
def TransportationRoute_delete(Route, pk):
    transportationRoute = get_object_or_404(TransportationRoute, pk=pk)
    transportationRoute.delete()
    return redirect('/super_admin/TransportationRoutes_detail/')

# view for deleting all users
def TransportationRoutes_delete(Route):
    transportationRoute =TransportationRoute.objects.all()
    transportationRoute.delete()
    return redirect('/super_admin/TransportationRoute_detail/')

        
    