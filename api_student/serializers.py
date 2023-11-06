from web_super_admin.models import *
from rest_framework import serializers

class ExamResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamResult
        fields = '__all__'

class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice 
        fields = "__all__"

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event 
        fields = "__all__"

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student 
        fields = "__all__"
        

