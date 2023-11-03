from django.urls import path
from . import views

app_name = 'api_teacher'

urlpatterns = [
    path('', views.index)
]
