from django.urls import path
from . import views
from . views import ExamResultListCreateView, ExamResultRetrieveUpdateDestroyView, NoticeListCreateView, NoticeRetrieveUpdateDestroyView
from . views import EventListCreateView, EventRetrieveUpdateDestroyView, StudentListCreateView, StudentRetrieveUpdateDestroyView
from . views import FeeListCreateView, FeeRetrieveUpdateDestroyView, AssignmentListCreateView, AssignmentRetrieveUpdateDestroyView
from . views import ElearningListCreateView, ElearningRetrieveUpdateDestroyView, School_blocksListCreateView, School_blocksRetrieveUpdateDestroyView
from . views import ExamListCreateView, ExamRetrieveUpdateDestroyView, SubjectListCreateView, SubjectRetrieveUpdateDestroyView
from . views import class_blockListCreateView, class_blockRetrieveUpdateDestroyView, TimeTableListCreateView, TimeTableRetrieveUpdateDestroyView
from . views import TransportationRouteListCreateView, TransportationRouteRetrieveUpdateDestroyView


app_name = 'api_student'

# issue transportation request

urlpatterns = [
    path('', views.index),

    # urls for exam result
    path('examresults/', ExamResultListCreateView.as_view(), name='ExamResultListCreateView'),
    path('examresult/<int:pk>/', ExamResultRetrieveUpdateDestroyView.as_view(), name = "ExamResultRetrieveUpdateDestroyView"),

    
    # urls for notices
    path('notice/', NoticeListCreateView.as_view(), name='NoticeListCreateView'),
    path('notice/<int:pk>/', NoticeRetrieveUpdateDestroyView.as_view(), name='NoticeRetrieveUpdateDestroyView'),

    #urls for events
    path('events/', EventListCreateView.as_view(), name='EventListCreateView'),
    path('event/<int:pk>/', EventRetrieveUpdateDestroyView.as_view(), name='EventRetrieveUpdateDestroyView'),

    # urls for students
    path('students/', StudentListCreateView.as_view(), name='StudentListCreateView'),
    path('student/<int:pk>/', StudentRetrieveUpdateDestroyView.as_view(), name='StudentRetrieveUpdateDestroyView'),

    # urls for fee
    path('fees/', FeeListCreateView.as_view(), name='FeeListCreateView'),
    path('fee/<int:pk>/', FeeRetrieveUpdateDestroyView.as_view(), name="FeeRetrieveUpdateDestroyView"),

    # urls for assignment
    path('assignments/', AssignmentListCreateView.as_view(), name='AssignmentListCreateView'),
    path('assignment/<int:pk>', AssignmentRetrieveUpdateDestroyView.as_view(), name='AssignmentRetrieveUpdateDestroyView'),

    # urls for elearning
    path('elearnings/', ElearningListCreateView.as_view(), name='ELearningListCreateView'),
    path('elearning/<int:pk>/', ElearningRetrieveUpdateDestroyView.as_view(), name='ELearningRetrieveUpdateDestroyView'),

       # urls for school blocks
    path('school_blocks/', School_blocksListCreateView.as_view(), name='School_blocksListCreateView'),
    path('school_block/<int:pk>/', School_blocksRetrieveUpdateDestroyView.as_view(), name='School_blockRetrieveUpdateDestroy'),

    #urls for class blocks
    path('class_blocks/', class_blockListCreateView.as_view(), name='class_blockListCreateView'),
    path('class_block/<int:pk>/', class_blockRetrieveUpdateDestroyView.as_view(), name='class_blockRetrieveUpdateDestroyView'),

    # urls for exam
    path('exams', ExamListCreateView.as_view(), name='ExamListCreateView'),
    path('exam/<int:pk>/', ExamRetrieveUpdateDestroyView.as_view(), name='ExamRetrieveUpdateDestroyView'),

    
    # urls for subjects
    path('subjects/', SubjectListCreateView.as_view(), name='SubjectListCreateView'),
    path('subject/<int:pk>/', SubjectRetrieveUpdateDestroyView.as_view(), name="SubjectRetrieveUpdateDestroyView"),

    #urls for timetable
    path('timetables/', TimeTableListCreateView.as_view(), name='TimeTableListCreateView'),
    path('timetable/<int:pk>/', TimeTableRetrieveUpdateDestroyView.as_view(), name='TimeTableRetrieveUpdateDestroyView'),

        # urls for transportation list
    path('transportationroutelist/', TransportationRouteListCreateView.as_view(), name='TransportationRouteListCreateView'),
    path('transportationroute/<int:pk>/', TransportationRouteRetrieveUpdateDestroyView.as_view(), name='TransportationRouteRetrieveUpdateDestroyView'),


]
