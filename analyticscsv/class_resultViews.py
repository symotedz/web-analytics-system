from datetime import datetime
import csv

from django.http import HttpResponse

from .models import *

def export_csv_view(request):
    response = HttpResponse(content_type = "text/csv")
    response['content-disposition'] = 'attachment: file_name="data.csv"'
    writer = csv.writer(["FirstName", "LastName", "Proffesional"])
    writer = csv.writer(["simon", "kamau", "Software Engineer"])
    return response