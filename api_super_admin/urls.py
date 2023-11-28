from django.urls import path
from . import views
from . views import PlanListCreateView, PlanRetrieveUpdateDestroyView, TeacherListCreateView, TeacherRetrieveUpdateDestroyView
from . views import StaffListCreateView, StaffRetrieveUpdateDestroyView, School_blocksListCreateView, School_blockRetrieveUpdateDestroy
from . views import class_blockListCreateView, class_blockRetrieveUpdateDestroyView, StudentListCreateView, StudentRetrieveUpdateDestroyView
from . views import class_createListCreateView, classRetrieveUpdateDestroyView, FeeListCreateView, FeeRetrieveUpdateDestroyView
from . views import LibraryCategoryListCreateView, LibraryCategoryRetrieveUpdateDestroyView, LibraryItemListCreateView, LibraryItemRetrieveUpdateDestroyView
from . views import LibraryItemCopyListCreateView, LibraryItemCopyRetrieveUpdateDestroyView, LibraryReservationListCreateView, LibraryReservationRetrieveUpdateDestroy
from . views import EventListCreateView, EventRetrieveUpdateDestroyView, NoticeListCreateView, NoticeRetrieveUpdateDestroyView
from . views import SubjectListCreateView, SubjectRetrieveUpdateDestroyView, ExamListCreateView, ExamRetrieveUpdateDestroyView
from . views import ExamResultListCreateView, ExamResultRetrieveUpdateDestroyView, AttendanceListCreateView, AttendanceRetrieveUpdateDestroyView
from . views import AssignmentListCreateView, AssignmentRetrieveUpdateDestroyView, GradeListCreateView, GradeRetrieveUpdateDestroyView
from . views import TransportationRouteListCreateView, TransportationRouteRetrieveUpdateDestroyView
from . views import TransportationStopListCreateView, TransportationStopRetrieveUpdateDestroyView
from . views import TransportationStopOrderListCreateView,  TransportationStopOrderListRetrieveUpdateDestroyView
from . views import OpportunitiesListCreateView, OpportunitiesRetrieveUpdateDestroyView, ELearningListCreateView, ELearningRetrieveUpdateDestroyView
from . views import MessageListCreateView, MessageRetrieveUpdateDestroyView, TimeTableListCreateView, TimeTableRetrieveUpdateDestroyView

app_name = 'api_super_admin'

# an issue on school block

