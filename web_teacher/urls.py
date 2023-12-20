from django.urls import path
from . import views  # noqa
from . OpportunityView import opportunity_list, opportunity_detail
from . import ELearning_views, Event_views, exam_result_pdf_view, exam_views, ExamResult_views

app_name = 'web_teacher'

urlpatterns = [
    path('', views.index),

    # urls for Elearning view
    path('ELearning_create/',  ELearning_views.ELearning_create, name='ELearning_create'),
    path('ELearnings_detail/',  ELearning_views.ELearnings_detail, name='ELearnings_detail'),
    path('ELearning_detail/<int:pk>/',  ELearning_views.ELearning_detail, name='ELearning_detail'),
    path('ELearning_update/<int:pk>/',  ELearning_views.ELearning_update, name='ELearning_update'),
    path('ELearning_delete/<int:pk>/',  ELearning_views.ELearning_delete, name='ELearning_delete'),
    path('ELearnings_delete/',  ELearning_views.ELearnings_delete, name='ELearnings_delete'),

    # urls for Event view
    path('Event_create/', Event_views.Event_create, name='Event_create'),
    path('Events_detail/', Event_views.Events_detail, name='Events_detail'),
    path('Event_detail/<int:pk>/', Event_views.Event_detail, name='Event_detail'),
    path('Event_update/<int:pk>/', Event_views.Event_update, name='Event_update'),
    path('Event_delete/<int:pk>/', Event_views.Event_delete, name='Event_delete'),
    path('Events_delete/', Event_views.Events_delete, name='Events_delete'),

    # urls for ExamResult view
    path('ExamResult_create/', ExamResult_views.ExamResult_create, name='ExamResult_create'),
    path('ExamResults_detail/', ExamResult_views.ExamResults_detail, name='ExamResults_detail'),
    path('ExamResult_detail/<int:pk>/', ExamResult_views.ExamResult_detail, name='ExamResult_detail'),
    path('ExamResult_update/<int:pk>/', ExamResult_views.ExamResult_update, name='ExamResult_update'),
    path('ExamResult_delete/<int:pk>/', ExamResult_views.ExamResult_delete, name='ExamResult_delete'),
    path('ExamResults_delete/', ExamResult_views.ExamResults_delete, name='ExamResults_delete'),

    # Urls for exams view
    path('exam_create/', exam_views.exam_create, name='exam_create'),
    path('exams_detail/', exam_views.exams_detail, name='exams_detail'),
    path('exam_detail/<int:pk>/', exam_views.exam_detail, name='exam_detail'),
    path('exam_update/<int:pk>/', exam_views.exam_update, name='exam_update'),
    path('exam_delete/<int:pk>/', exam_views.exam_delete, name='exam_delete'),
    path('exams_delete/', exam_views.exams_delete, name='exams_delete'),

    # Urls for Opportunity
    path('opportunities/', opportunity_detail, name='opportunity_detail'),
    path('opportunity/<int:pk>/', opportunity_list, name='opportunity_detail'),
]
