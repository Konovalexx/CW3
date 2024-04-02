from src.data_operations import open_json_file, filter_operations, sort_operations, mask_operation_info, format_date

def main():
    """
    Главная функция программы, которая загружает данные, фильтрует и сортирует операции,
    а затем выводит информацию о каждой операции.
    """
    data = open_json_file()
    operations = filter_operations(data)
    operations = sort_operations(operations)[:5]

    for operation in operations:
        print(format_date(operation), operation['description'], end="\n")
        print(mask_operation_info(operation))
        print(f"{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}")
        print()

if __name__ == "__main__":
    main()