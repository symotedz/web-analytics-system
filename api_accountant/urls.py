from django.urls import path 
from . import views

app_name = 'api_accountant'

urlpatterns = [
    path('', views.index)
]
