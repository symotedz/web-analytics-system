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

class FeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fee 
        fields = "__all__"

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = "__all__"

class ElearningSerializer(serializers.ModelSerializer):
    class Meta:
        model = ELearning
        fields = "__all__"

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject 
        fields = "__all__"

