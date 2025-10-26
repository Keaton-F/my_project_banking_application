import os
import requests
from dotenv import load_dotenv
from typing import Optional, Dict

load_dotenv()  # Загрузка переменных окружения

API_URL = os.getenv("API_URL", "https://api.apilayer.com/exchangerates_data/convert")
API_KEY = os.getenv("API_KEY")  # Токен из .env


def convert_to_rub(transaction: Dict) -> Optional[float]:
    """
    Конвертирует сумму транзакции в рубли.

    Если транзакция в USD или EUR, используется внешний API для конвертации.
    Для других валют возвращается исходная сумма (float).

    Args:
        transaction (dict): Словарь с данными транзакции.

    Returns:
        float: Сумма транзакции в рублях, либо None при ошибке.
    """
    try:
        amount = float(transaction["operationAmount"]["amount"])
        currency = transaction["operationAmount"]["currency"]["code"]
    except (KeyError, TypeError, ValueError):
        return None

    if currency == "RUB":
        return amount

    if currency not in ("USD", "EUR"):
        return amount  # Для других валют возвращает без конвертации

    params = {
        "from": currency,
        "to": "RUB",
        "amount": amount
    }
    headers = {
        "apikey": API_KEY
    }

    try:
        response = requests.get(API_URL, headers=headers, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        return float(data.get("result", 0.0))
    except (requests.RequestException, ValueError, TypeError):
        # Любая ошибка при запросе или обработке API
        return None
