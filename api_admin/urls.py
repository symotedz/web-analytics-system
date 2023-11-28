from django.urls import path
from . import views
from . views import PlanListCreateView, PlanRetrieveUpdateDestroyView, TeacherListCreateView, TeacherRetrieveUpdateDestroyView
from . views import StaffListCreateView, StaffRetrieveUpdateDestroyView, School_blocksListCreateView, School_blockRetrieveUpdateDestroy
from . views import class_blockListCreateView, class_blockRetrieveUpdateDestroyView, StudentListCreateView, StudentRetrieveUpdateDestroyView
from . views import class_createListCreateView, class_createRetrieveUpdateDestroyView, FeeListCreateView, FeeRetrieveUpdateDestroyView
from . views import LibraryCategoryListCreateView, LibraryCategoryRetrieveUpdateDestroyView

app_name = 'api_admin'

urlpatterns = [
    path('', views.index),

    # urls for plans
    path('plans/', PlanListCreateView.as_view(), name="PlanListCreateView"),
    path('plan/<int:pk>/', PlanRetrieveUpdateDestroyView.as_view(), name="plan"),

    # urls for teacher api endpoint
    path('teachers/', TeacherListCreateView.as_view(), name='TeacherListCreateView'),
    path("teacher/<int:pk>/", TeacherRetrieveUpdateDestroyView.as_view(), name="teacher"),

    # urls for staffs
    path('staffs/', StaffListCreateView.as_view(), name='StaffListCreateView'),
    path('staff/<int:pk>/', StaffRetrieveUpdateDestroyView.as_view(), name="staff"),

    # urls for school blocks
    path('school_blocks/', School_blocksListCreateView.as_view(), name='School_blocksListCreateView'),
    path("school_block/<int:pk>/", School_blockRetrieveUpdateDestroy.as_view(), name="school_block"),

    # urls for class blocks
    path('class_blocks/', class_blockListCreateView.as_view(), name='class_blockListCreateView'),
    path('school_block/<int:pk>/', class_blockRetrieveUpdateDestroyView.as_view(), name="school_block"),

    # urls for student
    path('students/', StudentListCreateView.as_view(), name='StudentListCreateView'),
    path('student/<int:pk>/', StudentRetrieveUpdateDestroyView.as_view(), name="student"),

    # urls for class create
    path('class_creates/', class_createListCreateView.as_view(), name='class_createListCreateView'),
    path("class_create/<int:pk>/", class_createRetrieveUpdateDestroyView.as_view(), name="class_create"),

    # urls for fee
    path('fees/', FeeListCreateView.as_view(), name='FeeListCreateView'),
    path("fee/int:pk>/", FeeRetrieveUpdateDestroyView.as_view(), name="fee"),

    # urls for library category
    path('librarycategories/', LibraryCategoryListCreateView.as_view(), name='LibraryCategoryListCreateView'),
    path("librarycategory/<int:pk>/", LibraryCategoryRetrieveUpdateDestroyView.as_view(), name="librarycategory"),
]
