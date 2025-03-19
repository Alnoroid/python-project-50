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
    file1 = read_file(os.path.abspath(file_path1))
    file2 = read_file(os.path.abspath(file_path2))
    diff = parse_files(file1, file2)
    return diff


def parse_files(file1, file2):
    diff = {}
    all_keys = file1.keys() | file2.keys()

    for key in sorted(all_keys):
        value1 = file1.get(key)
        value2 = file2.get(key)

        if key not in file1:
            diff[key] = {'status': 'added', 'value': format_value(value2)}
        elif key not in file2:
            diff[key] = {'status': 'removed', 'value': format_value(value1)}
        elif value1 == value2:
            diff[key] = {'status': 'unchanged', 'value': format_value(value1)}
        elif isinstance(value1, dict) and isinstance(value2, dict):
            diff[key] = {'status': 'nested',
                         'children': parse_files(value1, value2)}
        else:
            diff[key] = \
                {'status': 'updated',
                 'old_value': format_value(value1),
                 'new_value': format_value(value2)}
    return diff


def format_value(value):
    if isinstance(value, bool):
        return 'true' if value else 'false'
    elif value is None:
        return 'null'
    return value