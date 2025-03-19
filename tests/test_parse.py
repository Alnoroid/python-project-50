from pathlib import Path
import pytest
from gendiff.parse import read_file

def test_read_file_unsupported_format():
    with pytest.raises(NotImplementedError):
        read_file(Path(__file__).parent / 'test_data' / 'unsupported.exe')