import pytest as pytest
from django.urls import reverse

from books import models


@pytest.fixture
def db_author_1(db):
    return models.Author.objects.create(name="Test Author", id=1)


@pytest.fixture
def db_language_en(db):
    return models.Language.objects.create(name="En")


@pytest.fixture
def valid_isbn():
    return 9787503507762


@pytest.fixture
def db_book_1(db, db_author_1, db_language_en, valid_isbn):
    return models.Book.objects.create(
        title="Test Book", publication_year=2000, ISBN=valid_isbn, no_pages=42,
        language=db_language_en, address="www.example.com", id=1
    )


@pytest.fixture
def book_list_response(client, db):
    url = reverse("books:book_list")
    return client.get(url)


@pytest.fixture
def posted_data(db_author_1, db_language_en, valid_isbn):
    return {"authors": [1], "language": 1, "title": "Some Book",
            "address": "www.TheExample.com", "no_pages": 42, "ISBN": valid_isbn,
            "publication_year": 2010}
