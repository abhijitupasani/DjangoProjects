from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from .serializers import BookSerializer
from django.shortcuts import render,redirect, get_object_or_404
from django.http import JsonResponse
from .models import Book, Publisher
from django import forms
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']
        
    
def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'books/book_form.html', {'form': form})
        
def book_update(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'books/book_form.html', {'form': form})

def book_delete(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    else:
        return render(request, 'books/book_confirm_delete.html', {'book': book})
    

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    
    return render(request, 'books/book_form.html', {'form': form})

# def book_list_api(request):
#     books = Book.objects.all().values('id', 'title', 'author', 'published_date')
#     return JsonResponse(list(books), safe=False)

# def book_detail_api(request, id):
#     book = get_object_or_404(Book, id=id)
#     data = {
#         'id': book.id,
#         'title': book.title,
#         'author':book.author,
#         'published_date': book.published_date,
#     }
#     return JsonResponse(data, safe=False)

# @csrf_exempt  # only for testing — not safe for production
# def book_create_api(request):
#     if request.method =='POST':
#         try:
#             data = json.loads(request.body)
            
#             book = Book.objects.create(
#                 title = data.get('title'),
#                 author = data.get('author'),
#                 published_date = data.get('published_date') #YYYY-MM-DD format
#             )
#             return JsonResponse({
#                 "title": book.title,
#                 "author": book.author,
#                 "published_date": book.published_date
#             }, status=201)
#         except json.JSONDecodeError:
#             return JsonResponse({"error": "Invalid JSON"}, status=400)
    
#     return JsonResponse({"error": "Only POST method is allowed"}, status=405)


# @csrf_exempt
# def book_update_api(request, id):
#     if request.method == 'PUT':
#         try:
#             book = Book.objects.get(id=id)
#         except:
#             return JsonResponse({"error": "Book does not exist"}, status=404)
        
#         try:
#             data = json.loads(request.body)
#         except json.JSONDecodeError:
#             return JsonResponse({"error": "Invalid JSON"}, status=400)
        
#         if "title" in data:
#             book.title = data["title"]
#         if "author" in data:
#             book.author = data["author"]
#         if "published_date" in data:
#             book.published_date = data["published_date"]
#         book.save()
        
#         return JsonResponse({
#             "id": book.id,
#             "title": book.title,
#             "author": book.author,
#             "published_date": book.published_date
#         })
        
#     return JsonResponse({"error": "Only PUT method is allowed"}, status=405)

# @csrf_exempt
# def book_delete_api(request, id):
#     if request.method == 'DELETE':
#         try:
#             book = Book.objects.get(id=id)
#         except Book.DoesNotExist:
#             return JsonResponse({"error": "Book does not exist"}, status=404)
        
#         book.delete()
#         return JsonResponse({"message": "Book deleted successfully"}, status=204)
#     return JsonResponse({"error": "Only DELETE method is allowed"}, status=405)    

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Allow read-only access to unauthenticated users
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['author' , 'published_date']
    search_fields = ['title', 'author']
    ordering_fields  = ['published_date','title']
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)