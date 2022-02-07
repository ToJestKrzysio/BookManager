from django.urls import path

from . import views

app_name = "books"
urlpatterns = [
    path("list/", views.BookListView.as_view(), name="book_list"),
    path("create/", views.BookCreateView.as_view(), name="book_create"),
    path("update/<int:pk>", views.BookUpdateView.as_view(), name="book_update"),
    path("delete/<int:pk>", views.BookDeleteView.as_view(), name="book_delete"),
    path("create/author/", views.AuthorCreateView.as_view(), name="author_create"),
    path("update/author/<int:pk>", views.AuthorUpdateView.as_view(), name="author_update"),
    path("create/language/", views.LanguageCreateView.as_view(), name="language_create"),
    path("update/language/<int:pk>", views.LanguageUpdateView.as_view(), name="language_update"),
]
