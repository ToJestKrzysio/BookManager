def get_isbn(isbn_list: list[dict]) -> str | None:
    isbn = {}
    for value in isbn_list:
        type_ = value.get("type")
        identifier = value.get("identifier")
        if type_ and identifier:
            isbn[type_] = identifier
    return isbn.get("ISBN_13", None) or isbn.get("ISBN_10", None)
