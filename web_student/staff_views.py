from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from web_super_admin . models import Staff




# view for reading all staffs
def staffs_detail(request):
    staffs = Staff.objects.all()
    context = {
        'staffs' : staffs
    }
    return render(request, 'Dashboard/staffs_detail.html', context)

# view for reading a single user

def staff_detail(request, pk):
    staff = get_object_or_404(Staff, pk=pk)
    context = {
        'staff' : staff
    }
    return render(request, 'Dashboard/staff_detail.html', context)


    