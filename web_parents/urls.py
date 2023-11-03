from django.urls import path
from . import views 

app_name = 'web_parents'

urlpatterns = [
    path('', views.index)
]
