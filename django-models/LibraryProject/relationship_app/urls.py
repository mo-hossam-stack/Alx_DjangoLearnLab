from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import admin_view, librarian_view, member_view, add_book_view, edit_book_view, delete_book_view

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('librarian-role/', librarian_view, name='librarian_view'),
    path('member-role/', member_view, name='member_view'),
    path('add_book/', add_book_view, name='add_book'),
    path('edit_book/<int:book_id>/', edit_book_view, name='edit_book'),
    path('delete_book/<int:book_id>/', delete_book_view, name='delete_book'),
]
