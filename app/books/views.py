from django.views import generic

from . import models


class BookListView(generic.ListView):
    queryset = models.Book.objects.select_related().all()
    context_object_name = "books"
