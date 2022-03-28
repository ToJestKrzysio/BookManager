def test_author_serializer(author_serializer, author_db):
    result = author_serializer.data
    expected = {"id": author_db.id, "name": author_db.name}

    assert result == expected


def test_langauge_serializer(language_serializer, langauge_db):
    result = language_serializer.data
    expected = {"id": langauge_db.id, "name": langauge_db.name}

    assert result == expected


def test_book_serializer(book_serializer, langauge_db, author_db, book_db):
    result = book_serializer.data
    expected = {
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

    assert result == expected
