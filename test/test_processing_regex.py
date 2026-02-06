import pytest

from src.processing import process_bank_operations, process_bank_search


@pytest.fixture
def sample_data():
    return [
        {"description": "Оплата услуг", "amount": 100},
        {"description": "Перевод на карту", "amount": 200},
        {"description": "Открытие вклада", "amount": 300},
        {"description": "Оплата мобильной связи", "amount": 150},
    ]


def test_process_bank_search_found(sample_data):
    result = process_bank_search(sample_data, "оплата")
    assert len(result) == 2
    assert all("оплата" in item["description"].lower() for item in result)


def test_process_bank_search_not_found(sample_data):
    result = process_bank_search(sample_data, "что")
    assert result == []


def test_process_bank_operations(sample_data):
    categories = ["Оплата", "Перевод", "Вклад"]
    result = process_bank_operations(sample_data, categories)

    assert result == {
        "Оплата": 2,
        "Перевод": 1,
        "Вклад": 1,
    }
