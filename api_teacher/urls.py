from django.urls import path
from . import views
from . views import TeacherListCreateView, TeacherRetrieveUpdateDestroyView, class_blockListCreateView, class_blockRetrieveUpdateDestroyView
from . views import StudentListCreateView, StudentRetrieveUpdateDestroyView, EventListCreateView, EventRetrieveUpdateDestroyView
from . views import NoticeListCreateView, NoticeRetrieveUpdateDestroyView, SubjectListCreateView, SubjectRetrieveUpdateDestroyView
from . views import ExamListCreateView, ExamRetrieveUpdateDestroyView, ExamResultListCreateView, ExamResultRetrieveUpdateDestroyView
from . views import AttendanceListCreateView, AttendanceRetrieveUpdateDestroyView, AssignmentListCreateView, AssignmentRetrieveUpdateDestroyView
from . views import GradeListCreateView, GradeRetrieveUpdateDestroyView, OpportunitiesListCreateView, OpportunitiesRetrieveUpdateDestroyView
from . views import ELearningListCreateView, ElearningRetrieveUpdateDestroyView, MessageListCreateView, MessageRetrieveUpdateDestroyView
from . views import TimeTableListCreateView, TimeTableRetrieveUpdateDestroyView

app_name = 'api_teacher'

urlpatterns = [
    path('', views.index),

     # plans for teachers
    path('teachers/', TeacherListCreateView.as_view(), name='TeacherListCreateView'),
    path('teacher/<int:pk>/', TeacherRetrieveUpdateDestroyView.as_view(), name="TeacherRetrieveUpdateDestroyView"),

    #urls for class blocks
    path('class_blocks/', class_blockListCreateView.as_view(), name='class_blockListCreateView'),
    path('class_block/<int:pk>/', class_blockRetrieveUpdateDestroyView.as_view(), name='class_blockRetrieveUpdateDestroyView'),

    # urls for students
    path('students/', StudentListCreateView.as_view(), name='StudentListCreateView'),
    path('student/<int:pk>/', StudentRetrieveUpdateDestroyView.as_view(), name='StudentRetrieveUpdateDestroyView'),

    #urls for events
    path('events/', EventListCreateView.as_view(), name='EventListCreateView'),
    path('event/<int:pk>/', EventRetrieveUpdateDestroyView.as_view(), name='EventRetrieveUpdateDestroyView'),

    # urls for notices
    path('notice/', NoticeListCreateView.as_view(), name='NoticeListCreateView'),
    path('notice/<int:pk>/', NoticeRetrieveUpdateDestroyView.as_view(), name='NoticeRetrieveUpdateDestroyView'),

     # urls for subjects
    path('subjects/', SubjectListCreateView.as_view(), name='SubjectListCreateView'),
    path('subject/<int:pk>/', SubjectRetrieveUpdateDestroyView.as_view(), name="SubjectRetrieveUpdateDestroyView"),

    # urls for exam
    path('exams', ExamListCreateView.as_view(), name='ExamListCreateView'),
    path('exam/<int:pk>/', ExamRetrieveUpdateDestroyView.as_view(), name='ExamRetrieveUpdateDestroyView'),

    # urls for exam result
    path('examresults/', ExamResultListCreateView.as_view(), name='ExamResultListCreateView'),
    path('examresult/<int:pk>/', ExamResultRetrieveUpdateDestroyView.as_view(), name = "ExamResultRetrieveUpdateDestroyView"),

    # urls for attendance
    path('attendances/', AttendanceListCreateView.as_view(), name='AttendanceListCreateView'),
    path('atendance/<int:pk>/', AttendanceRetrieveUpdateDestroyView.as_view(), name='AttendanceRetrieveUpdateDestroyView'),

    # urls for assignment
    path('assignments/', AssignmentListCreateView.as_view(), name='AssignmentListCreateView'),
    path('assignment/<int:pk>', AssignmentRetrieveUpdateDestroyView.as_view(), name='AssignmentRetrieveUpdateDestroyView'),

     # urls for grade
    path('grades/', GradeListCreateView.as_view(), name='GradeListCreateView'),
    path('grade/<int:pk>/', GradeRetrieveUpdateDestroyView.as_view(), name="GradeRetrieveUpdateDestroyView"),

    # urls for opportunities
    path('opportunities/', OpportunitiesListCreateView.as_view(), name='OpportunitiesListCreateView'),
    path('opportunity/<int:pk>/', OpportunitiesRetrieveUpdateDestroyView.as_view(), name='OpportunitiesRetrieveUpdateDestroyView'),

    # urls for elearning
    path('elearnings/', ELearningListCreateView.as_view(), name='ELearningListCreateView'),
    path('elearning/<int:pk>/', ElearningRetrieveUpdateDestroyView.as_view(), name='ELearningRetrieveUpdateDestroyView'),

    # urls for messages
    path('messages/', MessageListCreateView.as_view(), name='MessageListCreateView'),
    path('message/<int:pk>/',  MessageRetrieveUpdateDestroyView.as_view(), name='MessageRetrieveUpdateDestroyView'),

    #urls for timetable
    path('timetables/', TimeTableListCreateView.as_view(), name='TimeTableListCreateView'),
    path('timetable/<int:pk>/', TimeTableRetrieveUpdateDestroyView.as_view(), name='TimeTableRetrieveUpdateDestroyView'),
]
