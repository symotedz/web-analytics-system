from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics

from .serializers import *
from web_super_admin.models import *

# Create your views here.
def index(request):
    return HttpResponse("Hello World")

# view for listing and creating
class PlanListCreateView(generics.ListCreateAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

class PlanRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    
class TeacherListCreateView(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class TeacherRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    
class StaffListCreateView(generics.ListCreateAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

class StaffRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    
class School_blocksListCreateView(generics.ListCreateAPIView):
    queryset = School_blocks.objects.all()
    serializer_class = School_blocksSerializer

class School_blockRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset  = School_blocks.objects.all()
    serializer_class = School_blocksSerializer


class class_blockListCreateView(generics.ListCreateAPIView):
    queryset = class_block.objects.all()
    serializer_class = class_blockSerializer
    
class class_blockRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = class_block.objects.all()
    serializer_class = class_blockSerializer

class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
class class_createListCreateView(generics.ListCreateAPIView):
    queryset = class_create.objects.all()
    serializer_class = class_createSerializer

class classRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = class_create.objects.all()
    serializer_class = class_createSerializer
    
class FeeListCreateView(generics.ListCreateAPIView):
    queryset = Fee.objects.all()
    serializer_class = FeeSerializer

class FeeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fee.objects.all()
    serializer_class  = FeeSerializer
class LibraryCategoryListCreateView(generics.ListCreateAPIView):
    queryset = LibraryCategory.objects.all()
    serializer_class = LibraryCategorySerializer

class LibraryCategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LibraryCategory.objects.all()
    serializer_class = LibraryCategorySerializer
    
class LibraryItemListCreateView(generics.ListCreateAPIView):
    queryset = LibraryItem.objects.all()
    serializer_class = LibraryItemSerializer

class LibraryItemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LibraryItem.objects.all()
    serializer_class = LibraryItemSerializer
    
class LibraryItemCopyListCreateView(generics.ListCreateAPIView):
    queryset = LibraryItemCopy.objects.all()
    serializer_class = LibraryItemCopySerializer

class LibraryItemCopyRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset =  LibraryItemCopy.objects.all()
    serializer_class = LibraryItemCopySerializer
    
class LibraryReservationListCreateView(generics.ListCreateAPIView):
    queryset = LibraryReservation.objects.all()
    serializer_class = LibraryReservationSerializer

class EventListCreateView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    
class NoticeListCreateView(generics.ListCreateAPIView):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer
    
class SubjectListCreateView(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    
class ExamListCreateView(generics.ListCreateAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    
class ExamResultListCreateView(generics.ListCreateAPIView):
    queryset = ExamResult.objects.all()
    serializer_class = ExamResultSerializer
    
class AttendanceListCreateView(generics.ListCreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    
class AssignmentListCreateView(generics.ListCreateAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    
class GradeListCreateView(generics.ListCreateAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    
class TransportationRouteListCreateView(generics.ListCreateAPIView):
    queryset = TransportationRoute.objects.all()
    serializer_class = TransportationRouteSerializer
    
class TransportationStopListCreateView(generics.ListCreateAPIView):
    queryset = TransportationStop.objects.all()
    serializer_class = TransportationStopSerializer
    
class TransportationStopOrderListCreateView(generics.ListCreateAPIView):
    queryset = TransportationStopOrder.objects.all()
    serializer_class = TransportationStopOrderSerializer
    
class TransportationRequestListCreateView(generics.ListCreateAPIView):
    queryset = TransportationRequest.objects.all()
    serializer_class = TransportationRequestSerializer
    
class OpportunitiesListCreateView(generics.ListCreateAPIView):
    queryset = Opportunities.objects.all()
    serializer_class = OpportunitiesSerializer
    
class ELearningListCreateView(generics.ListCreateAPIView):
    queryset = ELearning.objects.all()
    serializer_class = ELearningSerializer
    
class MessageListCreateView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    
class TimeTableListCreateView(generics.ListCreateAPIView):
    queryset = TimeTable.objects.all()
    serializer_class = TimeTableSerializer
    