urlpatterns = [
    path('', views.index, name = 'web_super_admin_index'),

    # urls for plan
    path('plans/', PlanListCreateView.as_view(), name='PlanListCreateView'),
    path('plan/<int:pk>/',  PlanRetrieveUpdateDestroyView.as_view(), name=' PlanRetrieveUpdateDestroyView'),

    # plans for teachers
    path('teachers/', TeacherListCreateView.as_view(), name='TeacherListCreateView'),
    path('teacher/<int:pk>/', TeacherRetrieveUpdateDestroyView.as_view(), name="TeacherRetrieveUpdateDestroyView"),

    # urls for staffs
    path('staffs/', StaffListCreateView.as_view(), name='StaffListCreateView'),
    path('staff/<int:pk>/', StaffRetrieveUpdateDestroyView.as_view(), name='StaffRetrieveUpdateDestroyView'),

    # urls for school blocks
    path('school_blocks/', School_blocksListCreateView.as_view(), name='School_blocksListCreateView'),
    path('school_block/<int:pk>/', School_blockRetrieveUpdateDestroy.as_view(), name='School_blockRetrieveUpdateDestroy'),

    #urls for class blocks
    path('class_blocks/', class_blockListCreateView.as_view(), name='class_blockListCreateView'),
    path('class_block/<int:pk>/', class_blockRetrieveUpdateDestroyView.as_view(), name='class_blockRetrieveUpdateDestroyView'),

    # urls for students
    path('students/', StudentListCreateView.as_view(), name='StudentListCreateView'),
    path('student/<int:pk>/', StudentRetrieveUpdateDestroyView.as_view(), name='StudentRetrieveUpdateDestroyView'),

    # urls for classes
    path('classes/', class_createListCreateView.as_view(), name='class_createListCreateView'),
    path('class/<int:pk>/', classRetrieveUpdateDestroyView.as_view(), name='classRetrieveUpdateDestroyView'),

    # urls for fee
    path('fees/', FeeListCreateView.as_view(), name='FeeListCreateView'),
    path('fee/<int:pk>/', FeeRetrieveUpdateDestroyView.as_view(), name="FeeRetrieveUpdateDestroyView"),

    # urls for library category
    path('librarycategories/', LibraryCategoryListCreateView.as_view(), name='LibraryCategoryListCreateView'),
    path('librarycategory/<int:pk>/', LibraryCategoryRetrieveUpdateDestroyView.as_view(), name="LibraryCategoryRetrieveUpdateDestroyView"),

    # urls for library item
    path('libraryitems/', LibraryItemListCreateView.as_view(), name='LibraryItemListCreateView'),
    path('libraryitem/<int:pk>/', LibraryItemRetrieveUpdateDestroyView.as_view(), name="LibraryItemRetrieveUpdateDestroyView"),

    # urls for library item copy
    path('libraryitemcopies/', LibraryItemCopyListCreateView.as_view(), name='LibraryItemCopyListCreateView'),
    path('libraryitemcopy/', LibraryItemCopyRetrieveUpdateDestroyView.as_view(), name='LibraryItemCopyRetrieveUpdateDestroyView'),

    # urls for library researvation
    path('libraryreservations/', LibraryReservationListCreateView.as_view(), name='LibraryReservationListCreateView'),
    path('libraryresearvation/<int:pk>/', LibraryReservationRetrieveUpdateDestroy.as_view(), name='LibraryReservationRetrieveUpdateDestroy'),

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

    # urls for transportation request
    path('transportationrouterequests/', TransportationRouteListCreateView.as_view(), name='TransportationRouteListCreateView'),
    path('transportationroute/<int:pk>/', TransportationRouteRetrieveUpdateDestroyView.as_view(), name='TransportationRouteRetrieveUpdateDestroyView'),

    # urls for transportation list
    path('transportationroutelist/', TransportationRouteListCreateView.as_view(), name='TransportationRouteListCreateView'),
    path('transportationroute/<int:pk>/', TransportationRouteRetrieveUpdateDestroyView.as_view(), name='TransportationRouteRetrieveUpdateDestroyView'),

    # urls for transportation stop order
    path('transportationstoporders/', TransportationStopOrderListCreateView.as_view(), name='TransportationStopOrderListCreateView'),
    path('transportationstoporder/<int:pk>/', TransportationStopOrderListRetrieveUpdateDestroyView.as_view(), name='TransportationStopOrderListRetrieveUpdateDestroyView'),

    # urls for opportunities
    path('opportunities/', OpportunitiesListCreateView.as_view(), name='OpportunitiesListCreateView'),
    path('opportunity/<int:pk>/', OpportunitiesRetrieveUpdateDestroyView.as_view(), name='OpportunitiesRetrieveUpdateDestroyView'),

    # urls for elearning
    path('elearnings/', ELearningListCreateView.as_view(), name='ELearningListCreateView'),
    path('elearning/<int:pk>/', ELearningRetrieveUpdateDestroyView.as_view(), name='ELearningRetrieveUpdateDestroyView'),

    # urls for messages
    path('messages/', MessageListCreateView.as_view(), name='MessageListCreateView'),
    path('message/<int:pk>/',  MessageRetrieveUpdateDestroyView.as_view(), name='MessageRetrieveUpdateDestroyView'),

    #urls for timetable
    path('timetables/', TimeTableListCreateView.as_view(), name='TimeTableListCreateView'),
    path('timetable/<int:pk>/', TimeTableRetrieveUpdateDestroyView.as_view(), name='TimeTableRetrieveUpdateDestroyView'),
]