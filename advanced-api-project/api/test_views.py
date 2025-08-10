from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate

from .models import Book
from .views import ListView, DetailView, CreateView, UpdateView, DeleteView


class BookAPITests(APITestCase):
    def setUp(self):
        # Create test users
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.other_user = User.objects.create_user(username="otheruser", password="otherpass")

        # Create sample books
        self.book1 = Book.objects.create(title="Book One", author="Author A", publication_year=2000)
        self.book2 = Book.objects.create(title="Book Two", author="Author B", publication_year=2010)

        # Initialize APIRequestFactory
        self.factory = APIRequestFactory()

    def test_list_books(self):
        """Test retrieving all books"""
        request = self.factory.get(reverse("book-list"))
        force_authenticate(request, user=self.user)
        response = ListView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_single_book(self):
        """Test retrieving a single book by ID"""
        request = self.factory.get(reverse("book-detail", kwargs={"pk": self.book1.pk}))
        force_authenticate(request, user=self.user)
        response = DetailView.as_view()(request, pk=self.book1.pk)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["title"], self.book1.title)

    def test_create_book(self):
        """Test creating a new book"""
        data = {"title": "New Book", "author": "New Author", "publication_year": 2023}
        request = self.factory.post(reverse("book-list"), data, format="json")
        force_authenticate(request, user=self.user)
        response = CreateView.as_view()(request)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Book.objects.count(), 3)

    def test_update_book(self):
        """Test updating an existing book"""
        data = {"title": "Updated Title", "author": "Author A", "publication_year": 2001}
        request = self.factory.put(reverse("book-detail", kwargs={"pk": self.book1.pk}), data, format="json")
        force_authenticate(request, user=self.user)
        response = UpdateView.as_view()(request, pk=self.book1.pk)
        self.assertEqual(response.status_code, 200)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Title")

    def test_delete_book(self):
        """Test deleting a book"""
        request = self.factory.delete(reverse("book-detail", kwargs={"pk": self.book1.pk}))
        force_authenticate(request, user=self.user)
        response = DeleteView.as_view()(request, pk=self.book1.pk)
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Book.objects.filter(pk=self.book1.pk).exists())

    def test_filter_books_by_author(self):
        """Test filtering books by author"""
        request = self.factory.get(reverse("book-list") + "?author=Author A")
        force_authenticate(request, user=self.user)
        response = ListView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(all(b["author"] == "Author A" for b in response.data))

    def test_search_books_by_title(self):
        """Test searching books by title"""
        request = self.factory.get(reverse("book-list") + "?search=Book One")
        force_authenticate(request, user=self.user)
        response = ListView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(any("Book One" in b["title"] for b in response.data))

    def test_order_books_by_year(self):
        """Test ordering books by publication year descending"""
        request = self.factory.get(reverse("book-list") + "?ordering=-publication_year")
        force_authenticate(request, user=self.user)
        response = ListView.as_view()(request)
        years = [b["publication_year"] for b in response.data]
        self.assertEqual(years, sorted(years, reverse=True))