from django.shortcuts import render, get_object_or_404, redirect
from web_super_admin .models import Opportunities
from web_super_admin.forms import OpportunitiesForm

def opportunity_list(request):
    opportunities = Opportunities.objects.all()
    return render(request, 'opportunity_list.html', {'opportunities': opportunities})

def opportunity_detail(request, pk):
    opportunity = get_object_or_404(Opportunities, pk=pk)
    return render(request, 'opportunity_detail.html', {'opportunity': opportunity})

def opportunity_create(request):
    if request.method == 'POST':
        form = OpportunitiesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('opportunity_list')
    else:
        form = OpportunitiesForm()
    return render(request, 'opportunity_form.html', {'form': form})

def opportunity_edit(request, pk):
    opportunity = get_object_or_404(Opportunities, pk=pk)
    if request.method == 'POST':
        form = OpportunitiesForm(request.POST, instance=opportunity)
        if form.is_valid():
            form.save()
            return redirect('opportunity_list')
    else:
        form = OpportunitiesForm(instance=opportunity)
    return render(request, 'opportunity_form.html', {'form': form})

def opportunity_delete(request, pk):
    opportunity = get_object_or_404(Opportunities, pk=pk)
    opportunity.delete()
    return redirect('opportunity_list')
