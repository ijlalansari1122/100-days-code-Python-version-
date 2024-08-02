from django.urls import path
from .views import BookListCreate, BookDetail, BorrowerListCreate, BorrowerDetail

urlpatterns = [
    path('books/', BookListCreate.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book-detail'),
    path('borrowers/', BorrowerListCreate.as_view(), name='borrower-list-create'),
    path('borrowers/<int:pk>/', BorrowerDetail.as_view(), name='borrower-detail'),
]
