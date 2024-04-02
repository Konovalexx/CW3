import json
import datetime as dt
import re

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
    filtered_list = []
    for operation in operations_data:
        if operation.get('state') == 'EXECUTED':
            filtered_list.append(operation)
    return filtered_list

def sort_operations(operations_data: list[dict]) -> list[dict]:
    """
    Сортирует список операций по дате в обратном порядке.

    Args:
        operations_data (list[dict]): Список операций.

    Returns:
        list[dict]: Отсортированный список операций.
    """
    sorted_list = sorted(operations_data, key=lambda x: x['date'], reverse=True)
    return sorted_list

def mask_operation_info(operation):
    """
    Маскирует информацию об операции, скрывая часть номера счета.

    Args:
        operation (dict): Словарь с информацией об операции.

    Returns:
        str: Маскированная информация об операции.
    """
    operation_from = operation.get('from')
    operation_to = operation.get('to')

    if operation_from:
        # Маскировка номера кредитной карты
        masked_from = re.sub(r'\d', '*', operation_from[:-4]) + operation_from[-4:]
        # Маскировка номера счета получателя
        masked_to = re.sub(r'\d', '*', operation_to[:-4]) + operation_to[-4:]
        return f"{masked_from} -> {masked_to}"
    else:
        # Маскировка номера счета получателя
        masked_to = re.sub(r'\d', '*', operation_to[:-4]) + operation_to[-4:]
        return f"{masked_to}"

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
    print(format_date(operation))
    print(operation['description'])
    print(mask_operation_info(operation))
    print(f"{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}")
    print() # Добавляем пустую строку для разделителя