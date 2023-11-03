from django.urls import path
from . import views
from . views import *

app_name = 'api_super_admin'

urlpatterns = [
    path('', views.index, name = 'web_super_admin_index'),
    path('plan/', PlanListCreateView.as_view(), name='PlanListCreateView'),
    path('teacher/', TeacherListCreateView.as_view(), name='TeacherListCreateView'),
    path('staff/', StaffListCreateView.as_view(), name='StaffListCreateView'),
    path('school_block/', School_blocksListCreateView.as_view(), name='School_blocksListCreateView'),
    path('class_block/', class_blockListCreateView.as_view(), name='class_blockListCreateView'),
    path('student/', StudentListCreateView.as_view(), name='StudentListCreateView'),
    path('class/', class_createListCreateView.as_view(), name='class_createListCreateView'),
    path('fee/', FeeListCreateView.as_view(), name='FeeListCreateView'),
    path('librarycategory/', LibraryCategoryListCreateView.as_view(), name='LibraryCategoryListCreateView'),
    path('libraryitem/', LibraryItemListCreateView.as_view(), name='LibraryItemListCreateView'),
    path('libraryitemcopy/', LibraryItemCopyListCreateView.as_view(), name='LibraryItemCopyListCreateView'),
    path('libraryreservation/', LibraryReservationListCreateView.as_view(), name='LibraryReservationListCreateView'),
    path('event/', EventListCreateView.as_view(), name='EventListCreateView'),
    path('notice/', NoticeListCreateView.as_view(), name='NoticeListCreateView'),
    path('subject/', SubjectListCreateView.as_view(), name='SubjectListCreateView'),
    path('exam', ExamListCreateView.as_view(), name='ExamListCreateView'),
    path('examresults/', ExamResultListCreateView.as_view(), name='ExamResultListCreateView'),
    path('attendance/', AttendanceListCreateView.as_view(), name='AttendanceListCreateView'),
    path('assignment/', AssignmentListCreateView.as_view(), name='AssignmentListCreateView'),
    path('grade/', GradeListCreateView.as_view(), name='GradeListCreateView'),
    path('transportationrouterequest/', TransportationRouteListCreateView.as_view(), name='TransportationRouteListCreateView'),
    path('transportationroutelist/', TransportationRouteListCreateView.as_view(), name='TransportationRouteListCreateView'),
    path('transportationstoporder/', TransportationStopOrderListCreateView.as_view(), name='TransportationStopOrderListCreateView'),
    path('opportunities/', OpportunitiesListCreateView.as_view(), name='OpportunitiesListCreateView'),
    path('eleraning/', ELearningListCreateView.as_view(), name='ELearningListCreateView'),
    path('messages/', MessageListCreateView.as_view(), name='MessageListCreateView'),
    path('timetable/', TimeTableListCreateView.as_view(), name='TimeTableListCreateView'),
]