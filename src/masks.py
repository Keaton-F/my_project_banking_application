import logging
from pathlib import Path

# Настройка логера для masks
log_path = Path("logs")
log_path.mkdir(exist_ok=True)

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(log_path / "masks.log", mode="w", encoding="utf-8")
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

logger.debug("Логгер masks настроен и работает")


def get_mask_card_number(user_card_number: str) -> str:
    """Функция, преобразующая полный номер карты в маску XXXX XX** **** XXXX, принимает на вход
    строку и возвращает новую строку, где первые 6 цифр показываются, а остальные заменяются
    на звездочки, с сохранением пробелов для форматирования."""
    if user_card_number:
        user_card_number = user_card_number.replace(" ", "")
        if user_card_number.isdigit():
            if len(user_card_number) == 16:
                mask_card_number = user_card_number[:6] + "******" + user_card_number[12:]
                message_for_user = " ".join([mask_card_number[i : i + 4] for i in range(0, len(mask_card_number), 4)])
                logger.debug(f"Успешно замаскирован номер карты: {user_card_number} -> {message_for_user}")
            elif len(user_card_number) > 16:
                message_for_user = "Номер не может содержать лишние символы."
                logger.error(f"Номер карты слишком длинный: {user_card_number}")
            else:
                message_for_user = "Не верный формат ввода."
                logger.error(f"Неверный формат номера карты: {user_card_number}")
        else:
            message_for_user = "Номер допускает для ввода только цифры."
            logger.error(f"Номер карты содержит недопустимые символы: {user_card_number}")
    else:
        message_for_user = "Данный параметр не может быть пустым."
        logger.error("Пустой ввод для номера карты")
    return message_for_user


def get_mask_account(user_account: str) -> str:
    """Функция, которая принимает номер счета в виде числа и возвращает его маску.
    Она преобразует число в строку, а затем применяет к нему форматирование, скрывая
    часть символов звездочками."""
    if user_account:
        if user_account.isdigit():
            if len(user_account) >= 6:
                message_for_user = "**" + user_account[-4:]
                logger.debug(f"Успешно замаскирован номер счета: {user_account} -> {message_for_user}")
            else:
                message_for_user = "Номер не может быть короче 6-ти символов."
                logger.error(f"Слишком короткий номер счета: {user_account}")
        else:
            message_for_user = "Номер не может содержать лишние символы."
            logger.error(f"Номер счета содержит недопустимые символы: {user_account}")
    else:
        message_for_user = "Данный параметр не может быть пустым."
        logger.error("Пустой ввод для номера счета")
    return message_for_user
