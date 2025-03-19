def format_plain(diff, path=''):
    result = []
    for key, data in diff.items():
        status = data['status']
        match status:
            case 'added':
                result.append(f"Property '{path}{key}' was added "
                              f"with value: {format_value(data['value'])}")
            case 'removed':
                result.append(f"Property '{path}{key}' was removed")
            case 'updated':
                result.append(f"Property '{path}{key}' was updated. "
                              f"From {format_value(data['old_value'])} "
                              f"to {format_value(data['new_value'])}")
            case 'nested':
                result.append(format_plain(data['children'], path + key + '.'))
    return '\n'.join(result)


def format_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, str) and value not in ['true', 'false', 'null']:
        return f"\'{value}\'"

    return value