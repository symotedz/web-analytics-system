from django.urls import path
from . import views

app_name = 'api_parent'

urlpatterns = [
    path('', views.index)
]
