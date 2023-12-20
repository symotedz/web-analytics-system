from django.urls import path      
from . import views, books_render_views, books_views, notices_views, Message_views
from . OpportunityView import opportunity_detail, opportunity_list

app_name = 'web_librarian'

urlpatterns = [
    path('', views.index, name='index'),
    
    # url routes for books rendering
    path('book_render_create/', books_render_views.book_render_create, name='book_render_create'),
    path('book_render_update/<int:pk>/', books_render_views.book_render_update, name='book_render_update'),
    path('book_render_delete/<int:pk>/', books_render_views.book_render_delete, name='book_render_delete'),
    path('books_render_delete/', books_render_views.books_render_delete, name='books_render_delete'),
    path('books_render_detail/', books_render_views.books_render_detail, name='books_render_detail'),
    path('book_render_detail/<int:pk>/', books_render_views.book_render_detail, name='book_render_detail'),
    
    #url routes for books creation
    path('Books_create/', books_views.Books_create, name='Books_create'),
    path('Books_Detail/', books_views.Books_Detail, name='Books_Detail'),
    path('Books_delete/', books_views.Books_delete, name='Books_delete'),
    path('Book_Detail/<int:pk>/', books_views.Book_Detail, name='Book_Detail'),
    path('Book_Update/<int:pk>/', books_views.Book_Update, name='Book_Update'),
    path('Book_delete/<int:pk>/', books_views.Book_delete, name='Book_delete'),

    # urls for Message view
    path('Message_create/',  Message_views.Message_create, name='Message_create'),
    path('Messages_detail/',  Message_views.Messages_detail, name='Messages_detail'),
    path('Message_detail/<int:pk>/',  Message_views.Message_detail, name='Message_detail'),
    path('Message_update/<int:pk>/',  Message_views.Message_update, name='Message_update'),
    path('Message_delete/<int:pk>/',  Message_views.Message_delete, name='Message_delete'),
    path('Messages_delete/',  Message_views.Messages_delete, name='Messages_delete'),

    # view urls
    path('notices/', notices_views.Notices, name="Notices"),

    # Ulrs for Opportunity
    path('opportunities/', opportunity_list, name='opportunity_list'),
    path('opportunity/<int:pk>/', opportunity_detail, name='opportunity_detail'),
]
