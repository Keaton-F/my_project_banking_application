from src import masks

def mask_account_card(user_data: str) -> str:
    list_user_data = user_data.lower().replace('ё', 'е').split()
    user_data_type = None
    found_index = None
    for index, item in enumerate(list_user_data):
        if len(item) == 16 and not 'счет' in list_user_data:
            found_index = index
            user_data_type = 'card'
        elif item == 'счет' and len(list_user_data) == 2:
            found_index = -index - 1
            user_data_type = 'account'
    if user_data_type == 'card':
        message_for_user = f'Карта {masks.get_mask_card_number(list_user_data[found_index])}'
    elif user_data_type == 'account':
        message_for_user = f'Счёт {masks.get_mask_account(list_user_data[found_index])}'
    else:
        message_for_user = 'Некорректный ввод: тип данных не является номером карты или номером счёта.'
    return message_for_user
