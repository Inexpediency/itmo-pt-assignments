def sum_some(numbers, indices):
    """
    Вернуть сумму элементов из numbers, на позициях, записанных в indices
    sum_some([1, 2, 3], [0, 1, 1]) -> 5 = (1+2+2)
    """
    return sum([numbers[index] for index in indices])


def replace_range(a, b, x, y):
    """
    Заменить подмассив массива a с индексами от x до y на массив b
    replace_range([1, 2, 3, 4], [7, 8, 9], 0, 1) -> [7, 8, 9, 3, 4]
    """
    return a[:x] + b + a[y+1:]


def sum_list(a):
    """
    Рекурсивно просуммировать элементы массива a
    sum_list([1, 2, 3]) -> 6
    """
    def recursion(arr):
        if len(arr) == 0:
            return 0
        return arr[0] + recursion(arr[1:])

    return recursion(a)


def signs(a):
    """
    Расставьте между элементами массива a знаки отношений "меньше", "равно" или "больше"
    signs([2, 8, 4, 4]) -> [2, '<', 8, '>', 4, '=', 4]
    """
    b = []

    for i in range(1, len(a)):
        x, y = a[i-1], a[i]
        b.append(x)

        if x < y:
            b.append('<')
        elif x > y:
            b.append('>')
        else:
            b.append('=')

    b.append(a[-1])
    return b
