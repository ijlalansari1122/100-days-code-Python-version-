from django.shortcuts import render

from rest_framework import generics
from .models import Book, Borrower
from .serializers import BookSerializer, BorrowerSerializer

class BookListCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BorrowerListCreate(generics.ListCreateAPIView):
    queryset = Borrower.objects.all()
    serializer_class = BorrowerSerializer

class BorrowerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Borrower.objects.all()
    serializer_class = BorrowerSerializer
