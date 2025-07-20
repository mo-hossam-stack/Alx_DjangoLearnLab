from relationship_app.models import Author, Book, Library, Librarian

author_name = "J.K. Rowling"
try:
    author = Author.objects.get(name=author_name)
    books_by_author = Book.objects.filter(authors=author)
    print(f"Books by {author_name}:")
    for book in books_by_author:
        print(f"- {book.title}")
except Author.DoesNotExist:
    print(f"Author '{author_name}' not found.")

library_name = "Central Library"
try:
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)
    print(f"Librarian at {library_name}: {librarian.name}")
except Library.DoesNotExist:
    print(f"Library '{library_name}' not found.")
except Librarian.DoesNotExist:
    print(f"No librarian assigned to {library_name}.")