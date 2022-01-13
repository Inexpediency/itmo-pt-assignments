import exercise
from pytest import mark
from common.test.run import CTEST


# @formatter:off
@mark.parametrize(
    ['input_args', 'output'],
    [
        ([ lambda x: x + 1, 1 ], 3),
        ([ str.swapcase, 'AbcD' ], 'AbcD'),
        ([ lambda x: x * x, 3 ], 81),
        ([ lambda x: f'1{x}2', '33' ], '113322'),
        ([ lambda x: str(len(x)), '1' * 100 ], '3'),
        ([ lambda x: x + 0, 0 ], 0)
    ]
)
# @formatter:on
def test_twice(input_args, output):
    CTEST(exercise.twice, input_args, output)


# @formatter:off
@mark.parametrize(
    ['input_args', 'output'],
    [
        ([ [lambda x: x, lambda x: x + 1], [1, 2] ], [1, 3]),
        ([ [lambda x: x ** x], [3] ], [27]),
        ([ [lambda x: list(sorted(x)), lambda x: list(reversed(x))], [[1, 3, 2], [1, 2, 4]] ], [[1, 2, 3], [4, 2, 1]]),
        ([ [lambda x: x + '1', lambda x: '1' + x, lambda x: f'1{x}1'], ['a', 'b', 1] ], ['a1', '1b', '111']),
        ([ [], [] ], []),
        ([ [lambda x: [x, x], lambda x: [[x]]], [[1], 2] ], [[[1], [1]], [[2]]])
    ]
)
# @formatter:on
def test_foreach(input_args, output):
    CTEST(exercise.foreach, input_args, output)


def __example(*args, **kwargs):
    def __str(x):
        return f'{str(type(x))[8]}{str(x)[0]}'

    args = list(map(__str, args))
    kwargs = list(map(lambda item: f'{str(item[0][0])}={__str(item[1])}', sorted(kwargs.items())))
    return ':'.join(args + kwargs)


# @formatter:off
@mark.parametrize(
    ['input_args', 'output'],
    [
        ([ __example, [], {} ], ''),
        ([ __example, [1, 2], {} ], 'i1:i2'),
        ([ __example, [0.12], {'alpha': 'str'} ], 'f0:a=ss'),
        ([ __example, [], {'key': (0, 1), 'value': 0} ], 'k=t(:v=i0'),
        ([ __example, [0, 1, 2, 'mode'], {'mode': 'mode'} ], 'i0:i1:i2:sm:m=sm'),
        ([ __example, ['a', 'b', 'c'], {'a': '0', 'b': 0, 'c': 0.0} ], 'sa:sb:sc:a=s0:b=i0:c=f0')
    ]
)
# @formatter:on
def test_apply(input_args, output):
    CTEST(exercise.apply, input_args, output)


def __ternary(n, d):
    """
    Даже если вы нашли эту функцию, нет, ее нельзя использовать в задании all_ternary
    Используйте рекурсию!
    """
    s = []
    for _ in range(d):
        s.append(n % 3)
        n //= 3
    return ''.join(map(str, reversed(s)))


# @formatter:off
@mark.parametrize(
    ['input_args', 'output'],
    [
        ([ 0 ], ['']),
        ([ 1 ], ['0', '1', '2']),
        ([ 2 ], ['00', '01', '02', '10', '11', '12', '20', '21', '22']),
        ([ 3 ], list(map(lambda n: __ternary(n, 3), range(3 ** 3)))),
        ([ 4 ], list(map(lambda n: __ternary(n, 4), range(3 ** 4)))),
        ([ 7 ], list(map(lambda n: __ternary(n, 7), range(3 ** 7))))
    ]
)
# @formatter:on
def test_all_ternary(input_args, output):
    CTEST(exercise.all_ternary, input_args, output)


# @formatter:off
@mark.parametrize(
    ['input_args', 'output'],
    [
        (( lambda x, y: x - y, [ 1, 2 ] ), 1),
        (( lambda x, y: x + y, [ 1, 2 ] ), 3),
        (( lambda x, y: x + y, [ [1], [2] ] ), [2, 1]),
        (( lambda x, y: x(y), [ lambda a: '1' + str(a)[0], lambda a: '2' + str(a)[0] ] ), '2<'),
        (( lambda x, y: None if x < y else '', [ 1, 2 ] ), ''),
        (( lambda x, y: x(y(0)), [ lambda x: x + 1, lambda x: x * 2 ] ), 2)
    ]
)
# @formatter:on
def test_swap_arguments(input_args, output):
    CTEST(exercise.swap_arguments(input_args[0]), input_args[1], output)
