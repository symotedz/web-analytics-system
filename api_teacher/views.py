from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics

from .serializers import *
from web_super_admin.models import *

def index(request):
    return HttpResponse("hello a teacher api")


class TeacherListCreateView(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class class_blockListCreateView(generics.ListCreateAPIView):
    queryset = class_block.objects.all()
    serializer_class = class_blockSerializer

class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

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