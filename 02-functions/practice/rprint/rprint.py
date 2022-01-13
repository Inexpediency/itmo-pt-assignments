def flatten(a):
    """Вернуть все числа, содержащиеся в массиве на любом уровне вложенности"""
    result = []
    for e in a:
        if isinstance(e, list):
            result += flatten(e)
        else:
            result.append(e)
    return result


def rprint(a, depth, current_depth=0):
    """Вернуть строковое представление массива, обрезав его по глубине depth"""
    result = ''
    if depth <= 0:
        return '[...]'
    for i in a:
        if isinstance(i, list):
            result += f', {rprint(i, depth - 1)}'
        else:
            result += f', {i}'
    return '[' + result[2:] + ']'


def get_spaces(depth):
    return ' ' * 4 * depth


def is_contains_sublists(array):
    for e in array:
        if isinstance(e, list):
            return True
    return False


def stringify(arr):
    if len(arr) == 0:
        return '[ ]'
    return f'[ {" ".join(list(map(lambda x: str(x), arr)))} ]'


# noinspection PyShadowingBuiltins
def pretty_rprint(a, current_depth=0, print=print):
    """Вывести массив, делая отступы, соответствующие уровню вложенности"""
    if not is_contains_sublists(a):
        print(get_spaces(current_depth) + stringify(a))
        return

    print(get_spaces(current_depth) + '[')
    for e in a:
        if isinstance(e, list):
            if is_contains_sublists(e):
                pretty_rprint(e, current_depth=current_depth + 1, print=print)
            else:
                print(get_spaces(current_depth + 1) + stringify(e))
        else:
            print(get_spaces(current_depth + 1) + str(e))
    print(get_spaces(current_depth) + ']')
