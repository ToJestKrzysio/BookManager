from django.urls import path
from . import views

app_name = 'books_api'

urlpatterns = [
    path("books", views.BookListAPIView.as_view(), name="book_list_view"),
    path("books/<int:pk>", views.BookRetrieveUpdateDestroyAPIView.as_view(),
         name="book_detail_view"),
]
