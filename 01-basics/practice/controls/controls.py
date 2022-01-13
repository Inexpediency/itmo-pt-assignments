import math


def transpose(a):
    """Транспозиция матрицы"""

    aT = []

    for i in range(0, len(a[0])):
        aT.append(list())

        for j in range(0, len(a)):
            aT[i].append(a[j][i])

    return aT


def read_lines(input, print):
    """Количество непустых строк во вводе до первой пустой"""

    count = 0

    while True:
        inp = input()

        if inp != '':
            count += 1

        else:
            break

    print(count)


def min_prime(n):
    """Минимальный простой делитель числа"""

    def isPrime(x):
        flag = True
        sqrtX = round(x ** 0.5)

        if (sqrtX ** 2 == x) or (x % 2 == 0):
            return False

        else:
            for i in range(3, sqrtX, 2):
                if flag == False:
                    break

                if (x % i == 0):
                    flag = False

        return flag

    primes = [2] + [i for i in range(3, n + 1, 1) if isPrime(i)]

    for num in primes:
        if n % num == 0:
            return num


def from_hexadecimal(s):
    """Перевод из шестнадцатеричной системы счисления"""

    values = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

    rev_s = s[::-1]
    s10 = 0

    for i in range(0, len(rev_s), 1):
        elem = rev_s[i]

        if elem.isdigit():
            elem = int(elem)

        else:
            elem = values[elem]

        s10 += elem * (16 ** i)

    return s10
