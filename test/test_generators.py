import pytest
from src.generators import filter_by_currency  # импортируем твою функцию


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
