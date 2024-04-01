import json

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
    sorted_list = sorted(operations_data, key=lambda x: x['date'])
    return sorted_list


data = open_json_file()
operations = filter_operations(data)
operations = sort_operations(operations)
print(operations)
