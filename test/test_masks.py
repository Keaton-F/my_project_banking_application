import pytest

from src.masks import get_mask_account, get_mask_card_number


# get_mask_card_number
@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("1234567890123456", "1234 56** **** 3456"),
        ("1234 5678 9012 3456", "1234 56** **** 3456"),
        ("12345678901234567890", "Номер не может содержать лишние символы."),
        ("", "Данный параметр не может быть пустым."),
        ("123", "Не верный формат ввода."),
        ("abcd1234", "Номер допускает для ввода только цифры."),
    ],
)
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected


# get_mask_account
@pytest.mark.parametrize(
    "account, expected",
    [
        ("40817810099910004312", "**4312"),
        ("12345678", "**5678"),
        ("", "Данный параметр не может быть пустым."),
        ("123", "Номер не может быть короче 6-ти символов."),
        ("abcd1234", "Номер не может содержать лишние символы."),
    ],
)
def test_get_mask_account(account, expected):
    assert get_mask_account(account) == expected
