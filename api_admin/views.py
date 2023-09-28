from django.shortcuts import render
from django.http import HttpResponse
from . serializers import *
from web_super_admin.models import *
from api_super_admin.serializers import *
from rest_framework import generics

# Create your views here.
def index(request):
    return HttpResponse("Hello, World")

class PlanListCreateView(generics.ListCreateAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    
class TeacherListCreateView(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    
class StaffListCreateView(generics.ListCreateAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    
    
class School_blocksListCreateView(generics.ListCreateAPIView):
    queryset = School_blocks.objects.all()
    serializer_class = School_blocksSerializer
    
class class_blockListCreateView(generics.ListCreateAPIView):
    queryset = class_block.objects.all()
    serializer_class = class_blockSerializer
    
class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
class class_createListCreateView(generics.ListCreateAPIView):
    queryset = class_create.objects.all()
    serializer_class = class_createSerializer
    
class FeeListCreateView(generics.ListCreateAPIView):
    queryset = Fee.objects.all()
    serializer_class = FeeSerializer
    
class  LibraryCategoryListCreateView(generics.ListCreateAPIView):
    queryset =  LibraryCategory.objects.all()
    serializer_class =  LibraryCategorySerializer
    
class LibraryItemListCreateView(generics.ListCreateAPIView):
    queryset = LibraryItem.objects.all()
    serializer_class = LibraryItemSerializer


class LibraryItemCopyListCreateView(generics.ListCreateAPIView):
    queryset = LibraryItemCopy.objects.all()
    serializer_class = LibraryItemCopySerializer
    
class LibraryReservationListCreateView(generics.ListCreateAPIView):
    queryset = LibraryReservation.objects.all()
    serializer_class = LibraryReservationSerializer
    
class EventListCreateAPIView(generics.ListCreateAPIView):
    queryset=Event.objects.all()
    serializer_class = EventSerializer
    
class NoticeListCreateView(generics.ListCreateAPIView):
    queryset = Notice.objects.all() #get only last ten notices
    serializer_class = NoticeSerializer

class ExamListCreateView(generics.ListCreateAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer