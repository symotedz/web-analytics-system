from django.urls import path
from django.http import HttpResponse
from . views import dataAnalysis_Index

app_name = 'dataAnalysis'

urlpatterns = [
    path('', dataAnalysis_Index, name='dataAnalysis_Index'),
]