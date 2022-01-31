import pytest as pytest

from books import models


@pytest.fixture
def db_author_1(db):
    return models.Author.objects.create(name="Test Author")


@pytest.fixture
def db_language_en(db):
    return models.Language.objects.create(name="En")


@pytest.fixture
def valid_isbn():
    return 9787503507762
