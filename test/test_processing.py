import pytest
from src.processing import filter_by_state, sort_by_date

# Фикстура с операциями
@pytest.fixture
def operations_fixture():
    return [
        {"state": "EXECUTED", "date": "2021-10-01T12:30:00"},
        {"state": "CANCELED", "date": "2021-11-01T10:00:00"},
        {"state": "CANCELED", "date": "2020-01-01T00:00:00"},
        {"state": "EXECUTED", "date": "2022-03-05T08:00:00"},
        {"state": "EXECUTED", "date": "invalid-date"},
    ]


# filter_by_state
def test_filter_by_state_found(operations_fixture):
    result = filter_by_state(operations_fixture, "EXECUTED")
    assert len(result) == 3
    for operation in result:
        assert operation["state"] == "EXECUTED"

def test_filter_by_state_not_found(operations_fixture):
    result = filter_by_state(operations_fixture, "NON_EXISTENT")
    assert result == []

@pytest.mark.parametrize("state", ["EXECUTED", "CANCELED"])
def test_filter_by_state_param(operations_fixture, state):
    result = filter_by_state(operations_fixture, state)
    for operation in result:
        assert operation["state"] == state


# sort_by_date
def test_sort_by_date_desc(operations_fixture):
    result = sort_by_date(operations_fixture, descending=True)
    valid_dates = [operation["date"] for operation in result if "T" in operation["date"]]
    assert valid_dates == sorted(valid_dates, reverse=True)

def test_sort_by_date_asc(operations_fixture):
    result = sort_by_date(operations_fixture, descending=False)
    valid_dates = [operation["date"] for operation in result if "T" in operation["date"]]
    assert valid_dates == sorted(valid_dates)

def test_sort_by_date_with_invalid(operations_fixture):
    result = sort_by_date(operations_fixture)
    assert isinstance(result, list)
