from io import StringIO, SEEK_END
import pytest

try:
    from helloworld2 import greetings
except ImportError:
    def greetings(*args):
        pass


def input_setup():
    count = 0
    data = ''

    def __input(prompt=None):
        nonlocal count
        count += 1
        assert prompt == 'What is your name?'
        return data

    def __setup(s):
        nonlocal count, data
        count = 0
        data = s

    def __validate():
        assert count == 1

    return __input, __setup, __validate


def print_setup():
    count = 0
    buffer = StringIO()

    def __print(*args, **kwargs):
        nonlocal count
        assert 'file' not in kwargs.keys()
        assert count == 0
        count += 1
        print(*args, **kwargs, file=buffer)

    def __setup():
        nonlocal count, buffer
        count = 0
        buffer = StringIO()

    def __get():
        assert count == 1
        return buffer.getvalue()

    return __print, __setup, __get


_input, prepare, validate = input_setup()
_print, init, get = print_setup()


test_data = [
    ('Ivan', 'Hello, Ivan!'),
    ('A', 'Hello, A!'),
    ('a', 'Hello, World!'),
    ('World', 'Hello, World!'),
    ('world', 'Hello, World!'),
    ('An ex', 'Hello, World!'),
    ('', 'Hello, World!'),
    ('BOSS', 'Hello, World!'),
    ('Xander', 'Hello, Xander!'),
    ('XanderX', 'Hello, World!')
]


@pytest.mark.parametrize('data', test_data)
def test(data):
    name, expect = data
    init()
    prepare(name)
    try:
        greetings(_input, _print)
    except (IndexError, ValueError) as e:
        pytest.fail(e)
    validate()
    assert get().strip() == expect
