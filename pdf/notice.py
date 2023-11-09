from datetime import datetime 
import csv 
import io 

from django.template.loader import get_template
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from xhtml2pdf import pisa

from .models import *
from web_super_admin.models import *

def notice_pdf(request, pk):
    # getting the data for notice pdf
    school_name = "my school",
    headline = "my headline",
    generation_date = datetime.now(),
    logo = "path to my logo",

    # creating a dictionary to pass the data to the template
    notice_data = {
        'school_name' : school_name,
        'headline' : headline,
        'generation_date' : generation_date,
        'logo': logo
    }

    # render the payslip template with provided data
    template = get_template("pdf/notice.html")
    notice_html = template.render(notice_data)

    # create a PDF file
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="payslip.pdf"'

    # generate a PDF from the HTML using XHTML2pdf library
    pisa_status = pisa.CreatePDF(notice_html, dest=response)

    # check if the pdf generation was succesful
    if pisa_status.err:
        return HttpResponse('pdf generation failed.')
    
    return response