from datetime import datetime
import io 
import csv 

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import get_template
from xhtml2pdf import pisa

from web_super_admin.models import *
from .models import *

def payslip(request, pk):
    # get the data to be applied for pdf generation

    school_name = "my school",
    employee_name = "employee name",
    generation_date = datetime.now(),

    payslip_data = {
        'school_name' : school_name,
        'employee_name' : employee_name,
        'generation_date' : generation_date,
    }

    template = get_template("pdf/payslip.html")
    payslip_html = template.render(payslip_data)

    response = HttpResponse(content_type = "application/pdf")
    response['Content-Disposition'] = 'filename = "payslip.pdf"'

    pisa_status = pisa.CreatePDF(payslip_html, desc = response)

    if pisa_status.err:
        return HttpResponse("error generating the pdf")
    
    return response 
