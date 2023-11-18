from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from web_super_admin.models import Notice
from web_super_admin.forms import NoticeForm

def Notices(request):
    notices = Notice.objects.all()
    context = {
        'notices' : notices
    }
    return render(request, "librarian/notices_detail.html", context)
    