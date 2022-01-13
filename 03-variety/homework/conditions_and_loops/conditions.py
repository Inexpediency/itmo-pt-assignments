def median(a, b, c):
    """
    Вернуть медиану из трех элементов
    median(2, 5, 3) -> 3
    """
    return sorted([a, b, c])[1]


def get_or_none(a, index):
    """
    Вернуть a[index], если он существует, иначе None
    get_or_none([1, 2, 3], 2) -> 2
    get_or_none([1, 2], 2)    -> None
    """
    if index >= 0 and index < len(a):
        return a[index]
    if index == -1 and len(a) >= 1:
        return a[index]
    if index < 0 and abs(index + 1) < len(a):
        return a[index]
    return None


def is_power_of_two(x):
    """
    Вернуть, является ли x степенью двойки
    is_power_of_two(8) -> True
    is_power_of_two(0) -> False
    """
    s = bin(x)
    return True if s[2] == '1' and s[3:] == len(s[3:]) * '0' else False

def is_monotonic(a, b, c):
    """
    Проверить, является ли [a, b, c] строго монотонной последовательностью
    is_monotonic(1, 2, 3) -> True
    is_monotonic(9, 5, 4) -> True
    is_monotonic(6, 7, 6) -> False
    """
    return max(a, c) > b > min(a,c) or False

def inline_if(a, b, condition):
    """
    Вернуть a, если condition == True, и b иначе. Тело функции должно занимать одну строку
    inline_if(1, 2, False) -> 2
    """
    return a if condition else b

