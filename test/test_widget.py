import pytest

from src.widget import get_date, mask_account_card


# mask_account_card
@pytest.mark.parametrize(
    "data, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счёт **4305"),
        ("Счет 7000792289606361", "Счёт **6361"),
        ("", "Данный параметр не может быть пустым."),
        ("123", "Некорректный ввод: тип данных не является номером карты или номером счёта."),  # нераспознанный тип
    ],
)
def test_mask_account_card(data, expected):
    assert mask_account_card(data) == expected


# get_date
@pytest.mark.parametrize(
    "date_str, expected",
    [
        ("2022-05-01T14:30.078459", "01.05.2022"),
        ("2021-12-31T23:59:59", "31.12.2021"),
        ("2022-09-08", "08.09.2022"),
        ("9999-99-99T99:99:99", "Ошибка данных: значение не является датой, или имеет неверный формат."),
        ("", None),
        ("invalid-date", "Ошибка данных: значение не является датой, или имеет неверный формат."),
    ],
)
def test_get_date(date_str, expected):
    assert get_date(date_str) == expected
