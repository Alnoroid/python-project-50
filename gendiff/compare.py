from .formatters.json import format_json
from .formatters.plain import format_plain
from .formatters.stylish import format_stylish
from .parse import compare_files


def generate_diff(file_path1, file_path2, format_name='stylish'):
    diff = compare_files(file_path1, file_path2)
    if format_name == 'stylish':
        return '{\n' + format_stylish(diff) + '\n}'
    elif format_name == 'plain':
        return format_plain(diff)
    elif format_name == 'json':
        print(format_json(diff))
        return format_json(diff)