from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from .models import Book

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/view_books.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    ...

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    ...

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    ...