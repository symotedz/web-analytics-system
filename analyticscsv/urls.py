from django.urls import path
from . import class_resultViews

urlpatterns = [
    path('export_csv/', class_resultViews.export_csv_view, name="export_csv")
]