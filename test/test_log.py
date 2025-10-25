import pytest
from src.decorators.log import log
from pathlib import Path


def test_log_to_file(tmp_path: Path):
    """
    Проверяет, что при успешном выполнении функции с декоратором log,
    сообщение с текстом "<имя функции> ok" записывается в указанный лог-файл.
    """
    log_file = tmp_path / "test_log.txt"

    @log(filename=str(log_file))
    def add(x, y):
        return x + y

    add(1, 2)

    content = log_file.read_text(encoding="utf-8")
    assert "add ok" in content


def test_log_error_to_file(tmp_path: Path):
    """
    Проверяет, что при возникновении исключения декоратор log
    записывает в лог-файл сообщение об ошибке с типом исключения
    и входными аргументами функции.
    """
    log_file = tmp_path / "error_log.txt"

    @log(filename=str(log_file))
    def div(x, y):
        return x / y  # вызовет ZeroDivisionError

    with pytest.raises(ZeroDivisionError):
        div(1, 0)

    content = log_file.read_text(encoding="utf-8")
    assert "div error: ZeroDivisionError" in content
    assert "Inputs: (1, 0)" in content


def test_log_to_console(capsys):
    """
    Проверяет, что при отсутствии аргумента filename
    декоратор log выводит сообщение о выполнении функции в консоль.
    Для проверки используется фикстура capsys, которая перехватывает stdout.
    """
    @log()
    def mult(x, y):
        return x * y

    mult(2, 3)
    captured = capsys.readouterr()
    assert "mult ok" in captured.out
