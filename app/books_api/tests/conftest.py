import pytest
from django.contrib.auth import get_user_model

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
        title="Test Book", publication_year=2000, ISBN=valid_isbn, no_pages=42, id=1,
        language=langauge_db,
        thumbnail="https://cdn.pixabay.com/photo/2022/01/17/19/59/dog-6945696_960_720.jpg")
    book.authors.add(author_db)
    book.save()
    return book


@pytest.fixture
def book_serializer(book_db):
    return serializers.BookSerializer(instance=book_db)


@pytest.fixture
def book_serializer_return(langauge_db, author_db, book_db):
    return {
        "id": book_db.id,
        "title": book_db.title,
        "publication_year": book_db.publication_year,
        "ISBN": str(book_db.ISBN),
        "no_pages": book_db.no_pages,
        "language": langauge_db.name,
        "thumbnail": book_db.thumbnail,
        "authors": [
            {
                "id": author_db.id,
                "name": author_db.name,
            },
        ]
    }


@pytest.fixture
def user_1(db):
    user_model = get_user_model()
    return user_model.objects.create(username="someUser", email="test@mail.com")


@pytest.fixture
def admin_1(db):
    user_model = get_user_model()
    return user_model.objects.create_superuser(username="someAdmin", email="admin@mail.com")
