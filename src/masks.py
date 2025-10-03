def get_mask_card_number(user_card_number: str) -> str:
    """Функция, преобразующая полный номер карты в маску XXXX XX** **** XXXX, принимает на вход
    строку и возвращает новую строку, где первые 6 цифр показываются, а остальные заменяются
    на звездочки, с сохранением пробелов для форматирования."""
    if user_card_number.isdigit() and len(user_card_number) == 16:
        mask_card_number = user_card_number[:6] + "******" + user_card_number[12:]
        message_for_user = " ".join([mask_card_number[i : i + 4] for i in range(0, len(mask_card_number), 4)])
    elif user_card_number.isdigit() and not len(user_card_number) == 16:
        message_for_user = "Не верный формат ввода."
    else:
        message_for_user = "Номер не может содержать лишние символы."
    return message_for_user


def get_mask_account(user_account: str) -> str:
    """Функция, которая принимает номер счета в виде числа и возвращает его маску.
    Она преобразует число в строку, а затем применяет к нему форматирование, скрывая
    часть символов звездочками."""
    if user_account.isdigit():
        message_for_user = "**" + user_account[-4:]
    else:
        message_for_user = "Номер не может содержать лишние символы."
    return message_for_user
