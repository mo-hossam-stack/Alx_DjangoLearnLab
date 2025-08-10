from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer


# A ListView for retrieving all books (read-only, public)
class ListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# A DetailView for retrieving a single book by ID (read-only, public)
class DetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# A CreateView for adding a new book (authenticated users only)
class CreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Custom behavior: you can add more validations here
        serializer.save()


# An UpdateView for modifying an existing book (authenticated users only)
class UpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        # Custom behavior: additional data checks before saving
        serializer.save()

# A DeleteView for removing a book (authenticated users only)
class DeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]