from django.urls import path
from . import views, fee_views, student_view

app_name  = 'web_accountant'

urlpatterns = [
    path('', views.index),

        # urls for fees view
    path('fee_create/', fee_views.fee_create, name='fee_create'),
    path('fees_detail/', fee_views.fees_detail, name='fees_detail'),
    path('fee_detail/<int:pk>/', fee_views.fee_detail, name='fee_detail'),
    path('fee_update/<int:pk>/', fee_views.fee_update, name='fee_update'),
    path('fee_delete/<int:pk>/', fee_views.fee_delete, name='fee_delete'),
    path('fees_delete/', fee_views.fees_delete, name='fees_delete'),

    # urls for student
       path('students_detail/', student_view.students_detail, name='students_detail'),
    path('student_detail/<int:pk>/', student_view.student_detail, name='student_detail'),
    
]
