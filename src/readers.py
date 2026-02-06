from typing import Any, Dict, List

import pandas as pd


def read_transactions_from_csv(path: str) -> List[Dict[str, Any]]:
    """
    Считывает финансовые транзакции из CSV-файла и возвращает список словарей.
    :param path: Путь к CSV-файлу.
    :return: Список словарей с транзакциями.
    """
    df: pd.DataFrame = pd.read_csv(path, sep=';')
    # Явное преобразование ключей в строки
    return [{str(k): v for k, v in row.items()} for row in df.to_dict(orient="records")]


def read_transactions_from_excel(path: str) -> List[Dict[str, Any]]:
    """
    Считывает финансовые транзакции из Excel-файла и возвращает список словарей.
    :param path: Путь к Excel-файлу.
    :return: Список словарей с транзакциями.
    """
    df: pd.DataFrame = pd.read_excel(path)
    return [{str(k): v for k, v in row.items()} for row in df.to_dict(orient="records")]
