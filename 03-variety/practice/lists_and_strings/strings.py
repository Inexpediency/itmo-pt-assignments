def reverse(s):
    """
    Вернуть исходную строку, записанную наоборот
    reverse('abc') -> 'cba'
    """
    return s[::-1]


def swap_case(s):
    """
    Заменить регистр каждого символа, входящего в строку, на противоположный
    swap_case('Hello world') -> 'hELLO WORLD'
    """
    return ''.join([a if not a.isalpha() else a.lower() if a.isupper() else a.upper() for a in s])


def censor_words(s, blacklist):
    """
    Вернуть исходную строку, в которой слова из blacklist заменены на звездочки
    censor_words('hello world', ['hello']) -> '***** world')
    """
    return ' '.join([w if w not in blacklist else '*' * len(w) for w in s.split(' ')])


def remove_duplicates(s):
    """
    Удалить идущие подряд повторы слов в строке
    remove_duplicates('hello nice nice world hello') -> 'hello nice world hello'
    """
    a = s.split(' ')
    b = [a[0]]

    for i in range(1, len(a)):
        if a[i] != a[i-1]:
            b.append(a[i])

    return ' '.join(b)


def parentheses(s):
    """
    Проверить, закрыты ли все пары круглых скобок в строке
    parentheses( '(abc(1+2))' )    -> True
    parentheses( '(lalala' )       -> False - скобка не закрыта
    parentheses( '(hello)world)' ) -> False - слишком много закрывающих скобок
    """

    a = ''.join([a for a in s if a in ('(', ')')])

    while '()' in a:
        a = a.replace('()', '')

    return a == ''
