def increase_ints(s):
    """Увеличить на 1 только целые числа в множестве"""
<<<<<<< HEAD
    return set(map(lambda i: i + 1 if isinstance(i, int) else i, s))


def weird_condition(a, b, x, y, z):
    """Довольно сомнительной адекватности условие (см. _legend.md)"""
    return all(map(lambda i: i % x == 0, a)) and all(map(lambda i: i % y == 0, b)) and all(map(lambda i: ((i in a) and (i not in b)) or ((i in b) and (i not in a)), [i for i in a if i % z == 0] + [i for i in b if i % z == 0]))
=======

    return set(elem + 1 if type(elem) == int else elem for elem in s)


def weird_condition(a, b, x, y, z):
    """Довольно сомнительной адекватности условие (см. _legend.md). Код смотрится достаточно неприятно, логичнее было бы использовать бэкслеши, что по идее делает строку "истинной" длины один гораздо более читаемой, но иначе нет прохождения теста test_one_line[weird_condition]"""

    return True if False not in list(True if elem % x == 0 else False for elem in set(a)) and False not in list(True if elem % y == 0 else False for elem in set(b)) and False not in list(True if elem % x == 0 and elem % y == 0 else False for elem in set(a) & set(b)) and (set(elem for elem in a if elem % z == 0) | set(elem for elem in b if elem % z == 0)).issubset(set(a) ^ set(b)) else False
>>>>>>> origin/practice


def index_of_median(a):
    """Индекс медианного значения массива"""
<<<<<<< HEAD
    return a.index(sorted(a)[(len(a) - 1) // 2])
=======

    return a.index(sorted(list(set(a)))[len(list(set(a)))//2])
>>>>>>> origin/practice
