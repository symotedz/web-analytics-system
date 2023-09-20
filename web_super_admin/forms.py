from django.forms import ModelForm
from . models import *

class PlanForm(ModelForm):
    class Meta:
        model = Plan
        fields = '__all__'
        
class StaffForm(ModelForm):
    class Meta:
        model = Staff
        fields = '__all__'
        
class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        
class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
        
class School_blocksForm(ModelForm):
    class Meta:
        model = School_blocks
        fields = '__all__'
        
class Class_blockForm(ModelForm):
    class Meta:
        model = class_block
        fields = '__all__'
        
class FeeForm(ModelForm):
    class Meta:
        model = Fee
        fields = '__all__'
        
class LibraryCategoryForm(ModelForm):
    class Meta:
        models = LibraryCategory
        fields = '__all__'
        
class LibraryItemForm(ModelForm):
    class Meta:
        model =LibraryItem
        fields = '__all__'
        
class LibraryItemCopyForm(ModelForm):
    class Meta:
        model = LibraryItemCopy
        fields = '__all__'
        
class LibraryReservationForm(ModelForm):
    class Meta:
        model = LibraryReservation
        fields = '__all__'
        
class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        
class NoticeForm(ModelForm):
    class Meta:
        model = Notice
        fields = '__all__'
        
        
class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'
        
class ExamForm(ModelForm):
    class Meta:
        model = Exam
        fields = '__all__'
        
class ExamResultForm(ModelForm):
    class Meta:
        model = ExamResult
        fields = '__all__'
        
class AttendanceForm(ModelForm):
    class Meta:
        model = Attendance
        fields = '__all__'
        
class AssignmentForm(ModelForm):
    class Meta:
        model = Assignment
        fields = '__all__'
        
class GradeForm(ModelForm):
    class Meta:
        model = Grade
        fields = '__all__'
        
class TimeTableForm(ModelForm):
    class Meta:
        model = TimeTable
        fields = '__all__'
        
class TransportationRouteForm(ModelForm):
    class Meta:
        model = TransportationRoute
        fields = '__all__'
        
class TransportationStopForm(ModelForm):
    class Meta:
        model = TransportationStop
        fields = '__all__'
        
class TransportationStopOrderForm(ModelForm):
    class Meta:
        model = TransportationStopOrder
        fields = '__all__'
        
class TransportationRequestForm(ModelForm):
    class Meta:
        model = TransportationRequest
        fields = '__all__'
        
class OpportunitiesForm(ModelForm):
    class Meta:
        model = Opportunities
        fields = '__all__'
        
class ELearningForm(ModelForm):
    class Meta:
        model = ELearning
        fields = '__all__'
        
class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = '__all__'