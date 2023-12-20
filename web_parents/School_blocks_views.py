from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from web_super_admin.models import School_blocks




# view for reading all School_blockss
def School_blockss_detail(request):
    school_blockss = School_blocks.objects.all()
    context = {
        'school_blockss' : school_blockss
    }
    return render(request, 'Dashboard/School_blockss_detail.html', context)

# view for reading a single user

def School_blocks_detail(request, pk):
    school_blocks = get_object_or_404(School_blocks, pk=pk)
    context = {
        'school_blocks' : school_blocks
    }
    return render(request, 'Dashboard/School_blocks_detail.html', context)



        
    