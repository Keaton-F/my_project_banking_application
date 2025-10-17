from src import masks


def mask_account_card(user_data: str) -> str:
    """Функция, которая должна получить строку, чтобы проверить, чем является строка - номером карты
    или номером счёта. После проверки, функция обращается к модулю masks.py и возвращает маску или
    возвращает сообщение о том, что она получила некорректные данные."""
    list_formatted_user_data = user_data.lower().replace("ё", "е").split()
    list_user_data = user_data.split()
    user_data_type = None
    found_index = 0
    if user_data:
        for index, item in enumerate(list_formatted_user_data):
            if len(item) == 16 and not "счет" in list_formatted_user_data:
                found_index = index
                user_data_type = "card"
            elif item == "счет" and len(list_formatted_user_data) == 2:
                found_index = -index - 1
                user_data_type = "account"
        if user_data_type == "card":
            card_number = "".join([i for i in list_user_data if len(i) == 16])
            mask_card_number = masks.get_mask_card_number(card_number)
            card_name = " ".join([i for i in list_user_data if i != card_number])
            message_for_user = f"{card_name} {mask_card_number}"
        elif user_data_type == "account":
            message_for_user = f"Счёт {masks.get_mask_account(list_formatted_user_data[found_index])}"
        else:
            message_for_user = "Некорректный ввод: тип данных не является номером карты или номером счёта."
    else:
        message_for_user = "Данный параметр не может быть пустым."
    return message_for_user


def get_date(date_time_data: str) -> str | None:
    """Функция, которая получает строку, содержащую информацию о дате и времени, и форматирует её
    в более удобный для чтения формат, отбрасывая данные времени."""
    invalid_date = "Ошибка данных: значение не является датой, или имеет неверный формат."
    if date_time_data:
        date_data = date_time_data.split("T")
        if len(date_data[0]) == 10:
            date_data_list = date_data[0].split("-")
            if "".join([i for i in date_data_list]).isdigit():
                if int(date_data_list[1]) <= 12 or int(date_data_list[2]) <= 31:
                    return f"{date_data_list[2]}.{date_data_list[1]}.{date_data_list[0]}"
                else:
                    return invalid_date
            else:
                return invalid_date
        else:
            return invalid_date
    return None
