from django.urls import path
from . views import system_admin_index

app_name = 'system_admin'

urlpatterns = [
    path('', system_admin_index, name='system_admin_index'),
]