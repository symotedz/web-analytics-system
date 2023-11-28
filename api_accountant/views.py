from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import generics


from web_super_admin.models import *
from . serializers import *

# Create your views here.
def index(request):
    return HttpResponse("Hello, World")

class StaffListCreateView(generics.ListCreateAPIView):
    staffs = Staff.objects.all()
    serializer_class = StaffSerializer

class StaffRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    staffs = Staff.objects.all()
    serializer_class = StaffSerializer

class FeeListCreateView(generics.ListCreateAPIView):
    fee = Fee.objects.all()
    serializer_class = FeeSerializer

class FeeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    fee = Fee.objects.all()
    serializer_class = FeeSerializer
class NoticeListCreateView(generics.ListCreateAPIView):
    notice = Notice.objects.all()
    serializer_class = NoticeSerializer

class NoticeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    notice = Notice.objects.all()
    serializer_class = NoticeSerializer

class EventListCreateView(generics.ListCreateAPIView):
    Event = Event.objects.all()
    serializer_class = EventSerializer

class EventRetrieveUpdateDestroyUpdateView(generics.RetrieveUpdateDestroyAPIView):
    event = Event.objects.all()
    serializer_class = EventSerializer

class MessageListCreateView(generics.ListCreateAPIView):
    messages = Message.objects.all()
    serializer_class = MessageSerializer

class MessageRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    messages = Message.objects.all()
    serializer_class = MessageSerializer




