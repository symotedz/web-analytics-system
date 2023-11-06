from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import generics

from web_super_admin.models import *
from .serializers import *
# Create your views here.

def index(request):
    return HttpResponse("Hello,World")

class ExamResultListCreateView(generics.ListCreateAPIView):
    examResult = ExamResult.objects.all()
    serializer_class = ExamResultSerializer

class NoticeListCreateView(generics.ListCreateAPIView):
    notice = Notice.objects.all()
    serializer_class = NoticeSerializer

class EventListCreateView(generics.ListCreateAPIView):
    event = Event.objects.all()
    serializer_class = EventSerializer

class StudentListCreateView(generics.ListCreateAPIView):
    student = Student.objects.all()
    serializer_class = StudentSerializer

class FeeListCreateView(generics.ListCreateAPIView):
    fee = Fee.objects.all()
    serializer_class = FeeSerializer

class AssignmentListCreateView(generics.ListCreateAPIView):
    assignment = Assignment.objects.all()
    serializer_class = AssignmentSerializer

class ElearningListCreateView(generics.ListCreateAPIView):
    elearning = ELearning.objects.all()
    serializer_class = ELearning

class School_blocksListCreateView(generics.ListCreateAPIView):
    schoolblocks = School_blocks.objects.all()
    serializer_class = School_blocksSerializer

class ExamListCreateView(generics.ListCreateAPIView):
    exam = Exam.objects.all()
    serializer_class = ExamSerializer

class SubjectListCreateView(generics.ListCreateAPIView):
    subject = Subject.objects.all()
    serializer_class = Subject

class TimeTableListCreateView(generics.ListCreateAPIView):
    timetable = TimeTable.objects.all()
    serializer_class = TimeTableSerializer

class TransportationRouteListCreateView(generics.ListCreateAPIView):
    transportationRequests = TransportationRoute.objects.all()
    serializer_class = TransportationRouteSerializer
    

