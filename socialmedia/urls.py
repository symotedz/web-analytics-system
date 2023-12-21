from django.urls import path
from . views import social_media_index
from . OpportunityView import opportunity_create, opportunity_delete,  opportunity_detail, opportunity_edit, opportunity_list

app_name = 'socialmedia'

urlpatterns = [
    path('', social_media_index, name='social_media_index'),

    # Urls for Opportunities
    path('opportunities/', opportunity_list, name='opportunity_list'),
    path('opportunities/<int:pk>/', opportunity_detail, name='opportunity_detail'),
    path('opportunities/new/', opportunity_create, name='opportunity_create'),
    path('opportunities/<int:pk>/edit/', opportunity_edit, name='opportunity_edit'),
    path('opportunities/<int:pk>/delete/', opportunity_delete, name='opportunity_delete'),
]