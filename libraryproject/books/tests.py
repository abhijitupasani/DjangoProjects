from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Book, Publisher
# Create your tests here.

class BookAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='123')
        self.publisher = Publisher.objects.create(name="Bloomsbury")
        self.client.login(username='testuser', password='123')
        self.book_data = {
            "title": "Harry Potter and the Philosopher's Stone",
            "author": "J.K. Rowling",
            "published_date": "2000-07-08",
            "publisher_id": self.publisher.id
        }

    def test_create_book(self):
        response = self.client.post("/api/books/", self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('id', response.data)

    def test_update_book(self):
        create_response = self.client.post("/api/books/", self.book_data, format='json')
        book_id = create_response.data['id']
        updated_data = self.book_data.copy()
        updated_data['title'] = "Harry Potter and the Chamber of Secrets"
        response = self.client.put(f"/api/books/{book_id}/", updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], updated_data['title'])

    def test_delete_book(self):
        create_response = self.client.post("/api/books/", self.book_data, format='json')
        book_id = create_response.data['id']
        response = self.client.delete(f"/api/books/{book_id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_list_books(self):
        self.client.post("/api/books/", self.book_data, format='json')
        response = self.client.get("/api/books/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)