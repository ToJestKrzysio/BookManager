from . import models


def get_isbn(isbn_list: list[dict]) -> str | None:
    isbn = {}
    for value in isbn_list:
        type_ = value.get("type")
        identifier = value.get("identifier")
        if type_ and identifier:
            isbn[type_] = identifier
    return isbn.get("ISBN_13", None) or isbn.get("ISBN_10", None)


def create_book(book: dict):
    volume_info = book.get("volumeInfo", {})
    title = volume_info.get("title")
    authors = volume_info.get("authors", [])
    language = volume_info.get("language")
    thumbnail = volume_info.get("imageLinks", {}).get("smallThumbnail", None)
    page_count = volume_info.get("pageCount", None)
    published_date = volume_info.get("publishedDate", None)
    published_date = published_date.split("-")[0] if published_date else None
    isbn_list = volume_info.get("industryIdentifiers", [])
    isbn = get_isbn(isbn_list)
    language_object, _ = models.Language.objects.get_or_create(name=language)
    book_object, created = models.Book.objects.get_or_create(
        title=title,
        language=language_object,
        thumbnail=thumbnail,
        no_pages=page_count,
        ISBN=isbn,
        publication_year=published_date
    )
    for author in authors:
        author_object, _ = models.Author.objects.get_or_create(name=author)
        book_object.authors.add(author_object)
    book_object.save()
    return book_object, created
