from django.urls import path
from . import views 

app_name  = 'web_accountant'

urlpatterns = [
    path('', views.index)
]
