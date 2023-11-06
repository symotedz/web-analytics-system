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

class School_blocksSerializer(serializers.ModelSerializer):
    class Meta:
        model = School_blocks
        fields = "__all__"

class class_blockSerializer(serializers.ModelSerializer):
    class Meta:
        model = class_block
        fields = "__all__"

class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam 
        fields = "__all__"

class TimeTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeTable 
        fields = "__all__"

class TransportationRouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportationRoute
        fields = "__all__"
    
class TransportationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportationRequest
        fields = "__all__"

