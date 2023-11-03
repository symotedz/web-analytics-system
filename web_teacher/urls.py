from django.urls import path
from . import views  # noqa

app_name = 'web_teacher'

urlpatterns = [
    path('', views.index)
]
