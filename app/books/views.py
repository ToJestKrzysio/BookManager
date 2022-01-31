from django.contrib import messages
from django.urls import reverse
from django.views import generic

from . import models


class BookListView(generic.ListView):
    queryset = models.Book.objects
    context_object_name = "books"
    paginate_by = 2
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
        queryset = super().get_queryset().filter(**filters).all()
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

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS,
                             f"Book {self.request.POST['title']} added successfully.")
        return reverse("books:book_list")


class BookUpdateView(generic.UpdateView):
    model = models.Book
    fields = "__all__"
    template_name = "books/book_update.html"

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS,
                             f"Book {self.request.POST['title']} added successfully.")
        return reverse("books:update_book", kwargs={"pk": self.object.pk})
