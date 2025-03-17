from pathlib import Path
from gendiff import generate_diff

def get_test_data_path(filename):
    return Path(__file__).parent / 'test_data' / filename
#
def read_file(filename):
    return get_test_data_path(filename).read_text()

def test_generate_diff():
    test_cases = [
        'json',
        'yml'
    ]

    for extension in test_cases:
        file1 = get_test_data_path(f"file1.{extension}")
        file2 = get_test_data_path(f"file2.{extension}")
        expected_output = read_file('result')

        result = generate_diff(file1, file2)
        assert result == expected_output, f"Test failed for {extension}"