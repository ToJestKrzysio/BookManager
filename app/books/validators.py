import datetime

from django.core.exceptions import ValidationError


def year_validator(value: int) -> int:
    current_year = datetime.date.today().year
    if value > current_year + 1:
        raise ValidationError("Please select a valid year.")
    return value


def isbn_validator(value: str | None) -> str | None:
    if value is None:
        return None
    if len(value) == 13:
        return validate_isbn_13(value)
    if len(value) == 10:
        return validate_isbn_10(value)
    raise ValidationError("Wrong length of ISBN, valid length is 10 or 13.")


def validate_isbn_13(value: str) -> str:
    digit_sum = 0
    for idx, digit in enumerate(value, start=1):
        multiplier = 3 if idx % 2 == 0 else 1
        digit_sum += int(digit) * multiplier
    if digit_sum % 10 != 0:
        raise ValidationError("Invalid ISBN13 number.")
    return value


def validate_isbn_10(value: str) -> str:
    return value


def validate_numeric(value: str) -> str:
    if value.isnumeric():
        return value
    raise ValidationError("ISBN should be numeric only.")
