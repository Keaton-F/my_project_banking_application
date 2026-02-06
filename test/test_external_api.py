from unittest.mock import Mock, patch

from requests.exceptions import RequestException

from src.external_api import convert_to_rub


def test_convert_to_rub_rub_amount():
    """
    Проверяет, что сумма в RUB возвращается без конвертации.
    """
    transaction = {
        "operationAmount": {"amount": "500", "currency": {"code": "RUB"}}
    }
    assert convert_to_rub(transaction) == 500.0

@patch("src.external_api.requests.get")
def test_convert_to_rub_usd(mock_get):
    """
    Проверяет конвертацию транзакции из USD в RUB через API.
    Проверяет, что API был вызван один раз.
    """
    mock_response = Mock()
    mock_response.json.return_value = {"result": 7500.0}
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    transaction = {
        "operationAmount": {"amount": "100", "currency": {"code": "USD"}}
    }

    result = convert_to_rub(transaction)
    assert result == 7500.0
    mock_get.assert_called_once()


@patch("src.external_api.requests.get")
def test_convert_to_rub_api_error(mock_get):
    """
    Проверяет, что функция возвращает None, если API возвращает ошибку.
    """
    mock_get.side_effect = RequestException("API error")  # <-- вот так
    transaction = {
        "operationAmount": {"amount": "100", "currency": {"code": "USD"}}
    }
    result = convert_to_rub(transaction)
    assert result is None


def test_convert_to_rub_invalid_transaction():
    """
    Проверяет поведение функции при некорректной структуре транзакции – должно вернуть None.
    """
    transaction = {"bad": "data"}
    result = convert_to_rub(transaction)
    assert result is None
