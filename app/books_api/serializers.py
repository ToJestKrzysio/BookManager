from rest_framework import serializers
from books import models


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Author
        fields = ["id", "name"]


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Language
        fields = ["id", "name"]


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True, read_only=True)
    language = serializers.StringRelatedField()

    class Meta:
        model = models.Book
        fields = ["id", "title", "publication_year", "ISBN", "no_pages", "thumbnail", "authors",
                  "language"]
