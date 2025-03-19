def format_stylish(diff, indent=2):
    result = []
    for key, data in diff.items():
        status = data['status']
        match status:
            case 'added':
                result.append(f"{' ' * indent}+ {key}: "
                              f"{format_value(data['value'], indent + 4)}")
            case 'removed':
                result.append(f"{' ' * indent}- {key}: "
                              f"{format_value(data['value'], indent + 4)}")
            case 'unchanged':
                result.append(f"{' ' * indent}  {key}: "
                              f"{format_value(data['value'], indent + 4)}")
            case 'updated':
                result.append(f"{' ' * indent}- {key}: "
                              f"{format_value(data['old_value'], indent + 4)}")
                result.append(f"{' ' * indent}+ {key}: "
                              f"{format_value(data['new_value'], indent + 4)}")
            case 'nested':
                result.append(f"{' ' * indent}  {key}: " + '{')
                result.append(format_stylish(data['children'], indent + 4))
                result.append(f"{' ' * indent}" + '  }')
    return '\n'.join(result)


def format_value(value, indent):
    if isinstance(value, dict):
        formatted_items = []
        for k, v in value.items():
            formatted_items.append(f"{' ' * (indent + 2)}{k}: "
                                   f"{format_value(v, indent + 4)}")
        return ('{\n' + '\n'.join(formatted_items) +
                '\n' + ' ' * (indent - 2) + '}')
    else:
        return str(value)
