def square_sum(a):
    """Сумма квадратов элементов"""
<<<<<<< HEAD
    return sum(map(lambda i: i * i, a))
=======

    return sum(list(b ** 2 for b in a))
>>>>>>> origin/practice


def print_dividing(a, b, t, print):
    """Все числа от a до b, делящиеся на t, через пробел"""
<<<<<<< HEAD
    print(' '.join([str(i) for i in range(a, b + 1) if i % t == 0]))
=======

    print(' '.join(list(str(c) for c in range(a, b + 1, 1) if c % t == 0)))
>>>>>>> origin/practice


def shuffle_lists(a, b):
    """Перемешать массивы в порядке чередования"""
<<<<<<< HEAD
    return [i for kek in zip(a, b) for i in kek]


# print([ i for i in range(30) if i % 7 == 0 ])
#
# new_list = []
# for i in range(30):
#     if i % 7 == 0:
#         new_list.append(i)
# print(new_list)
=======

    return list(a[i//2] if i % 2 == 0 else b[(i-1)//2] for i in range(2 * len(a)))
>>>>>>> origin/practice
