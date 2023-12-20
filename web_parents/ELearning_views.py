from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from web_super_admin.models import ELearning
from web_super_admin.forms import ELearningForm



# view for reading all ELearnings
def ELearnings_detail(request):
    eLearnings = ELearning.objects.all()
    context = {
        'eLearnings' : eLearnings
    }
    return render(request, 'Dashboard/ELearnings_detail.html', context)

# view for reading a single user

def ELearning_detail(request, pk):
    eLearning = get_object_or_404(ELearning, pk=pk)
    context = {
        'eLearning' : eLearning
    }
    return render(request, 'Dashboard/ELearning_detail.html', context)



        
    