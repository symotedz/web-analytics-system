from django.urls import path
from . import class_resultViews
from . views import analyticscsv_index

app_name = 'analyticscsv'

urlpatterns = [
    path('', analyticscsv_index, name='analyticscsv_index'),
    path('export_csv/', class_resultViews.export_csv_view, name="export_csv")
]