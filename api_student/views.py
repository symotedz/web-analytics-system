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

class ExamResultRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    examResult = ExamResult.objects.all()
    serializer_class = ExamResultSerializer

class NoticeListCreateView(generics.ListCreateAPIView):
    notice = Notice.objects.all()
    serializer_class = NoticeSerializer

class NoticeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    notice = Notice.objects.all()
    serializer_class = NoticeSerializer

class EventListCreateView(generics.ListCreateAPIView):
    event = Event.objects.all()
    serializer_class = EventSerializer

class EventRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    event = Event.objects.all()
    serializer_class = EventSerializer

class StudentListCreateView(generics.ListCreateAPIView):
    student = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializer

class FeeListCreateView(generics.ListCreateAPIView):
    fee = Fee.objects.all()
    serializer_class = FeeSerializer

class FeeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    fee = Fee.objects.all()
    serializer_class = FeeSerializer

class AssignmentListCreateView(generics.ListCreateAPIView):
    assignment = Assignment.objects.all()
    serializer_class = AssignmentSerializer

class AssignmentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    assignment = Assignment.objects.all()
    serializer_class = AssignmentSerializer

class ElearningListCreateView(generics.ListCreateAPIView):
    elearning = ELearning.objects.all()
    serializer_class = ElearningSerializer

class ElearningRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    elearning = ELearning.objects.all()
    serializer_class = ElearningSerializer

class School_blocksListCreateView(generics.ListCreateAPIView):
    schoolblocks = School_blocks.objects.all()
    serializer_class = School_blocksSerializer

class School_blocksRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = School_blocks.objects.all()
    serializer_class = School_blocksSerializer

class ExamListCreateView(generics.ListCreateAPIView):
    exam = Exam.objects.all()
    serializer_class = ExamSerializer

class ExamRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    exam = Exam.objects.all()
    serializer_class = ExamSerializer

class SubjectListCreateView(generics.ListCreateAPIView):
    subject = Subject.objects.all()
    serializer_class = SubjectSerializer

class SubjectRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    subject = Subject.objects.all()
    serializer_class = SubjectSerializer

class TimeTableListCreateView(generics.ListCreateAPIView):
    timetable = TimeTable.objects.all()
    serializer_class = TimeTableSerializer

class TimeTableRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    timetable = TimeTable.objects.all()
    serializer_class = TimeTableSerializer

class TransportationRouteListCreateView(generics.ListCreateAPIView):
    transportationRequests = TransportationRoute.objects.all()
    serializer_class = TransportationRouteSerializer

class TransportationRouteRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    TransportationRequests = TransportationRequest.objects.all()
    serializer_class = TransportationRequestSerializer
    

