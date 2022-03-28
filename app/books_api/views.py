from rest_framework import generics
from . import serializers
from books import models


class BookListAPIView(generics.ListAPIView):
    serializer_class = serializers.BookSerializer
    queryset = models.Book.objects.prefetch_related("authors", "language")


class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.BookSerializer
    queryset = models.Book.objects.prefetch_related("authors", "language")
