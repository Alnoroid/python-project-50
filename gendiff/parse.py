import os
import json

def generate_diff(file_path1, file_path2):
    file1 = load_file(os.path.abspath(file_path1))
    file2 = load_file(os.path.abspath(file_path2))
    print(file1)
    print(file2)

    # file1 = open(os.path(file_path1), 'r')
    # file2 = open(os.path(file_path2), 'r')

def load_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)
