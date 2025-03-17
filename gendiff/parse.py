import json
import os

import yaml


def read_file(file_path):
    extension = os.path.splitext(file_path)[1]
    with open(file_path, 'r') as file:
        if extension == '.json':
            return json.load(file)
        elif extension == '.yml' or extension == '.yaml':
            return yaml.safe_load(file)
        else:
            raise NotImplementedError


def compare_files(file_path1, file_path2):
    check_extension(file_path1, file_path2)

    file1 = read_file(os.path.abspath(file_path1))
    file2 = read_file(os.path.abspath(file_path2))
    diff = parse_files(file1, file2)
    return diff


def check_extension(file_path1, file_path2):
    extension1 = os.path.splitext(file_path1)[1]
    extension2 = os.path.splitext(file_path2)[1]
    if extension1 != extension2:
        raise ValueError(
            f"Extension mismatch {extension1} != {extension2}"
        )


def parse_files(file1, file2):
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