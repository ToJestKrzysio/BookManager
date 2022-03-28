def test_author_serializer(author_serializer, author_db):
    result = author_serializer.data
    expected = {"id": author_db.id, "name": author_db.name}

    assert result == expected


def test_langauge_serializer(language_serializer, langauge_db):
    result = language_serializer.data
    expected = {"id": langauge_db.id, "name": langauge_db.name}

    assert result == expected


def test_book_serializer(book_serializer, book_serializer_return):
    assert book_serializer.data == book_serializer_return
