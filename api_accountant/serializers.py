from rest_framework import serializer
import datetime as datetime

from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import serializers

from web_super_admin.models import *
from api_super_admin.models import *

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff 
        fields = "__all__"

class FeeSerializer(serializer.ModelSerializer):
    class Meta:
        model = Fee 
        fields = "__all__"

class NoticeSerializer(serializer.ModelSerializer):
    class Meta:
        model  = Notice 
        fields = "__all__"

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event 
        fields = "__all__"

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message 
        fields = "__all__"

