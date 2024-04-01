import json
import datetime as dt

def open_json_file():
    with open('operations.json', encoding='utf-8') as f:
        return json.load(f)

def filter_operations(operations_data):
    filtered_list = []
    for operation in operations_data:
        if operation.get('state') == 'EXECUTED':
            filtered_list.append(operation)
    return filtered_list

def sort_operations(operations_data: list[dict]) -> list[dict]:
    sorted_list = sorted(operations_data, key=lambda x: x['date'], reverse=True)
    return sorted_list

def mask_operation_info(operation):
    operation_from = operation.get('from')
    operation_to = operation.get('to')

    if operation_from:
        parts = operation_from.split(' ')
        numbers = parts[-1]
        if len(numbers) == 16:
            masked_numbers = f"{numbers[:4]} {numbers[4:6]}** **** {numbers[-4:]}"
            return f"{" ".join(parts[:-1])} {masked_numbers}"
        else:
            return f'Счет **{numbers[-4:]}'

def format_date(operations):
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