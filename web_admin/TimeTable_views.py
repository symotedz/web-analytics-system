from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from . models import *
from web_super_admin.forms import *
from web_super_admin.models import *

# view for creating new TimeTables
def TimeTable_create(request):
    form = TimeTableForm(request.POST)
    if request.method == 'POST':
        form = TimeTableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/web_admin/%20TimeTables_detail/')
    else:
        form = TimeTableForm(request.POST)
    context = {
        'form' : form
    }
    return render(request, 'webadmin/TimeTable_create.html', context)

# view for reading all TimeTables
def TimeTables_detail(request):
    Timetables = TimeTable.objects.all()
    context = {
        'Timetables' : Timetables
    }
    return render(request, 'webadmin/TimeTables_detail.html', context)

# view for reading a single Timetable

def TimeTable_detail(request, pk):
    Timetable = get_object_or_404(TimeTable, pk=pk)
    context = {
        'Timetable' : Timetable
    }
    return render(request, 'webadmin/TimeTable_detail.html', context)

# view for updating a single Timetable
def TimeTable_update(request, pk):
    Timetable = get_object_or_404(TimeTable, pk=pk)
    form = TimeTableForm(request.POST, instance = Timetable)
    if request.method == 'POST':
        form = TimeTableForm(request.POST, instance = Timetable)
        if form.is_valid():
            form.save()
            return redirect('/web_admin/%20TimeTables_detail/')
    else:
        form = TimeTableForm(request.POST, instance = Timetable)
    context = {
        'form' : form,
        'Timetable' : Timetable
    }
    return render(request, 'webadmin/TimeTable_update.html', context)

#view for deleting a single Timetable
def TimeTable_delete(request, pk):
    Timetable = get_object_or_404(TimeTable, pk=pk)
    Timetable.delete()
    return redirect('/web_admin/%20TimeTables_detail/')

# view for deleting all Timetable
def TimeTables_delete(request):
   Timetable =TimeTable.objects.all()
   Timetable.delete()
   return redirect('/web_admin/%20TimeTables_detail/')

        
    