def get_mask_card_number(user_card_number: str) -> str:
    """Функция, преобразующая полный номер карты в маску XXXX XX** **** XXXX, принимает на вход
    номер карты, преобразует его в строку и возвращает новую строку, где первые 6 цифр
    показываются, а остальные заменяются на звездочки, с сохранением пробелов для
    форматирования."""
    formatted_card_number = user_card_number.replace(" ", "")
    if formatted_card_number.isdigit() and len(formatted_card_number) == 16:
        mask_card_number = formatted_card_number[:6] + "******" + formatted_card_number[12:]
        message_for_user = " ".join([mask_card_number[i : i + 4] for i in range(0, len(mask_card_number), 4)])
    elif formatted_card_number.isdigit() and not len(formatted_card_number) == 16:
        message_for_user = "Не верный формат ввода."
    else:
        message_for_user = "Номер не может содержать лишние символы."
    return message_for_user


def get_mask_account(user_account: str) -> str:
    """Функция, которая принимает номер счета в виде числа и возвращает его маску.
    Она преобразует число в строку, а затем применяет к нему форматирование, скрывая
    часть символов звездочками."""
    formated_account = user_account.replace(" ", "")
    if formated_account.isdigit():
        message_for_user = "**" + formated_account[-4:]
    else:
        message_for_user = "Номер не может содержать лишние символы."
    return message_for_user
