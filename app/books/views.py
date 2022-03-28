import json
import urllib.request

from django.contrib import messages
from django.core.exceptions import ValidationError
from django.urls import reverse, reverse_lazy
from django.views import generic

from . import forms, helpers, models


class BookListView(generic.ListView):
    queryset = models.Book.objects
    context_object_name = "books"
    paginate_by = 24
    ordering = "title"

    def get_queryset(self):
        filters = {}
        if title := self.request.GET.get("title", ""):
            filters["title__icontains"] = title
        if author := self.request.GET.get("author", ""):
            filters["authors__name__icontains"] = author
        if language := self.request.GET.get("language", ""):
            filters["language__name__icontains"] = language
        if published_after := self.request.GET.get("pub_after", ""):
            filters["publication_year__gt"] = published_after
        if published_after := self.request.GET.get("pub_before", ""):
            filters["publication_year__lt"] = published_after
        queryset = super().get_queryset().prefetch_related("authors", "language").filter(
            **filters).all()
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        filtered_fields = ["title", "author", "language", "pub_after", "pub_before"]
        filtering = ""
        for field in filtered_fields:
            context[field] = self.request.GET.get(field, "")
            filtering += f"&{field}={self.request.GET.get(field, '')}"
        context["filtering"] = filtering
        return context


class BookCreateView(generic.CreateView):
    model = models.Book
    fields = "__all__"
    template_name = "books/book_create.html"
    extra_context = {"page_name": "Add Book"}

    def get_success_url(self):
        messages.success(self.request, f"Book {self.request.POST['title']} added successfully.")
        return reverse("books:book_list")


class BookUpdateView(generic.UpdateView):
    model = models.Book
    fields = "__all__"
    template_name = "books/book_update.html"
    extra_context = {"page_name": "Update Book"}

    def get_success_url(self):
        messages.success(self.request, f"Book {self.request.POST['title']} updated successfully.")
        return reverse_lazy("books:book_list")


class BookDeleteView(generic.DeleteView):
    model = models.Book
    success_url = reverse_lazy("books:book_list")


class BookSearchView(generic.FormView):
    template_name = "books/book_update.html"
    form_class = forms.SearchForm
    extra_context = {"page_name": "Import"}
    success_url = reverse_lazy("books:book_search")

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if not form.is_valid():
            return self.form_invalid(form)

        books_data = helpers.get_books_data(form)
        if not books_data:
            messages.error(request, 'No books matching selected query.')
            return self.form_invalid(form)
        book_objects = []
        for book_data in books_data:
            book_object, created = helpers.create_book(book_data)
            if created:
                book_objects.append(book_object)
        if len(book_objects) > 0:
            messages.success(self.request, f"Successfully imported {len(book_objects)} books.")
        else:
            messages.warning(self.request,
                             f"All books matching query already exist in our database.")
        return super().form_valid(form)


class AuthorCreateView(generic.CreateView):
    model = models.Author
    fields = "__all__"
    template_name = "books/book_create.html"
    extra_context = {"page_name": "Add Author"}

    def get_success_url(self):
        messages.success(self.request, f"Author {self.request.POST['name']} created successfully.")
        return reverse_lazy("books:book_list")


class AuthorUpdateView(generic.UpdateView):
    model = models.Author
    fields = "__all__"
    template_name = "books/book_update.html"
    extra_context = {"page_name": "Update Author"}

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS,
                             f"Author {self.request.POST['name']} updated successfully.")
        return reverse_lazy("books:book_list")


class LanguageCreateView(generic.CreateView):
    model = models.Language
    fields = "__all__"
    template_name = "books/book_create.html"
    extra_context = {"page_name": "Add Language"}

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS,
                             f"Author {self.request.POST['name']} created successfully.")
        return reverse_lazy("books:book_list")


class LanguageUpdateView(generic.UpdateView):
    model = models.Language
    fields = "__all__"
    template_name = "books/book_update.html"
    extra_context = {"page_name": "Update Language"}

    def get_success_url(self):
        messages.success(self.request, f"Author {self.request.POST['name']} updated successfully.")
        return reverse_lazy("books:book_list")
