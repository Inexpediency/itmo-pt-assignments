def bin_sum_two(filename):
    """
    Из бинарного файла filename прочитать два первых числа и вернуть их сумму.
    Оба числа имеют тип int и закодированы строго четырьмя байтами.
    """
    with open(filename, 'rb+') as file:
        x = int.from_bytes(file.read(4), byteorder='big', signed=True)
        y = int.from_bytes(file.read(4), byteorder='big', signed=True)
        return x + y


def find_person(filename, identifier):
    """Найти человека по id в базе указанной структуры (см. _legend.md)"""
    with open(filename, 'rb+') as file:
        k = int.from_bytes(file.read(4), byteorder='big', signed=True)
        for _ in range(k):
            user_id = int.from_bytes(file.read(4), byteorder='big', signed=True)
            n = int.from_bytes(file.read(4), byteorder='big', signed=True)
            string = file.read(n).decode('utf-8')

            if user_id == identifier:
                return string
