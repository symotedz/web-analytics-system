from django.shortcuts import render
from django.http import HttpResponse

from web_super_admin.models import *
from rest_framework import generics
from .serializers import *
# Create your views here.
def index(request):
    return HttpResponse("Hello,World")

class LibraryCategoryListCreateView(generics.ListCreateAPIView):
    libraryCategory = LibraryCategory.objects.all()
    serializer_class = LibraryCategorySerializer

class  LibraryItemListCreateView(generics.ListCreateAPIView):
    libraryItem =  LibraryItem.objects.all()
    serializer_class =  LibraryItemSerializer

class  LibraryReservationListCreateView(generics.ListCreateAPIView):
    libraryReservation =  LibraryReservation.objects.all()
    serializer_class =  LibraryReservationSerializer

class StaffListCreateView(generics.ListCreateAPIView):
    staffs =  Staff.objects.all()
    serializer_class = StaffSerializer

class NoticeListCreateView(generics.ListCreateAPIView):
    notices = Notice.objects.all()
    serializer_class = NoticeSerializer

class EventListCreateView(generics.ListCreateAPIView):
    notices  = Event.objects.all()
    serializer_class = EventSerializer

class StudentListCreateView(generics.ListCreateAPIView):
    students = Student.objects.all()
    serializer_class = StudentSerializer

class OpportunitiesListCreateView(generics.ListCreateAPIView):
    opportunities = Opportunities.objects.all()
    serializer_class = OpportunitiesSerializer
