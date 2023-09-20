from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from . models import *
from web_super_admin.forms import *
from web_super_admin.models import *

# view for creating new Plan
def Plan_create(request):
    form = PlanForm(request.POST)
    if request.method == 'POST':
        form = PlanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/web_admin/Plans_detail/')
    else:
        form = PlanForm(request.POST)
    context = {
        'form' : form
    }
    return render(request, 'webadmin/Plan_create.html', context)

# view for reading all Plans
def Plans_detail(request):
    plans = Plan.objects.all()
    context = {
        'plans' : plans
    }
    return render(request, 'webadmin/Plans_detail.html', context)

# view for reading a single user

def Plan_detail(request, pk):
    plan = get_object_or_404(Plan, pk=pk)
    context = {
        'plan' : plan
    }
    return render(request, 'webadmin/Plan_detail.html', context)

# view for updating a single user
def Plan_update(request, pk):
    plan = get_object_or_404(Plan, pk=pk)
    form = PlanForm(request.POST, instance = plan)
    if request.method == 'POST':
        form = PlanForm(request.POST, instance = plan)
        if form.is_valid():
            form.save()
            return redirect('/web_admin/Plans_detail/')
    else:
        form = PlanForm(request.POST, instance = plan)
    context = {
        'form' : form,
        'plan' : plan
    }
    return render(request, 'webadmin/Plan_update.html', context)

#view for deleting a single user
def Plan_delete(request, pk):
    plan = get_object_or_404(Plan, pk=pk)
    plan.delete()
    return redirect('/web_admin/Plans_detail/')

# view for deleting all users
def Plans_delete(request):
    plans = Plan.objects.all()
    plans.delete()
    return redirect('/web_admin/Plans_detail/')

        
    