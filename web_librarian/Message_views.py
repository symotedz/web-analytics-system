from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from web_super_admin . models import Message
from web_super_admin . forms import MessageForm

# view for creating new Messages
def Message_create(request):
    form = MessageForm(request.POST)
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/super_admin/%20Messages_detail/')
    else:
        form = MessageForm(request.POST)
    context = {
        'form' : form
    }
    return render(request, 'Dashboard/Message_create.html', context)

# view for reading all Messages
def Messages_detail(request):
    Messages = Message.objects.all()
    context = {
        'Messages' : Messages
    }
    return render(request, 'Dashboard/Messages_detail.html', context)

# view for reading a single user

def Message_detail(request, pk):
    message = get_object_or_404(Message, pk=pk)
    context = {
        'message' : message
    }
    return render(request, 'Dashboard/Message_detail.html', context)

# view for updating a single user
def Message_update(request, pk):
    message = get_object_or_404(Message, pk=pk)
    form = MessageForm(request.POST, instance = message)
    if request.method == 'POST':
        form = MessageForm(request.POST, instance = message)
        if form.is_valid():
            form.save()
            return redirect('/super_admin/%20Messages_detail/')
    else:
        form = MessageForm(request.POST, instance = message)
    context = {
        'form' : form,
        'message' : message
    }
    return render(request, 'Dashboard/Message_update.html', context)

#view for deleting a single user
def Message_delete(request, pk):
    message = get_object_or_404(Message, pk=pk)
    message.delete()
    return redirect('/super_admin/%20Messages_detail/')

# view for deleting all users
def Messages_delete(request):
   message =Message.objects.all()
   message.delete()
   return redirect('/super_admin/%20Messages_detail/')

        
    