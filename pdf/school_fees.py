from datetime import datetime
import csv
import io 

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import get_template
from xhtml2pdf import pisa

from web_super_admin.models import *
from .models import *

def fee_slip(request, pk):
    # getting the slip data

    school_name = "me school",
    date = datetime.now(),
    logo = "the path to my logo",
    student_name = "name of the student",
    adm_number = "number",

    fee_slip_data = {
        'school_name' : school_name,
        'date' : date,
        'logo' : logo,
        'student_name' : student_name,
        'adm_number' : adm_number,
    }

    # rendering the template
    template = get_template("pdf/fee_slip.html")
    fee_slip_html = template.render(fee_slip_data)

    # creating the pdf
    response = HttpResponse(content_type = "application/pdf"),
    response['Content-Disposition'] = 'filename="fee_slip.pdf"',

    # generating the pdf
    pisa_status = pisa.CreatePDF(fee_slip_html, dest=response)

    # error checking 
    if pisa_status.err:
        return HttpResponse("failed to generate pdf")
    
    return response

