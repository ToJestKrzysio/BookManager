from rest_framework.generics import ListAPIView
from . import serializers
from books import models


class BookListAPIView(ListAPIView):
    serializer_class = serializers.BookSerializer
    queryset = models.Book.objects.prefetch_related("authors", "language")
