from relationship_app.models import Library, Book, Author, Librarian
from django.core.exceptions import ObjectDoesNotExist

library_name = "Central Library"
author_name = "J.K. Rowling"

try:
    library = Library.objects.get(name=library_name)
    books_in_library = library.books.all()
    print(f"Books in {library_name}:")
    for book in books_in_library:
        print(book.title)

    librarian = Librarian.objects.get(library=library)
    print(f"Librarian retrieved using get(): {librarian.name}")

except Library.DoesNotExist:
    print(f"Library '{library_name}' not found.")
except Librarian.DoesNotExist:
    print(f"No librarian assigned to '{library_name}'.")

try:
    author = Author.objects.get(name=author_name)
    books_by_author = author.books.all()
    print(f"\nBooks by {author_name}:")
    for book in books_by_author:
        print(book.title)

    filtered_books = Book.objects.filter(author=author)
    print(f"\nFiltered books by {author_name}:")
    for book in filtered_books:
        print(book.title)

except Author.DoesNotExist:
    print(f"Author '{author_name}' not found.")

try:
    library = Library.objects.get(name=library_name)
    print(f"\nLibrarian of {library_name}: {library.librarian.name}")
except (Library.DoesNotExist, Librarian.DoesNotExist):
    print(f"Librarian for '{library_name}' not found.")