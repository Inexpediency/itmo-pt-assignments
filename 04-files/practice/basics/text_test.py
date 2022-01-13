import pytest
import os
import text

read_all_data = [
    ('test.txt', 'Lalala'),
    ('hello.txt', 'Hello world!'),
    ('hello.txt', 'Some other text!  '),
    ('multiline', 'One\nTwo\nThree')
]


@pytest.mark.parametrize('data', read_all_data)
def test_read_all(data):
    # noinspection PyArgumentList
    try:
        with open(data[0], 'w') as file:
            file.write(data[1])
        assert text.read_all(data[0]) == data[1]
    except Exception as e:
        pytest.fail(str(e))
    finally:
        if os.path.exists(data[0]):
            os.remove(data[0])


sum_two_data = [
    (('nums.txt', '1 2'), 3),
    (('nums.txt', '1 2 3'), 3),
    (('nums.txt', '20000 450'), 20450),
    (('numbers.txt', '-1 3 5 22 100 251 400 416'), 2)
]


@pytest.mark.parametrize('data', sum_two_data)
def test_sum_two(data):
    # noinspection PyArgumentList
    try:
        with open(data[0][0], 'w') as file:
            file.write(data[0][1])
        assert text.sum_two(data[0][0]) == data[1]
    except Exception as e:
        pytest.fail(str(e))
    finally:
        if os.path.exists(data[0][0]):
            os.remove(data[0][0])


longest_line_data = [
    ('test.txt', 'ab', 1),
    ('test.txt', 'ab\ncd', 1),
    ('test.txt', 'ab\ncd\nefgh', 3),
    ('test2.txt', 'Hello world!\nOh no??\n\nLalalalalalalalalalalalalala\n\n', 4),
    ('whynot', '\n\n\n\n\n\n', 1),
    ('empty.txt', '', 1)
]


@pytest.mark.parametrize('data', longest_line_data)
def test_longest_line(data):
    # noinspection PyArgumentList
    try:
        with open(data[0], 'w') as file:
            file.write(data[1])
        assert text.longest_line(data[0]) == data[2]
    except Exception as e:
        pytest.fail(str(e))
    finally:
        if os.path.exists(data[0]):
            os.remove(data[0])


random_access_data = [
    ('test.txt', 'Very nice\nand fun', 7, 'i'),
    ('test.txt', 'Very nice\nand fun', 13, 'd'),
    ('test.txt', 'Very nice\nand fun', 100000, ''),
    ('test.txt', 'Very nice\nand fun', -1, ''),
    ('test.txt', 'Very nice\nand fun', 0, ''),
    ('test.txt', '', 1, ''),
    ('test.txt', 'Hello world', 3, 'l')
]


@pytest.mark.parametrize('data', random_access_data)
def test_random_access(data):
    # noinspection PyArgumentList
    try:
        with open(data[0], 'w') as file:
            file.write(data[1])
        assert text.random_access(data[0], data[2]) == data[3]
    except Exception as e:
        pytest.fail(str(e))
    finally:
        if os.path.exists(data[0]):
            os.remove(data[0])


alphabet_data = [
    ('test.txt', False, 6, 'ABCDEF'),
    ('test.txt', True, 6, 'ABCDEF'),
    ('aaa.txt', False, 1, 'A'),
    ('abc.txt', False, 15, 'ABCDEFGHIJKLMNO'),
    ('abc.txt', False, 26, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
]


@pytest.mark.parametrize('data', alphabet_data)
def test_alphabet(data):
    # noinspection PyArgumentList
    try:
        if data[1]:
            with open(data[0], 'w') as file:
                file.write('FSGSDFGDSGSADFSADFAFDASFDSADF')
        text.alphabet(data[0], data[2])
        with open(data[0], 'r') as file:
            assert file.read() == data[3]
    except Exception as e:
        pytest.fail(str(e))
    finally:
        if os.path.exists(data[0]):
            os.remove(data[0])
