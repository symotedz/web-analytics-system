from django.urls import path
from . import views
from . views import *

app_name = 'api_admin'

urlpatterns = [
    path('', views.index),
    path('plan/', PlanListCreateView.as_view(), name="PlanListCreateView"),
    path('teacher/', TeacherListCreateView.as_view(), name='TeacherListCreateView'),
    path('staff/', StaffListCreateView.as_view(), name='StaffListCreateView'),
    path('school_block/', School_blocksListCreateView.as_view(), name='School_blocksListCreateView'),
    path('class_block/', class_blockListCreateView.as_view(), name='class_blockListCreateView'),
    path('student/', StudentListCreateView.as_view(), name='StudentListCreateView'),
    path('class_create/', class_createListCreateView.as_view(), name='class_createListCreateView'),
    path('fee/', FeeListCreateView.as_view(), name='FeeListCreateView'),
    path('librarycategory/', LibraryCategoryListCreateView.as_view(), name='LibraryCategoryListCreateView'),
]
