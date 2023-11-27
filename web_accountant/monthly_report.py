from datetime import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import url

from web_super_admin.models import *
from web_super_admin.forms import *

from .models import *
from .forms import *

def monthlyReport(request):
    pass