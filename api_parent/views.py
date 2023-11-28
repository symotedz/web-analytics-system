from datetime import datetime
import io
import csv

from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import generics

from web_super_admin.models import *
from .serializers import *

# Create your views here.
def index(request):
    return HttpResponse("Hello,World")

class StudentListCreateView(generics.ListCreateAPIView):
    student = Student.objects.all()
    serializer_class = StudentSerializer

class NoticeListCreateView(generics.ListCreateAPIView):
    notice = Notice.objects.all()
    serializer_class = NoticeSerializer

class EventListCreateView(generics.ListCreateAPIView):
    event = Event.objects.all()
    serializer_class = EventSerializer

class ExamResultListCreateView(generics.ListCreateAPIView):
    examResult = ExamResult.objects.all()
    serializer_class = ExamResultSerializer

class AssignmentListCreateView(generics.ListCreateAPIView):
    assignment = Assignment.objects.all()
    serializer_class = AssignmentSerializer

class SubjectListCreateView(generics.ListCreateAPIView):
    subject = Subject.objects.all()
    serializer_class = SubjectSerializer

class FeeListCreateView(generics.ListCreateAPIView):
    fee = Fee.objects.all()
    serializer_class = FeeSerializer

class class_blockListCreateView(generics.ListCreateAPIView):
    classblocks = class_block.objects.all()
    serializer_class = class_blockSerializer

class AttendanceListCreateView(generics.ListCreateAPIView):
    attendance = Attendance.objects.all()
    serializer_class = AttendanceSerializer

class School_blocksListCreateView(generics.ListCreateAPIView):
    school_blocks = School_blocks.objects.all()
    serializer_class = School_blocksSerializer 

class TransportationRequestListCreateView(generics.ListCreateAPIView):
    transporationRequest = TransportationRequest.objects.all()
    serializer_class = TransportationRequestSerializer







