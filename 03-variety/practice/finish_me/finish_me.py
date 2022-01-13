def larger_than(a, x):
    """
    Вернуть все элементы a, большие x
    larger_than([1, 8, 11], 4) -> [8, 11]
    """
    return [b for b in a if b > x]


def names_to_strings(names, surnames):
    """
    Вернуть массив полных имен по данным именам и фамилиям
    names_to_strings(['Alice', 'John'], ['Smith', 'Doe']) -> ['Alice Smith', 'John Doe']
    """
    return [name + ' ' + surname for name, surname in zip(names, surnames)]


def last_first(s):
    """
    Поменять в строке s первую и последнюю букву местами
    last_first('Hello') -> 'oellH'
    """
    if len(s) < 2:
        return s
    return s[-1] + s[1:-1] + s[0]


def int_strings(a):
    """
    Преобразовать числа в строки, а строки - в числа
    int_strings([1, '2', 3, '4']) -> ['1', 2, '3', 4]
    """

    def change_item(x):
        return str(x) if isinstance(x, int) else int(x)

    return list(map(change_item, a))


def no_long_words(s):
    """
    Вернуть строку, состоящую только из слов s, не длинее 5 символов
    no_long_words('Hello beautiful world') -> 'Hello world'
    """
    words = s.split(' ')
    return ' '.join([word for word in words if len(word) <= 5])
