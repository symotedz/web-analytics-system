from datetime import datetime 
import sys
from django.shortcuts import render, redirect, get_object_or_404
from Analytics.config import *

sys.path.append('../')


system_name = SYSTEM_NAME
copyright = COPYRIGHT
logo = LOGO
ipadress = IP_ADRESS

def base(request):
    context = {
        'system_name' : system_name,
        'copyright' : copyright,
        'logo' : logo,
        'ipadress' : ipadress
    }
    return render(request, "Dashboard/base.html", context)

print(SYSTEM_NAME)

