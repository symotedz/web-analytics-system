from django.urls import path
from . import views

app_name = 'web_student'

urlpatterns = [
    path('', views.index)
]
