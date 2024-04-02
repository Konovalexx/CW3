import pytest
from src.main import open_json_file, filter_operations, sort_operations, mask_operation_info, format_date

@pytest.fixture
def mock_operations_data():
    return [
        {"state": "EXECUTED", "date": "2019-08-26T10:50:58.294041"},
        {"state": "PENDING", "date": "2019-07-03T18:35:29.512364"},
        {"state": "EXECUTED", "date": "2019-06-30T02:08:58.425572"}
    ]

def test_open_json_file_non_existent_file(mocker):
    mocker.patch('builtins.open', side_effect=FileNotFoundError)
    with pytest.raises(FileNotFoundError):
        open_json_file()



def test_filter_operations(mock_operations_data):
    filtered_list = filter_operations(mock_operations_data)
    assert len(filtered_list) == 2





def test_sort_operations(mock_operations_data):
    sorted_list = sort_operations(mock_operations_data)
    assert sorted_list[0]['date'] == "2019-08-26T10:50:58.294041"



def test_mask_operation_info():
    operation = {"from": "Maestro 1596837868705199"}
    masked_info = mask_operation_info(operation)
    assert masked_info == "Maestro 1596 83** **** 5199"

def test_format_date():
    operation = {"date": "2019-08-26T10:50:58.294041"}
    formatted_date = format_date(operation)
    assert formatted_date == "26.08.2019"