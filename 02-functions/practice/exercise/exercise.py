def twice(fun, arg):
    """Вернуть результат применения функции fun дважды к аргументу arg"""
    return fun(fun(arg))


def foreach(funs, items):
    """Применить функции из массива funs к соответствующим элементам массива items"""
    return [funs[i](item) for i, item in enumerate(items)]


def apply(fun, args, kwargs):
    """Вернуть результат вызова функции fun с переданными позиционными и именными аргументами"""
    return fun(*args, **kwargs)


def all_ternary(n):
    """Вернуть все троичные числа длины n в алфавитном порядке"""
    if n == 0:
        return ['']
    if n == 1:
        return ['0', '1', '2']

    previous = all_ternary(n - 1) * 3
    result = []
    step = len(previous) // 3
    symbols = ['0', '1', '2']
    i = 0
    pointer = 0

    for p in previous:
        if i >= step:
            i = 0
            pointer += 1
        result.append(symbols[pointer] + p)
        i += 1

    return result


def swap_arguments(fun):
    """Вернуть функцию, принимающую аргументы в противоположном от fun порядке"""
    return lambda *args: fun(*reversed(args))
