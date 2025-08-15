from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

# urlpatterns = [
#     path('', views.book_list, name='book_list'),
#     path('add/', views.add_book, name='book_create'),
#     path('edit/<int:pk>/', views.book_update, name='book_update'),
#     path('delete/<int:pk>/', views.book_delete, name='book_delete'),
#     path('api/books/', views.book_list_api, name='book_list_api'),
#     path('api/books/<int:id>/', views.book_detail_api, name='book_detail_api'),
#     path('api/books/create/', views.book_create_api, name='book_create_api'),
#     path('api/books/<int:id>/update/', views.book_update_api, name='book_update_api'),
#     path('api/books/<int:id>/delete/', views.book_delete_api, name='book_delete_api'),

# ]

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
