import json
import datetime as dt

def open_json_file():
    """
    Открывает и читает JSON файл 'operations.json', возвращая его содержимое в виде словаря.

    Returns:
        dict: Словарь с данными из файла 'operations.json'.
    """
    with open('operations.json', encoding='utf-8') as f:
        return json.load(f)

def filter_operations(operations_data):
    """
    Фильтрует список операций, оставляя только те, у которых состояние равно 'EXECUTED'.

    Args:
        operations_data (list): Список операций.

    Returns:
        list: Фильтрованный список операций.
    """
    return [operation for operation in operations_data if operation.get('state') == 'EXECUTED']

def sort_operations(operations_data: list[dict]) -> list[dict]:
    """
    Сортирует список операций по дате в обратном порядке.

    Args:
        operations_data (list[dict]): Список операций.

    Returns:
        list[dict]: Отсортированный список операций.
    """
    return sorted(operations_data, key=lambda x: x['date'], reverse=True)

def mask_operation_info(operation):
    """
    Маскирует информацию об операции, скрывая часть номера счета.

    Args:
        operation (dict): Словарь с информацией об операции.

    Returns:
        str: Маскированная информация об операции.
    """
    def mask_credit_card_or_account(number):
        if len(number) == 16:
            return f"{number[:4]} {number[4:6]}** **** {number[-4:]}"
        else:
            return '*' * (len(number) - 4) + number[-4:]

    operation_from = operation.get('from')
    operation_to = operation.get('to')

    if operation_from and operation_to:
        from_parts = operation_from.split(' ')
        to_parts = operation_to.split(' ')
        from_numbers = from_parts[-1]
        to_numbers = to_parts[-1]
        masked_from_numbers = mask_credit_card_or_account(from_numbers)
        masked_to_numbers = mask_credit_card_or_account(to_numbers)
        return f"{from_parts[0]} {masked_from_numbers} -> {to_parts[0]} {masked_to_numbers}"
    elif operation_from:
        parts = operation_from.split(' ')
        numbers = parts[-1]
        masked_numbers = mask_credit_card_or_account(numbers)
        return f"{parts[0]} {masked_numbers}"
    elif operation_to:
        parts = operation_to.split(' ')
        numbers = parts[-1]
        masked_numbers = mask_credit_card_or_account(numbers)
        return f"{parts[0]} {masked_numbers}"
    else:
        return "Неизвестный источник или получатель"

def format_date(operations):
    """
    Форматирует дату операции в формат "dd.mm.yyyy".

    Args:
        operations (dict): Словарь с информацией об операции.

    Returns:
        str: Форматированная дата операции.
    """
    date = operations['date']
    dt_time = dt.datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
    return dt_time.strftime("%d.%m.%Y")

data = open_json_file()
operations = filter_operations(data)
operations = sort_operations(operations)[:5]

for operation in operations:
    print(format_date(operation), operation['description'], end="\n")
    print(mask_operation_info(operation))
    print(f"{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}")
    print()