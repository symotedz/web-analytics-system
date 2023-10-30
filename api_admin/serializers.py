from rest_framework import serializers

from api_super_admin.serializers import *
from web_super_admin.models import *

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
        model = class_create
        fields = '__all__'
        
class LibraryCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryCategory
        fields = '__all__'
        
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
        model = LibraryReservation
        fields = 'LibraryReservation'
        
class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryReservation
        fields = '__all__'
        
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        models = Subject 
        fields = '__all__' 
        
class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'
        
class ExamResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamResult
        fields = '__all__'
        
class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice 
        fields = '___all__'
        
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
        
        
        

