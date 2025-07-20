from relationship_app.models import Author, Book, Library, Librarian

author = Author.objects.get(name='J.K. Rowling')
books_by_author = Book.objects.filter(authors=author)  
for book in books_by_author:
    print(book.title)

book = Book.objects.get(title="Harry Potter and the Philosopher's Stone")
authors = book.authors.all()
for author in authors:
    print(author.name)

library = Library.objects.get(name='Central Library')
librarian = Librarian.objects.get(library=library)  
print(librarian.name)

library_name = 'Central Library'
library = Library.objects.get(name=library_name)  
books = library.books.all()                     
for book in books:
    print(book.title)
