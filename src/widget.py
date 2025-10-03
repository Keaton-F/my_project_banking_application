from src import masks


def mask_account_card(user_data: str) -> str:
    """Функция, которая должна получить строку, чтобы проверить, чем является строка - номером карты
    или номером счёта. После проверки, функция обращается к модулю masks.py и возвращает маску или
    возвращает сообщение о том, что она получила некорректные данные."""
    list_user_data = user_data.lower().replace("ё", "е").split()
    user_data_type = None
    found_index = 0
    for index, item in enumerate(list_user_data):
        if (
            len(item) == 16 and not "счет" in list_user_data
        ):  # Является ли полученная строка номером карты И НЕ счётом.
            found_index = index
            user_data_type = "card"
        elif (
            item == "счет" and len(list_user_data) == 2
        ):  # Является ли строка счётом И состоит ли из 2 объектов список.
            found_index = -index - 1
            user_data_type = "account"
    if user_data_type == "card":
        message_for_user = f"Карта {masks.get_mask_card_number(list_user_data[found_index])}"
    elif user_data_type == "account":
        message_for_user = f"Счёт {masks.get_mask_account(list_user_data[found_index])}"
    else:
        message_for_user = "Некорректный ввод: тип данных не является номером карты или номером счёта."
    return message_for_user


def get_date(date_time_data: str) -> str:
    """Функция, которая получает строку, содержащую информацию о дате и времени, и форматирует её
    в более удобный для чтения формат, отбрасывая данные времени."""
    date_data = date_time_data.split("T")
    date_data_list = date_data[0].split("-")
    return f"{date_data_list[2]}.{date_data_list[1]}.{date_data_list[0]}"
