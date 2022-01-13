import pytest
import finish_me


larger_than_test_data = [
    ([[1, 8, 11], 4], [8, 11]),
    ([[1, 2, 3, 4, 5], 0], [1, 2, 3, 4, 5]),
    ([[1, 2, 3, 4, 5], 3], [4, 5]),
    ([[8, 800, -555, 35, 35], 0], [8, 800, 35, 35]),
]


@pytest.mark.parametrize('data', larger_than_test_data)
def test_larger_than(data):
    # noinspection PyArgumentList
    assert finish_me.larger_than(*data[0]) == data[1]


names_to_strings_test_data = [
    ([['Alice', 'John'], ['Smith', 'Doe']], ['Alice Smith', 'John Doe']),
    ([['Rob', 'Jack', 'Mike'], ['Bor', 'Kcaj', 'Ekim']], ['Rob Bor', 'Jack Kcaj', 'Mike Ekim']),
    ([[], []], [])
]


@pytest.mark.parametrize('data', names_to_strings_test_data)
def test_names_to_strings(data):
    # noinspection PyArgumentList
    assert finish_me.names_to_strings(*data[0]) == data[1]


last_first_test_data = [
    ('Hello', 'oellH'),
    ('Goodbye sweetheart', 'toodbye sweethearG'),
    ('ananas', 'snanaa'),
    ('', ''),
    ('a', 'a'),
    ('ab', 'ba')
]


@pytest.mark.parametrize('data', last_first_test_data)
def test_last_first(data):
    # noinspection PyArgumentList
    assert finish_me.last_first(data[0]) == data[1]


int_strings_test_data = [
    ([1, '2', 3, '4'], ['1', 2, '3', 4]),
    ([1, 1, 1, -211], ['1', '1', '1', '-211']),
    ([], []),
    ([44444888, '-2423'], ['44444888', -2423])
]


@pytest.mark.parametrize('data', int_strings_test_data)
def test_int_strings(data):
    # noinspection PyArgumentList
    assert finish_me.int_strings(data[0]) == data[1]


no_long_words_test_data = [
    ('Hello beautiful world', 'Hello world'),
    ('', ''),
    ('lab wab cab dab', 'lab wab cab dab'),
    ('lab wab cab dab yooooohooooo', 'lab wab cab dab'),
    ('ab mesmerizing fascinating amazing ab', 'ab ab'),
    ('Johnson is', 'is')
]


@pytest.mark.parametrize('data', no_long_words_test_data)
def test_no_long_words(data):
    # noinspection PyArgumentList
    assert finish_me.no_long_words(data[0]) == data[1]
