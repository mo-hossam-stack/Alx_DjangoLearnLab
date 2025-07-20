from relationship_app.models import Library, Book, Author, Librarian

library_name = "Central Library"
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()
for book in books_in_library:
    print(book.title)

author_name = "J.K. Rowling"
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(authors=author)
for book in books_by_author:
    print(book.title)

library = Library.objects.get(name=library_name)
librarian = Librarian.objects.get(library=library)
print(librarian.name)