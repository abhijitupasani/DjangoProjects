from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
# Create your tests here.

class BookAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        
    def test_get_books(self):
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_create_book(self):
        data = {"title": "Test Book", "author": "Test Author", "published_date": "2023-10-01"}
        response = self.client.post('/api/books/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], "Test Book")
        
    def test_update_book(self):
        test_book = self.client.post('/api/books/', {"title": "Old Book", "author": "Old Author", "published_date": "2023-10-01"}, format='json')
        test_book_id = test_book.data['id']
        response = self.client.put(f'/api/books/{test_book_id}/', {"title": "Updated Book", "author": "Updated Author", "published_date": "2023-10-01"}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Updated Book")
        
    def test_delete_book(self):
        test_book = self.client.post('/api/books/', {"title": "Book to Delete", "author": "Author", "published_date": "2023-10-01"}, format='json')
        test_book_id = test_book.data['id']
        response = self.client.delete(f'/api/books/{test_book_id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
                
        