from datetime import datetime
import csv 
import io 

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import get_template
from xhtml2pdf import pisa

from web_super_admin.models import *
from .models import *

def subject_result_pdf(request, pk):
    # getting the nessesary data
     school_name = "my school",
     logo = "path to my logo",
     generation_date = datetime.now(),
     student_name = "the student name",
     adm_number = "adm number",

     subject_result_data = {
          'school_name' : school_name,
          'logo' : logo,
          'generation_date' : generation_date,
          'student_name' : student_name,
          'adm_number' : adm_number
     }

     template = get_template("pdf/subject_result_pdf.html")
     exam_result_html = template.render(exam_result_data)

     response = HttpResponse(content_type = "application/pdf")
     response['Content-Disposition'] = 'file_name = "subject_result.pdf"'

     pisa_status = pisa.CreatePDF(exam_result_html, desc = response)

     if pisa_status.err:
          return HttpResponse("pdf generation failed")
     
     return response