import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


transactions = [
    {
        "id": 1,
        "operationAmount": {
            "amount": "100.00",
            "currency": {"name": "USD", "code": "USD"}
        },
    },
    {
        "id": 2,
        "operationAmount": {
            "amount": "200.00",
            "currency": {"name": "EUR", "code": "EUR"}
        },
    },
    {
        "id": 3,
        "operationAmount": {
            "amount": "300.00",
            "currency": {"name": "USD", "code": "USD"}
        },
    },
]

def test_filter_by_currency_usd():
    """Проверяет, что функция корректно фильтрует транзакции по валюте USD."""
    result = list(filter_by_currency(transactions, "USD"))
    assert len(result) == 2
    assert all(t["operationAmount"]["currency"]["code"] == "USD" for t in result)


def test_filter_by_currency_not_found():
    """Проверяет, что при отсутствии транзакций с заданной валютой возвращается пустой список."""
    result = list(filter_by_currency(transactions, "GBP"))
    assert result == []


def test_filter_by_currency_empty_list():
    """Проверяет, что функция корректно обрабатывает пустой список транзакций."""
    result = list(filter_by_currency([], "USD"))
    assert result == []


def test_transaction_descriptions_basic():
    """Проверяет, что генератор возвращает корректные описания всех транзакций."""
    sample_transactions = [
        {"description": "Перевод организации"},
        {"description": "Перевод со счета на счет"},
        {"description": "Перевод с карты на карту"},
    ]
    result = list(transaction_descriptions(sample_transactions))
    assert result == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
    ]


def test_transaction_descriptions_empty_list():
    """Проверяет, что генератор корректно обрабатывает пустой список транзакций."""
    result = list(transaction_descriptions([]))
    assert result == []


@pytest.mark.parametrize(
    "start, end, expected",
    [
        (
            1,
            3,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
            ],
        ),
        (
            9999999999999997,
            9999999999999999,
            [
                "9999 9999 9999 9997",
                "9999 9999 9999 9998",
                "9999 9999 9999 9999",
            ],
        ),
    ],
)
def test_card_number_generator_parametrized(start, end, expected):
    """Проверяет, что генератор выдаёт корректные номера карт для заданного диапазона."""
    result = list(card_number_generator(start, end))
    assert result == expected


@pytest.fixture
def small_range():
    """Возвращает диапазон для проверки форматирования номеров."""
    return list(card_number_generator(10, 12))


def test_card_number_format(small_range):
    """Проверяет корректность форматирования номеров (4 группы по 4 цифры)."""
    for card in small_range:
        parts = card.split(" ")
        assert len(parts) == 4
        assert all(len(p) == 4 for p in parts)
        assert card.replace(" ", "").isdigit()


def test_card_number_generator_empty_range():
    """Проверяет, что при start > end генератор ничего не возвращает."""
    result = list(card_number_generator(5, 1))
    assert result == []
