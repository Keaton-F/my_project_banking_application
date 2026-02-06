import json
import logging
from pathlib import Path
from typing import Any, Dict, List

# Настройка логера для utils
log_path = Path("logs")
log_path.mkdir(exist_ok=True)

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(log_path / "utils.log", mode="w", encoding="utf-8")
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Тестовая запись для проверки
logger.debug("Логгер utils настроен и работает")


def read_json(file_path: str) -> List[Dict[str, Any]]:
    """
    Читает JSON-файл и возвращает список словарей с данными о транзакциях.

    Args:
        file_path (str): путь к JSON-файлу

    Returns:
        List[Dict[str, Any]]: список транзакций
        Если файл пустой, некорректный или не найден, возвращает пустой список.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        if not isinstance(data, list):
            logger.error(f"Файл {file_path} не содержит список")
            return []

        logger.debug(f"Успешно прочитан файл {file_path}, найдено {len(data)} записей")
        return data

    except FileNotFoundError:
        logger.error(f"Файл {file_path} не найден")
        return []
    except json.JSONDecodeError:
        logger.error(f"Файл {file_path} содержит некорректный JSON")
        return []
