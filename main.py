from typing import List, Dict, Any

from src.processing import (
    filter_by_state,
    sort_by_date,
    process_bank_search,
)
from src.readers import read_transactions_from_csv, read_transactions_from_excel
import json


def read_transactions_from_json(path: str) -> List[Dict[str, Any]]:
    """Считывает транзакции из JSON-файла."""
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if isinstance(data, list):
        return data

    if isinstance(data, dict) and "transactions" in data:
        return data["transactions"]

    return []


def print_transaction(transaction: Dict[str, Any]) -> None:
    """Красивый вывод транзакции."""
    date = transaction.get("date", "")[:10]
    description = transaction.get("description", "")
    from_acc = transaction.get("from", "Неизвестно")
    to_acc = transaction.get("to", "Неизвестно")
    amount_info = transaction.get("operationAmount", {})

    amount = amount_info.get("amount", "")
    currency = amount_info.get("currency", {}).get("name", "")

    print(f"{date} {description}")
    print(f"{from_acc} -> {to_acc}")
    print(f"Сумма: {amount} {currency}\n")


def select_file() -> List[Dict[str, Any]]:
    """Меню выбора источника данных."""
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    while True:
        choice = input("Ваш выбор: ").strip()

        if choice == "1":
            print("Для обработки выбран JSON-файл.")
            return read_transactions_from_json("data/operations.json")

        elif choice == "2":
            print("Для обработки выбран CSV-файл.")
            return read_transactions_from_csv("data/transactions.csv")

        elif choice == "3":
            print("Для обработки выбран XLSX-файл.")
            return read_transactions_from_excel("data/transactions_excel.xlsx")

        else:
            print("Ошибка: выберите 1, 2 или 3.")


def select_status() -> str:
    """Запрашивает корректный статус."""
    allowed = {"EXECUTED", "CANCELED", "PENDING"}

    while True:
        print("\nВведите статус для фильтрации:")
        print("Доступные статусы: EXECUTED, CANCELED, PENDING")

        status = input("Статус: ").strip().upper()

        if status in allowed:
            print(f'Операции отфильтрованы по статусу "{status}".')
            return status

        print(f'Статус "{status}" недоступен.\n')


def yes_no(prompt: str) -> bool:
    """Да/Нет → True/False."""
    answer = input(prompt + " Да/Нет: ").strip().lower()
    return answer in ("да", "y", "yes")


def main() -> None:
    """Основная логика программы."""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n")

    data = select_file()

    if not data:
        print("Файл пуст или содержит некорректные данные.")
        return

    # Фильтрация по статусу
    status = select_status()
    data = filter_by_state(data, status)

    if not data:
        print("Нет транзакций с таким статусом.")
        return

    # Сортировка
    if yes_no("Отсортировать операции по дате?"):
        descending = not yes_no("Отсортировать по возрастанию?")
        data = sort_by_date(data, descending)

    # Только рублевые
    if yes_no("Выводить только рублевые транзакции?"):
        data = [
            tr for tr in data
            if tr.get("operationAmount", {}).get("currency", {}).get("code") == "RUB"
        ]

    if not data:
        print("После фильтрации не осталось транзакций.")
        return

    # Поиск по описанию
    if yes_no("Отфильтровать по слову в описании?"):
        word = input("Введите слово: ").strip()
        data = process_bank_search(data, word)

    if not data:
        print("Не найдено ни одной транзакции, подходящей под ваши условия.")
        return

    print("\nРаспечатываю итоговый список транзакций...\n")
    print(f"Всего операций в выборке: {len(data)}\n")

    for tr in data:
        print_transaction(tr)


if __name__ == "__main__":
    main()
