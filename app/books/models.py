from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.name}"


class Language(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name}"


class Book(models.Model):
    title = models.CharField(max_length=300)
    authors = models.ManyToManyField(Author)
    publication_year = models.DateField()
    ISBN = models.IntegerField()
    no_pages = models.IntegerField()
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.title}"
