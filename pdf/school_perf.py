from datetime import datetime
import csv 
import io 

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from xhtml2pdf import pisa 
from django.template.loader import get_template

from web_super_admin.models import *
from .models import *

def school_perfomance_pdf(request):
    school_name = "my school";
    gen_date = datetime.now()
    principle = "school principle"

    school_perfomance_data = {
        'school_name' : school_name,
        'gen_date' : gen_date,
        'principle' : principle
    }

    template = get_template("pdf/school_result.html")
    school_slip_html = template.render(school_perfomance_data)

    response = HttpResponse(content_type = "application/pdf")
    response['Content-Disposition'] = 'filename = "fee_slip.pdf"',

    pisa_status = pisa.CreatePDF(school_slip_html, dest=response)

    if pisa_status.err:
        return HttpResponse("failed to generate pdf")
    
    return response

    