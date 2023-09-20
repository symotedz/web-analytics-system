from django.urls import path
from . import views  # noqa

urlpatterns = [
    path('', views.index)
]
