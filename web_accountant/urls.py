from django.urls import path
from . import views, fee_views, student_view, staff_views, CashOut_view, Message_views
from . OpportunityView import opportunity_detail, opportunity_list

app_name  = 'web_accountant'

urlpatterns = [
    path('', views.index),

    # Urls for fees view
    path('fee_create/', fee_views.fee_create, name='fee_create'),
    path('fees_detail/', fee_views.fees_detail, name='fees_detail'),
    path('fee_detail/<int:pk>/', fee_views.fee_detail, name='fee_detail'),
    path('fee_update/<int:pk>/', fee_views.fee_update, name='fee_update'),
    path('fee_delete/<int:pk>/', fee_views.fee_delete, name='fee_delete'),
    path('fees_delete/', fee_views.fees_delete, name='fees_delete'),

     # urls for Message view
    path('Message_create/',  Message_views.Message_create, name='Message_create'),
    path('Messages_detail/',  Message_views.Messages_detail, name='Messages_detail'),
    path('Message_detail/<int:pk>/',  Message_views.Message_detail, name='Message_detail'),
    path('Message_update/<int:pk>/',  Message_views.Message_update, name='Message_update'),
    path('Message_delete/<int:pk>/',  Message_views.Message_delete, name='Message_delete'),
    path('Messages_delete/',  Message_views.Messages_delete, name='Messages_delete'),

    # Urls for cashout
    path('CashOutCreate/', CashOut_view.CashOutCreate, name= "CashOutCreate"),
    path('CashOutUpdate/<int:pk>/', CashOut_view.CashOutUpdate, name="CashOutUpdate"),

    # Urls for student
    path('students_detail/', student_view.students_detail, name='students_detail'),
    path('student_detail/<int:pk>/', student_view.student_detail, name='student_detail'),

    # Urls for staff
    path('staffs_detail/', staff_views.staffs_detail, name='staffs_detail'),
    path('staff_detail/<int:pk>/', staff_views.staff_detail, name='staff_detail'),
    
    # Urls for opportunities
    path('opportunities/', opportunity_list, name='opportunity_list'),
    path('opportunity/<int:pk>/', opportunity_detail, name='opportunity_detail'),
]
