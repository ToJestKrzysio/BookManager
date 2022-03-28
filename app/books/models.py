from django.db import models

from . import validators


class Author(models.Model):
    name = models.CharField(max_length=300, unique=True)

    def __str__(self):
        return f"{self.name}"


class Language(models.Model):
    name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.name}"


class Book(models.Model):
    title = models.CharField(max_length=300)
    authors = models.ManyToManyField(Author)
    publication_year = models.PositiveSmallIntegerField(validators=[validators.year_validator],
                                                        blank=False, null=True)
    ISBN = models.CharField(max_length=13, validators=[validators.isbn_validator], unique=True,
                            null=True, blank=False)
    no_pages = models.PositiveSmallIntegerField(null=True, blank=True)
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)
    thumbnail = models.URLField(max_length=300, null=True)

    def __str__(self):
        return f"{self.title}"
