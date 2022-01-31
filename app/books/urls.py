from django.urls import path

from . import views

app_name = "books"
urlpatterns = [
    path("list/", views.BookListView.as_view(), name="book_list"),
    path("create/", views.BookCreateView.as_view(), name="book_create"),
    path("update/<int:pk>", views.BookUpdateView.as_view(), name="book_update"),
]
