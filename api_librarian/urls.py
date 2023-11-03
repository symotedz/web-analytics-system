from django.urls import path
from . import views

app_name = 'api_librarian'

urlpatterns = [
    path('', views.index)
]
