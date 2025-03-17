from .parse import compare_files


def generate_diff(file_path1, file_path2):
    diff = compare_files(file_path1, file_path2)
    return format_diff(diff)


def format_diff(diff):
    result = []
    for key, data in diff.items():
        status = data['status']

        if status == 'added':
            result.append(f"+ {key}: {data['value']}")
        elif status == 'removed':
            result.append(f"- {key}: {data['value']}")
        elif status == 'updated':
            result.append(f"- {key}: {data['old_value']}")
            result.append(f"+ {key}: {data['new_value']}")
        elif status == 'unchanged':
            result.append(f"  {key}: {data['value']}")
    return '{\n  ' + '\n  '.join(result) + '\n}'
