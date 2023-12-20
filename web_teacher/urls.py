from django.urls import path
from . import views , Message_views # noqa
from . OpportunityView import opportunity_list, opportunity_detail
from . import ELearning_views, Event_views, exam_result_pdf_view, exam_views, ExamResult_views
from . class_block_views import class_block_detail, class_blocks_detail
from . School_blocks_views import School_blocks_detail, School_blockss_detail
from . TimeTable_views import TimeTable_detail, TimeTables_detail

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
    path('Events_detail/', Event_views.Events_detail, name='Events_detail'),
    path('Event_detail/<int:pk>/', Event_views.Event_detail, name='Event_detail'),


    # urls for ExamResult view
    path('ExamResult_create/', ExamResult_views.ExamResult_create, name='ExamResult_create'),
    path('ExamResults_detail/', ExamResult_views.ExamResults_detail, name='ExamResults_detail'),
    path('ExamResult_detail/<int:pk>/', ExamResult_views.ExamResult_detail, name='ExamResult_detail'),
    path('ExamResult_update/<int:pk>/', ExamResult_views.ExamResult_update, name='ExamResult_update'),
    path('ExamResult_delete/<int:pk>/', ExamResult_views.ExamResult_delete, name='ExamResult_delete'),
    path('ExamResults_delete/', ExamResult_views.ExamResults_delete, name='ExamResults_delete'),

    # urls for Message view
    path(' Message_create/',  Message_views.Message_create, name='Message_create'),
    path(' Messages_detail/',  Message_views.Messages_detail, name='Messages_detail'),
    path(' Message_detail/<int:pk>/',  Message_views.Message_detail, name='Message_detail'),
    path(' Message_update/<int:pk>/',  Message_views.Message_update, name='Message_update'),
    path(' Message_delete/<int:pk>/',  Message_views.Message_delete, name='Message_delete'),
    path(' Messages_delete/',  Message_views.Messages_delete, name='Messages_delete'),

    # Urls for exams view
    path('exams_detail/', exam_views.exams_detail, name='exams_detail'),
    path('exam_detail/<int:pk>/', exam_views.exam_detail, name='exam_detail'),

    # Urls for School Blocks
    path('school_blockss/', School_blockss_detail, name='school_blockss_detail'),
    path('school_blocks/<int:pk>/', School_blocks_detail, name='school_blocks_detail'),

    # Urls for class Blocks
    path('class_blocks/', class_blocks_detail, name='class_blocks_detail'),
    path('class_blocks/<int:pk>/', class_block_detail, name='class_block_detail'),


    # Urls for Opportunity
    path('opportunities/', opportunity_detail, name='opportunity_detail'),
    path('opportunity/<int:pk>/', opportunity_list, name='opportunity_detail'),

     # Urls for TimeTable
    path('timetables/', TimeTables_detail, name='timetables_detail'),
    path('timetables/<int:pk>/', TimeTable_detail, name='timetable_detail'),
]
