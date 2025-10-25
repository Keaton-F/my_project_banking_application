import datetime
import functools
from typing import Any, Callable, Optional, TypeVar

# Тип-переменная для описания возвращаемого значения функции
T = TypeVar("T")


def log(filename: Optional[str] = None) -> Callable[[Callable[..., T]], Callable[..., T]]:
    """
    Декоратор для логирования вызовов функций, их аргументов, результатов и ошибок.

    :param filename: путь к файлу для записи логов (если None — лог в консоль)
    :return: декоратор, оборачивающий целевую функцию
    """

    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> T:
            timestamp: str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            try:
                result: T = func(*args, **kwargs)
                success_message: str = f"{timestamp} | {func.__name__} ok"
                _write_log(success_message, filename)
                return result
            except Exception as e:
                error_type: str = type(e).__name__
                error_message: str = f"{timestamp} | {func.__name__} error: {error_type}. " f"Inputs: {args}, {kwargs}"
                _write_log(error_message, filename)
                raise  # пробрасываем ошибку дальше

        return wrapper

    return decorator


def _write_log(message: str, filename: Optional[str] = None) -> None:
    """
    Помощник для записи в файл или консоль.

    :param message: строка лога для записи
    :param filename: путь к файлу, если нужно логировать в файл
    """
    if filename:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(message + "\n")
    else:
        print(message)
