from django.views import generic

from . import models


class BookListView(generic.ListView):
    queryset = models.Book.objects.select_related()
    context_object_name = "books"
    paginate_by = 1
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
            filters["publication_year__year__gt"] = published_after
        if published_after := self.request.GET.get("pub_before", ""):
            filters["publication_year__year__lt"] = published_after
        queryset = super().get_queryset().filter(**filters)
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
