import datetime as datetime
import csv 

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from web_super_admin.models import *
from web_super_admin.forms import *

def subject_result_csv(request):
    response = HttpResponse(content_type = "text/csv")
    response["content-disposition"] = 'attachment: filename="subject_result.csv"'
    writer = csv.writer(["firstName", "MiddleName", "LastName"])
    writer = csv.writer(["simon", "kamau", "waweru"])
    return response