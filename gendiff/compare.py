from .formatters.stylish import format_diff
from .parse import compare_files


def generate_diff(file_path1, file_path2, format_name='stylish'):
    diff = compare_files(file_path1, file_path2)
    if format_name == 'stylish':
        return '{\n' + format_diff(diff) + '\n}'