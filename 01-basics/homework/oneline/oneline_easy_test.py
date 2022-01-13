import pytest
from inspect import getmembers, isfunction, getsource
import oneline_easy
from io import StringIO


def test_no_new_functions():
    fs = getmembers(oneline_easy, isfunction)
    assert set(map(lambda x: x[0], fs)) == {'square_sum', 'print_dividing', 'shuffle_lists'}


@pytest.mark.parametrize('f', [
    oneline_easy.square_sum,
    oneline_easy.print_dividing,
    oneline_easy.shuffle_lists
])
def test_one_line(f):
    source = [x.strip() for x in getsource(f).split('\n') if len(x.strip()) > 0]
    code = [line for line in source if not line.startswith(f'def {f.__name__}') and not line.startswith('"""')]
    assert len(code) == 1


square_sum_test_data = [
    ([1, 2, 3, 4], 30),
    ([], 0),
    ([-10], 100),
    ([2 ** i for i in range(10)], (2 ** 20 - 1) // 3),
    ([3, 4], 25),
    ([0.5, 0.5, 0.5, -0.5], 1.0)
]


@pytest.mark.parametrize('data', square_sum_test_data)
def test_square_sum(data):
    assert oneline_easy.square_sum(data[0]) == data[1]


def print_setup():
    buffer = StringIO()

    def __print(*args, **kwargs):
        assert 'file' not in kwargs.keys()
        print(*args, **kwargs, file=buffer)

    def __setup():
        nonlocal buffer
        buffer = StringIO()

    def __get():
        return buffer.getvalue()

    return __print, __setup, __get


_print, init, get = print_setup()

print_dividing_test_data = [
    ([10, 20, 2], '10 12 14 16 18 20'),
    ([1, 1, -1], '1'),
    ([1, 5, 2], '2 4'),
    ([-99, 98, 33], '-99 -66 -33 0 33 66'),
    ([100, 197, 99], ''),
    ([-1000, -401, 100], '-1000 -900 -800 -700 -600 -500')
]


@pytest.mark.parametrize('data', print_dividing_test_data)
def test_print_dividing(data):
    init()
    # noinspection PyArgumentList
    oneline_easy.print_dividing(*data[0], _print)
    try:
        s = get()
        if s.endswith('\n'):
            s = s[:-1]
        assert s == data[1]
    except ValueError as e:
        pytest.fail(e)


shuffle_lists_test_data = [
    (([], []), []),
    (([1], [2]), [1, 2]),
    ((list(range(1, 10, 2)), list(range(2, 11, 2))), list(range(1, 11))),
    (([-1, 1, -1], [1, -1, 1]), [-1, 1, 1, -1, -1, 1]),
    (([[['']], []], [(1,), (2, 3)]), [[['']], (1,), [], (2, 3)]),
    ((['', 0], [0, 1]), ['', 0, 0, 1])
]


@pytest.mark.parametrize('data', shuffle_lists_test_data)
def test_shuffle_lists(data):
    assert oneline_easy.shuffle_lists(*data[0]) == data[1]
