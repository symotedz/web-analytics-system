from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'web_super_admin_index'),
    

]