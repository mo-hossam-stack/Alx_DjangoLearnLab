# relationship_app/query_samples.py

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

author_name = "J.K. Rowling"
try:
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    print(f"\n Books by {author_name}:")
    for book in books:
        print(f"- {book.title}")
except Author.DoesNotExist:
    print(f"\n Author '{author_name}' not found.")

library_name = "Central Library"
try:
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    print(f"\n Books in {library_name}:")
    for book in books:
        print(f"- {book.title}")
except Library.DoesNotExist:
    print(f"\n Library '{library_name}' not found.")

try:
    librarian = Librarian.objects.get(library__name=library_name)
    print(f"\n👨‍💼 Librarian of {library_name}: {librarian.name}")
except Librarian.DoesNotExist:
    print(f"\n No librarian assigned to {library_name}.")
