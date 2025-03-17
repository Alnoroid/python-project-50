from pathlib import Path
import pytest
from gendiff.parse import read_file, check_extension

def test_read_file_unsupported_format():
    with pytest.raises(NotImplementedError):
        read_file(Path(__file__).parent / 'test_data' / 'unsupported.exe')



def test_check_extension():
    f1_ext = Path(__file__).parent / 'test_data' / 'file1.json'
    f2_ext = Path(__file__).parent / 'test_data' / 'file2.yml'
    with pytest.raises(ValueError):
        check_extension(f1_ext, f2_ext)