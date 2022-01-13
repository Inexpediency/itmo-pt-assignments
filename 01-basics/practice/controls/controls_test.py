import pytest
import controls
from io import StringIO

transpose_test_data = [
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 4, 7], [2, 5, 8], [3, 6, 9]]),
    ([[1, 2, 3]], [[1], [2], [3]]),
    ([[1]], [[1]]),
    ([[1, 2, 3], [4, 5, 6]], [[1, 4], [2, 5], [3, 6]])
]


@pytest.mark.parametrize('data', transpose_test_data)
def test_transpose(data):
    # noinspection PyArgumentList
    assert controls.transpose(data[0]) == data[1]


def input_setup():
    last = 0
    data = []

    def __input(prompt=None):
        nonlocal last
        assert last < len(data)
        last += 1
        return data[last - 1]

    def __setup(s):
        nonlocal last, data
        last = 0
        data = s

    return __input, __setup


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


_input, prepare = input_setup()
_print, init, get = print_setup()

read_lines_test_data = [
    (['da', 'dds sdad', '  ', ''], 3),
    ([''], 0),
    (['abacaba sss aA', 'd', ' ', '.', ''], 4),
    (['x'] * 1000 + [''], 1000)
]


@pytest.mark.parametrize('data', read_lines_test_data)
def test_read_lines(data):
    # noinspection PyArgumentList
    prepare(data[0])
    init()
    controls.read_lines(_input, _print)
    try:
        assert int(get()) == data[1]
    except ValueError as e:
        pytest.fail(e)


min_prime_test_data = [
    (2 * 3 * 7 * 13, 2),
    (7 * 13 * 13, 7),
    (2 ** 12, 2),
    (5 ** 3 * 239, 5),
    (239, 239),
    (239 * 241, 239)
]


@pytest.mark.parametrize('data', min_prime_test_data)
def test_min_prime(data):
    # noinspection PyArgumentList
    assert controls.min_prime(data[0]) == data[1]


from_hexadecimal_test_data = [
    ('A', 10),
    ('0', 0),
    ('97', 9 * 16 + 7),
    ('FFFFFFE', 16 ** 7 - 2),
    ('ABA7ABA', (10 + 11 * 16 + 10 * 16 ** 2) * (1 + 16 ** 4) + 7 * 16 ** 3),
    ('99', 9 * 17),
    ('2F', 47),
    ('1' * 100, (16 ** 100 - 1) // 15)
]


@pytest.mark.parametrize('data', from_hexadecimal_test_data)
def test_from_hexadecimal(data):
    # noinspection PyArgumentList
    assert controls.from_hexadecimal(data[0]) == data[1]