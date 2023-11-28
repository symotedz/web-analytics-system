from django.urls import path 
from . import views
from . views import StaffListCreateView, StaffRetrieveUpdateDestroyView, FeeListCreateView, FeeRetrieveUpdateDestroyView
from . views import NoticeListCreateView, NoticeRetrieveUpdateDestroyView, EventListCreateView, EventRetrieveUpdateDestroyUpdateView
from . views import MessageListCreateView, MessageRetrieveUpdateDestroyView 

app_name = 'api_accountant'

urlpatterns = [
    path('', views.index),

    # urls endpoint for staffs
    path('staff/<int:pk>/', StaffRetrieveUpdateDestroyView.as_view(), name="staff"),
    path('staffs/', StaffListCreateView.as_view(), name='staffs'),

    # urls endpoints for fees
    path("fees/", FeeListCreateView.as_view(), name="fees"),
    path("fee/<int:pk>/", FeeRetrieveUpdateDestroyView.as_view(), name="fee"),

    # urls endpoints for Notices
    path("notices/", NoticeListCreateView.as_view(), name="notices"),
    path("fee/<int:pk>/", NoticeRetrieveUpdateDestroyView.as_view(), name="fee"),

    # urls for event
    path("events/", EventListCreateView.as_view(), name="events"),
    path("event/<int:pk>/", EventRetrieveUpdateDestroyUpdateView.as_view(), name="event"),

    # urls for messages
    path("messages/", MessageListCreateView.as_view(), name="messages"),
    path("message/<int:pk>/", MessageRetrieveUpdateDestroyView.as_view(), name="message"),
]
