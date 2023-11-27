from web_super_admin.models import *
from rest_framework import serializers


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'
        
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'
        
class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'
        
class School_blocksSerializer(serializers.ModelSerializer):
    class Meta:
        model = School_blocks
        fields = '__all__'
        
class class_blockSerializer(serializers.ModelSerializer):
    class Meta:
        model = class_block
        fields = '__all__'
        
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        
class class_createSerializer(serializers.ModelSerializer):
    class Meta:
        model = class_create
        fields = '__all__'
        
class FeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fee
        fields = '__all__'
        
class LibraryCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryCategory
        fields = '__all__'
        
class LibraryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryItem
        fields = '__all__'

class TransportationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportationRequest
        fields = "__all__"
        
class LibraryItemCopySerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryItemCopy
        fields = '__all__'
        
class LibraryReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryReservation
        fields = '__all__'
        
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
        
class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = '__all__'
        
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'
        
class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'
        
class ExamResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamResult
        fields = '__all__'
        
class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'
        
class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = '__all__'
        
class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = '__all__'
        
class TransportationRouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportationRoute
        fields = '__all__'
        
class TransportationStopSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportationStop
        fields = '__all__'
        
class TransportationStopOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportationStopOrder
        fields = '__all__'
        
class TransportationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportationRequest
        fields = '__all__'
        
class OpportunitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opportunities
        fields = '__all__'
        
class ELearningSerializer(serializers.ModelSerializer):
    class Meta:
        model = ELearning
        fields = '__all__'
        
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
        
class TimeTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeTable
        fields = '__all__'