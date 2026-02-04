from unittest.mock import patch, MagicMock
from src.readers import read_transactions_from_csv, read_transactions_from_excel


@patch("pandas.read_csv")
def test_read_transactions_from_csv(mock_read_csv):
    # Фейковый DataFrame - MagicMock
    mock_df = MagicMock()
    mock_df.to_dict.return_value = [
        {"id": 1, "amount": 100},
        {"id": 2, "amount": 200},
    ]
    mock_read_csv.return_value = mock_df

    path = "test.csv"
    result = read_transactions_from_csv(path)

    # Проверяем вызов pandas.read_csv
    mock_read_csv.assert_called_once_with(path)

    # Проверяем правильный возврат списка словарей
    assert result == [
        {"id": 1, "amount": 100},
        {"id": 2, "amount": 200},
    ]


@patch("pandas.read_excel")
def test_read_transactions_from_excel(mock_read_excel):
    mock_df = MagicMock()
    mock_df.to_dict.return_value = [
        {"id": 10, "amount": 999},
        {"id": 20, "amount": 555},
    ]
    mock_read_excel.return_value = mock_df

    path = "test.xlsx"
    result = read_transactions_from_excel(path)

    # Проверяем вызов pandas.read_excel
    mock_read_excel.assert_called_once_with(path)

    # Проверяем данные
    assert result == [
        {"id": 10, "amount": 999},
        {"id": 20, "amount": 555},
    ]
