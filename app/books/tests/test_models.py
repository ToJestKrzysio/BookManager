import pytest
from django.core import exceptions

from books import models


class TestBook:

    @pytest.mark.parametrize("year", [2030, 9999, 12000])
    def test_publication_year_in_future(self, year, db_author_1, db_language_en, valid_isbn):
        with pytest.raises(exceptions.ValidationError) as exception:
            book = models.Book.objects.create(
                title="Test Book", publication_year=year, ISBN=valid_isbn, no_pages=242,
                language=db_language_en, address="www.example.com"
            )
            book.full_clean()
        assert "Please select a valid year." in str(exception.value)

    @pytest.mark.parametrize("isbn", [int("1" * len_) for len_ in range(1, 20) if len_ != 13])
    def test_isbn_wrong_length(self, db_author_1, db_language_en, isbn):
        with pytest.raises(exceptions.ValidationError) as exception:
            book = models.Book.objects.create(
                title="Test Book", publication_year=2000, ISBN=isbn, no_pages=242,
                language=db_language_en, address="www.example.com"
            )
            book.full_clean()
        assert "Wrong ISBN13 length, should be 13 digits." in str(exception.value)

    @pytest.mark.parametrize("isbn", [1231231231231, 1234567890123])
    def test_isbn_wrong_value(self, db_author_1, db_language_en, isbn):
        with pytest.raises(exceptions.ValidationError) as exception:
            book = models.Book.objects.create(
                title="Test Book", publication_year=2000, ISBN=isbn, no_pages=242,
                language=db_language_en, address="www.example.com"
            )
            book.full_clean()
        assert "Invalid ISBN13 number." in str(exception.value)
