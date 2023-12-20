from django.shortcuts import render, get_object_or_404, redirect
from web_super_admin.models import Opportunities


def opportunity_list(request):
    opportunities = Opportunities.objects.all()
    return render(request, 'opportunity_list.html', {'opportunities': opportunities})

def opportunity_detail(request, pk):
    opportunity = get_object_or_404(Opportunities, pk=pk)
    return render(request, 'opportunity_detail.html', {'opportunity': opportunity})

