import json
import os


def generate_diff(file_path1, file_path2):
    file1 = read_file(os.path.abspath(file_path1))
    file2 = read_file(os.path.abspath(file_path2))

    diff = compare_files(file1, file2)
    return format_diff(diff)


def read_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def compare_files(file1, file2):
    diff = {}
    all_keys = file1.keys() | file2.keys()

    for key in sorted(all_keys):
        value1 = file1.get(key)
        value2 = file2.get(key)

        if key not in file1:
            diff[key] = {'status': 'added', 'value': value2}
        elif key not in file2:
            diff[key] = {'status': 'removed', 'value': value1}
        elif value1 == value2:
            diff[key] = {'status': 'unchanged', 'value': value1}
        else:
            diff[key] = \
                {'status': 'updated', 'old_value': value1, 'new_value': value2}

    return diff


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