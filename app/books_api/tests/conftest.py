import pytest
from books import models
from books_api import serializers


@pytest.fixture
def author_db(db):
    return models.Author.objects.create(id=1, name="John Doe")


@pytest.fixture
def author_serializer(author_db):
    return serializers.AuthorSerializer(instance=author_db)


@pytest.fixture
def langauge_db(db):
    return models.Language.objects.create(id=1, name="Test Lan")


@pytest.fixture
def language_serializer(langauge_db):
    return serializers.LanguageSerializer(instance=langauge_db)


@pytest.fixture
def valid_isbn():
    return 9787503507762


@pytest.fixture
def book_db(db, langauge_db, author_db, valid_isbn):
    book = models.Book.objects.create(
        title="Test Book", publication_year=2000, ISBN=valid_isbn, no_pages=42,
        language=langauge_db, thumbnail="www.example.com", id=1)
    book.authors.add(author_db)
    book.save()
    return book


@pytest.fixture
def book_serializer(book_db):
    return serializers.BookSerializer(instance=book_db)
