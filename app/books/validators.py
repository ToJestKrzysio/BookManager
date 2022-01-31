import datetime

from django.core.exceptions import ValidationError


def year_validator(value: int) -> int:
    current_year = datetime.date.today().year
    if value > current_year+1:
        raise ValidationError("Please select a valid year.")
    return value


def isbn_validator(value: int) -> int:
    if len(str(value)) != 13:
        raise ValidationError("Wrong ISBN13 length, should be 13 digits.")
    digit_sum = 0
    for idx, digit in enumerate(str(value), start=1):
        multiplier = 3 if idx % 2 == 0 else 1
        digit_sum += int(digit) * multiplier
    if digit_sum % 10 != 0:
        raise ValidationError("Invalid ISBN13 number.")
    return value
