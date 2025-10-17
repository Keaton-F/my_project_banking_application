import pytest
from src.generators import filter_by_currency, transaction_descriptions


# Примерные тестовые данные
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
    result = list(filter_by_currency(transactions, "USD"))
    assert len(result) == 2
    assert all(t["operationAmount"]["currency"]["code"] == "USD" for t in result)


def test_filter_by_currency_not_found():
    result = list(filter_by_currency(transactions, "GBP"))
    assert result == []


def test_filter_by_currency_empty_list():
    result = list(filter_by_currency([], "USD"))
    assert result == []


def test_transaction_descriptions_basic():
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
    result = list(transaction_descriptions([]))
    assert result == []


