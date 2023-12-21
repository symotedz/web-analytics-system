from django.urls import path
from . views import social_media_index

app_name = 'socialmedia'

urlpatterns = [
    path('', social_media_index, name='social_media_index'),
]