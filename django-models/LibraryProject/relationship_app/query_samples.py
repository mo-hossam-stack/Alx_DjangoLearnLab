from relationship_app.models import Author, Book, Library, Librarian

try:
    author = Author.objects.get(name='J.K. Rowling')
    books_by_author = Book.objects.filter(authors=author)
    print(f"Books by {author.name}: {[book.title for book in books_by_author]}")
except Author.DoesNotExist:
    print("Author 'J.K. Rowling' not found.")

try:
    book = Book.objects.get(title="Harry Potter and the Philosopher's Stone")
    authors = book.authors.all()
    print(f"Authors of {book.title}: {[author.name for author in authors]}")
except Book.DoesNotExist:
    print("Book 'Harry Potter and the Philosopher's Stone' not found.")

try:
    library = Library.objects.get(name='Central Library')
    librarian = Librarian.objects.get(library=library)
    print(f"Librarian for {library.name}: {librarian.name}")
except Library.DoesNotExist:
    print("Library 'Central Library' not found.")
except Librarian.DoesNotExist:
    print("No librarian assigned to Central Library.")

# List all books in a library
try:
    library_name = 'Central Library'
    library = Library.objects.get(name=library_name)
    books = library.books.all() 
    print(f"Books in {library.name}: {[book.title for book in books]}")
except Library.DoesNotExist:
    print(f"Library '{library_name}' not found.")
