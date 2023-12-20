from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from web_super_admin.models import class_block
from web_super_admin.forms import Class_blockForm



# view for reading all class_blocks
def class_blocks_detail(request):
    Class_blocks = class_block.objects.all()
    context = {
        'Class_blocks' : Class_blocks
    }
    return render(request, 'Dashboard/class_blocks_detail.html', context)

# view for reading a single user

def class_block_detail(request, pk):
    Class_block = get_object_or_404(class_block, pk=pk)
    context = {
        'Class_block' : Class_block
    }
    return render(request, 'Dashboard/class_block_detail.html', context)



        
    