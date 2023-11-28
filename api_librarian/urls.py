from django.urls import path
from . import views
from . views import LibraryCategoryListCreateView, LibraryCategoryRetrieveUpdateDestroyView
from . views import LibraryItemListCreateView, LibraryItemRetrieveUpdateDestroyView
from . views import LibraryReservationListCreateView, LibraryReservationRetrieveUpdateDestroy
from . views import LibraryItemCopyListCreateView, LibraryItemCopyRetrieveUpdateDestroyView
from . views import StaffListCreateView, StaffRetrieveUpdateDestroyView
from . views import NoticeListCreateView, NoticeRetrieveUpdateDestroyView
from . views import EventListCreateView, EventRetrieveUpdateDestroyView
from . views import StudentListCreateView, StudentRetrieveUpdateDestroyView
from . views import OpportunitiesListCreateView, OpportunitiesRetrieveUpdateDestroyView

app_name = 'api_librarian'

urlpatterns = [
    path('', views.index),

     # urls for library category
    path('librarycategories/', LibraryCategoryListCreateView.as_view(), name='LibraryCategoryListCreateView'),
    path('librarycategory/<int:pk>/', LibraryCategoryRetrieveUpdateDestroyView.as_view(), name="LibraryCategoryRetrieveUpdateDestroyView"),

    # urls for library item
    path('libraryitems/', LibraryItemListCreateView.as_view(), name='LibraryItemListCreateView'),
    path('libraryitem/<int:pk>/', LibraryItemRetrieveUpdateDestroyView.as_view(), name="LibraryItemRetrieveUpdateDestroyView"),

    # urls for library item copy
    path('libraryitemcopies/', LibraryItemCopyListCreateView.as_view(), name='LibraryItemCopyListCreateView'),
    path('libraryitemcopy/', LibraryItemCopyRetrieveUpdateDestroyView.as_view(), name='LibraryItemCopyRetrieveUpdateDestroyView'),

    # urls for library researvation
    path('libraryreservations/', LibraryReservationListCreateView.as_view(), name='LibraryReservationListCreateView'),
    path('libraryresearvation/<int:pk>/', LibraryReservationRetrieveUpdateDestroy.as_view(), name='LibraryReservationRetrieveUpdateDestroy'),

    # urls for staffs
    path('staffs/', StaffListCreateView.as_view(), name='StaffListCreateView'),
    path('staff/<int:pk>/', StaffRetrieveUpdateDestroyView.as_view(), name='StaffRetrieveUpdateDestroyView'),

    #urls for events
    path('events/', EventListCreateView.as_view(), name='EventListCreateView'),
    path('event/<int:pk>/', EventRetrieveUpdateDestroyView.as_view(), name='EventRetrieveUpdateDestroyView'),

    # urls for notices
    path('notice/', NoticeListCreateView.as_view(), name='NoticeListCreateView'),
    path('notice/<int:pk>/', NoticeRetrieveUpdateDestroyView.as_view(), name='NoticeRetrieveUpdateDestroyView'),

    # urls for students
    path('students/', StudentListCreateView.as_view(), name='StudentListCreateView'),
    path('student/<int:pk>/', StudentRetrieveUpdateDestroyView.as_view(), name='StudentRetrieveUpdateDestroyView'),

    # urls for opportunities
    path('opportunities/', OpportunitiesListCreateView.as_view(), name='OpportunitiesListCreateView'),
    path('opportunity/<int:pk>/', OpportunitiesRetrieveUpdateDestroyView.as_view(), name='OpportunitiesRetrieveUpdateDestroyView'),

]
