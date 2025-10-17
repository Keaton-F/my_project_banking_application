from typing import Dict, Generator, List


def filter_by_currency(transactions: List[Dict], currency: str) -> Generator[Dict, None, None]:
    """
    Принимает список транзакций и возвращает итератор,
    который выдаёт только те, у которых код валюты совпадает с заданным.
    """
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield transaction


def transaction_descriptions(sample_transactions: List[Dict[str, str]]) -> Generator[str, None, None]:
    """
    Генератор, возвращающий описание каждой транзакции из списка.
    """
    for transaction in sample_transactions:
        description = transaction.get("description")
        if description is not None:
            yield description


def card_number_generator(start: int, end: int) -> Generator[str, None, None]:
    """
    Генератор, выдающий номера банковских карт
    в формате 'XXXX XXXX XXXX XXXX' от start до end включительно.
    """
    for number in range(start, end + 1):
        # Преобразуем число в строку длиной 16 символов с ведущими нулями
        formatted = f"{number:016}"
        # Разбиваем на группы по 4 символа
        yield " ".join([formatted[i : i + 4] for i in range(0, 16, 4)])
