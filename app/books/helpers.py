def get_isbn13(isbn_list: list[dict]) -> int:
    for isbn in isbn_list:
        isbn_13 = isbn.get("ISBN_13", None)
        if isbn_13:
            return isbn_13
    return -1
