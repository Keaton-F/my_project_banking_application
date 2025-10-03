from typing import Any, Dict, List


def filter_by_state(bank_data: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Функция, которая принимает список словарей и строковое значение для ключа state (по умолчанию 'EXECUTED').
    Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state соответствует
    указанному значению."""
    return [i for i in bank_data if i.get("state") == state]


def sort_by_date(date_data: List[Dict[str, Any]], descending: bool = True) -> List[Dict[str, Any]]:
    """Функция, которая принимает список словарей и необязательный параметр, задающий порядок сортировки
    (по умолчанию — убывание). Функция должна возвращать новый список, отсортированный по дате (date)."""
    return sorted(date_data, key=lambda x: x["date"], reverse=descending)
