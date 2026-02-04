import pandas as pd
from typing import List, Dict


def read_transactions_from_csv(path: str) -> List[Dict]:
    """
    Считывает финансовые транзакции из CSV-файла и возвращает список словарей.
    :param path: Путь к CSV-файлу.
    :return: Список словарей с транзакциями.
    """
    df = pd.read_csv(path)
    return df.to_dict(orient="records")


def read_transactions_from_excel(path: str) -> List[Dict]:
    """
    Считывает финансовые транзакции из Excel-файла и возвращает список словарей.
    :param path: Путь к Excel-файлу.
    :return: Список словарей с транзакциями.
    """
    df = pd.read_excel(path)
    return df.to_dict(orient="records")
