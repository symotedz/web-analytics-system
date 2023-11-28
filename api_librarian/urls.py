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
    path('', views.index)
]
