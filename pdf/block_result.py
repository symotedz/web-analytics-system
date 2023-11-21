from datetime import datetime

from xhtml2pdf import pisa
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import get_template

from .models import *
from web_super_admin .models import *
from web_super_admin .forms import *

def block_result_pdf(request, pk):
    school_name = "my school"
    block_name = "my block"
    date = datetime.now()
    
    block_result_data = {
        'school_name' : school_name,
        'block_name' : block_name,
        'date' : date,
    }

    response = HttpResponse(content_type = "application/pdf")
    response['Content-Disposition'] = 'file_name = "block_result.pdf"'

    template = get_template("pdf/block_result.html")
    exam_result_html = template.render(block_result_data)

    pisa_status = pisa.CreatePDF(exam_result_html, desc = response)

    if pisa_status.err:
        return HttpResponse("could not generate the pdf")
    
    return response