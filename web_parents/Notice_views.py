from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from web_super_admin. models import Notice




# view for reading all notices
def notices_detail(request):
    notices = Notice.objects.all()
    context = {
        'notices' : notices
    }
    return render(request, 'Dashboard/notices_detail.html', context)

# view for reading a single user

def notice_detail(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    context = {
        'notice' : notice
    }
    return render(request, 'Dashboard/notice_detail.html', context)




#developed with love by kamau waweru @simokamaa github

        
    