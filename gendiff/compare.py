from .formatters.stylish import format_stylish
from .formatters.plain import format_plain
from .parse import compare_files


def generate_diff(file_path1, file_path2, format_name='stylish'):
    diff = compare_files(file_path1, file_path2)
    if format_name == 'stylish':
        return '{\n' + format_stylish(diff) + '\n}'
    if format_name == 'stylish':
        return '{\n' + format_plain(diff) + '\n}'