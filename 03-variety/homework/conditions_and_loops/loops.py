def is_increasing(a):
    """
    Вернуть True, если элементы массива строго возрастают, и False иначе
    is_increasing([1, 2, 6, 10]) -> True
    """
    for i in range(0, len(a)-1):
        if a[i] >= a[i+1]:
            return False
    return True


def twice_as_much(a):
    """
    Вернуть массив, каждый элемент которого в два раза больше соответствующего элемента из a
    twice_as_much([1, 'ab']) -> [2, 'abab']
    """
    return [2*b for b in a]


def count_oddity(a):
    """
    Вернуть пару из двух элементов - количество четных и количество нечетных элементов a
    count_oddity([1, 2, 3, 5]) -> (1, 3)
    """
    even, odd = 0, 0
    for i in a:
        if i % 2 == 1:
            odd += 1
        else:
            even += 1
    return even, odd

def pick_until(a, stop):
    """
    Вернуть начало массива a, взятое до момента, когда в a встречается stop
    pick_until([1, 2, 7, 1, 4, 3], 4) -> [1, 2, 7, 1]
    """
    b = []
    for x in a:
        if x == stop:
            break
        b.append(x)
    return b


def sum_until(a, stop):
    """
    Вернуть максимальную сумму первых элементов массива a, не превосходящую stop
    sum_until([1, 2, 7, 1, 4, 3], 13) -> 11 = (1+2+7+1)
    """
    result = 0
    for el in a:
        if result + el > stop:
            return result
        result += el
    return result
