def read_all(filename):
    """Вернуть содержимое текстового файла filename как строку."""
    with open(filename, 'r+', encoding='utf-8') as file:
        string = file.read()

        return string


def sum_two(filename):
    """Прочитать первые два числа из текстового файла и вернуть их сумму."""
    with open(filename, 'r+', encoding='utf-8') as file:
        string = file.read()
        numbers = string.split()

        return int(numbers[0]) + int(numbers[1])


def longest_line(filename):
    """Вернуть номер самой длинной строки текстового файла. Нумерация начинается с единицы."""
    with open(filename, 'r+', encoding='utf-8') as file:
        lines = file.readlines()
        s, k = '', 1

        for i in range(len(lines)):
            if len(s) < len(lines[i]):
                k = i + 1
                s = lines[i]

        return k


def random_access(filename, n):
    """Вернуть n-ый символ текстового файла. Нумерация с единицы"""
    with open(filename, 'r+', encoding='utf-8') as file:
        text = ''.join(file.readlines())

        if 0 <= n - 1 <= len(text) and text != '':
            return text[n-1]

        return ''


def alphabet(filename, n):
    """Вывести n первых заглавных букв латинского алфавита в текстовый файл."""
    alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    with open(filename, 'w+', encoding='utf-8') as file:
        file.write(alph[:n])
