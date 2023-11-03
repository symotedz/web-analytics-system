from django.urls import path
from . import views

app_name = 'api_student'

urlpatterns = [
    path('', views.index)
]
