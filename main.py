import json

def open_json_file():
    with open('operations.json', encoding='utf-8') as f:
        return json.load(f)

def filter_operations(data):
    filtered_list = []
    for operation in data:
        if operation in data:
            if operation.get('state') == 'EXECUTED':
                filtered_list.append(operation)
    return filtered_list

data = open_json_file()
operations = filter_operations(data)
print(operations)
