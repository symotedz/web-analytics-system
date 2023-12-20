from django.urls import path
from . import views
from . student_views import student_detail, students_detail
from . subject_views import subject_detail, subjects_detail
from . School_blocks_views import School_blocks_detail, School_blockss_detail
from . Notice_views import notice_detail, notices_detail
from . TimeTable_views import TimeTable_detail, TimeTables_detail
from . exam_views import exam_detail, exams_detail
from . Event_views import Event_detail, Events_detail
from . ELearning_views import ELearning_detail, ELearnings_detail
from . class_block_views import class_block_detail, class_blocks_detail
from . assignment_views import assignments_detail, assignment_detail
from . TransportationRequest_views import (
    TransportationRequest_create,
    TransportationRequests_detail,
    TransportationRequest_detail,
    TransportationRequest_update,
    TransportationRequest_delete,
    TransportationRequests_delete,
)


app_name = 'web_student'

urlpatterns = [
    path('', views.index),

    # Urls for Student
    path('students/', students_detail, name='students_detail'),
    path('students/<int:pk>/', student_detail, name='student_detail'),

    # Urls for Subjects
    path('subjects/', subjects_detail, name='subjects_detail'),
    path('subject/<int:pk>/', subject_detail, name='subject_detail'),

    # Urls for School Blocks
    path('school_blockss/', School_blockss_detail, name='school_blockss_detail'),
    path('school_blocks/<int:pk>/', School_blocks_detail, name='school_blocks_detail'),

    # Urls for Notices
    path('notices/', notices_detail, name='notices_detail'),
    path('notice/<int:pk>/', notice_detail, name='notice_detail'),

    # Urls for TimeTable
    path('timetables/', TimeTables_detail, name='timetables_detail'),
    path('timetables/<int:pk>/', TimeTable_detail, name='timetable_detail'),

    # Urls for Exam
    path('exams/', exams_detail, name='exams_detail'),
    path('exams/<int:pk>/', exam_detail, name='exam_detail'),

    # Urls for Event
    path('events/', Events_detail, name='events_detail'),
    path('event/<int:pk>/', Event_detail, name='event_detail'),

    # Elearning Urls
    path('elearnings/', ELearnings_detail, name='elearnings_detail'),
    path('elearnings/<int:pk>/', ELearning_detail, name='elearning_detail'),

    # Urls for class Blocks
    path('class_blocks/', class_blocks_detail, name='class_blocks_detail'),
    path('class_blocks/<int:pk>/', class_block_detail, name='class_block_detail'),

    # Urls for Assignment
    path('assignments/', assignments_detail, name='assignments_detail'),
    path('assignments/<int:pk>/', assignment_detail, name='assignment_detail'),

    # Urls for Transportation Request
    path('transportation_requests/create/', TransportationRequest_create, name='transportation_request_create'),
    path('transportation_requests/', TransportationRequests_detail, name='transportation_requests_detail'),
    path('transportation_requests/<int:pk>/', TransportationRequest_detail, name='transportation_request_detail'),
    path('transportation_requests/<int:pk>/update/', TransportationRequest_update, name='transportation_request_update'),
    path('transportation_requests/<int:pk>/delete/', TransportationRequest_delete, name='transportation_request_delete'),
    path('transportation_requests/delete-all/', TransportationRequests_delete, name='transportation_requests_delete_all'),
]
