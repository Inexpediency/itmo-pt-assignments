def kth(a, k):
    """k-е по величине значение в массиве"""

    return sorted(a)[k-1]


def head_tail(a, k):
    """Первые и последние k элементов в массиве"""

    return a[0:k] + a[len(a)-k:len(a)]


def filter_sort(a, c):
    """Отсортировать копию массива, удалив строки с символом c"""

    array = []

    for line in a:
        if c not in line:
            array.append(line)

    return sorted(array)


def build_dict(keys, values):
    """Построить словарь по набору ключей и значений"""

    d = dict()

    for i in range(0, len(keys), 1):
        d[keys[i]] = values[i]

    return d


def compare_contents(a1, a2):
    """Проверка наборов элементов на совпадение"""

    s1, s2 = set(a1), set(a2)
    return s1 == s2
