def filter_by_currency(transactions, currency):
    """
    Принимает список транзакций и возвращает итератор,
    который выдаёт только те, у которых код валюты совпадает с заданным.
    """
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield transaction


def transaction_descriptions(sample_transactions):
    """
    Генератор, возвращающий описание каждой транзакции из списка.
    """
    for transaction in sample_transactions:
        yield transaction.get("description")


