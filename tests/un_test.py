import unittest
from unittest.mock import patch, mock_open
import json
from src.main import open_json_file, filter_operations, sort_operations, mask_operation_info, format_date

class TestOperations(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data=json.dumps([
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        }
    ]))
    def test_open_json_file(self, mock_file):
        data = open_json_file()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['id'], 441945886)

    def test_filter_operations(self):
        operations_data = [
            {"state": "EXECUTED"},
            {"state": "PENDING"},
            {"state": "EXECUTED"}
        ]
        filtered_list = filter_operations(operations_data)
        self.assertEqual(len(filtered_list), 2)

    def test_sort_operations(self):
        operations_data = [
            {"date": "2019-08-26T10:50:58.294041"},
            {"date": "2019-07-03T18:35:29.512364"}
        ]
        sorted_list = sort_operations(operations_data)
        self.assertEqual(sorted_list[0]['date'], "2019-08-26T10:50:58.294041")

    def test_mask_operation_info(self):
        operation = {"from": "Maestro 1596837868705199"}
        masked_info = mask_operation_info(operation)
        self.assertEqual(masked_info, "Maestro 1596 83** **** 5199")

    def test_format_date(self):
        operation = {"date": "2019-08-26T10:50:58.294041"}
        formatted_date = format_date(operation)
        self.assertEqual(formatted_date, "26.08.2019")

if __name__ == '__main__':
    unittest.main()