from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from web_super_admin.models import TimeTable


# view for reading all TimeTables
def TimeTables_detail(request):
    Timetables = TimeTable.objects.all()
    context = {
        'Timetables' : Timetables
    }
    return render(request, 'Dashboard/TimeTables_detail.html', context)

# view for reading a single Timetable

def TimeTable_detail(request, pk):
    Timetable = get_object_or_404(TimeTable, pk=pk)
    context = {
        'Timetable' : Timetable
    }
    return render(request, 'Dashboard/TimeTable_detail.html', context)

        
    