from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from web_super_admin. models import Event




# view for reading all Events
def Events_detail(request):
    events = Event.objects.all()
    context = {
        'events' : events
    }
    return render(request, 'Dashboard/Events_detail.html', context)

# view for reading a single user

def Event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    context = {
        'event' : event
    }
    return render(request, 'Dashboard/Event_detail.html', context)

# view for updating a single user


        
    