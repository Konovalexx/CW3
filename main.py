import json

def open_json_file():
    with open('operations.json', encoding='utf-8') as f:
        return json.load(f)

print(open_json_file())