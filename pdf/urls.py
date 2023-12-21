from django.urls import path
from django.http import HttpResponse
from . views import pdf_index

app_name = 'pdf'

urlpatterns = [
    path('', pdf_index, name='pdf_index'),
]