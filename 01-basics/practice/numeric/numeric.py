import math


def triangle(a, b, c):
    """Проверка правила треугольника"""

    sides = list(map(float, [a, b, c]))
    flag = True

    statement = lambda side1, side2, side3: side1 < side2 + side3
    for side in sides:
        if not flag:
            break

        new = sides.copy()
        new.remove(side)
        flag = statement(side, new[0], new[1])

    return flag


def divide(n, k):
    """Разбиение на равные части"""

    return (n // k) * k


def add_float(x, y):
    """Сложение не более, чем десятичных, дробных чисел"""

    return (10 * x + 10 * y) / 10


def distance(x1, x2):
    """Расстояние между точками"""
    
    if (x1 >= 0 and x2 >= 0) or (x1 <= 0 and x2 <= 0):
        return abs(abs(x1) - abs(x2))

    else:
        return abs(abs(x1) + abs(x2))


def compare_power(x1, d1, x2, d2):
    """Сравнение степеней"""
    
    minus = x1 ** d1 - x2 ** d2
    eps = 1e-6

    if abs(minus) < eps:
        return 0

    elif minus < 0:
        return -1
    
    else:
        return 1



