import pytest
import strings


reverse_test_data = [
    ('abc', 'cba'),
    ('ok', 'ko'),
    ('', ''),
    ('n', 'n'),
    ('abyyba', 'abyyba'),
    ('Hello world', 'dlrow olleH')
]


@pytest.mark.parametrize('data', reverse_test_data)
def test_reverse(data):
    # noinspection PyArgumentList
    assert strings.reverse(data[0]) == data[1]


swap_case_test_data = [
    ('Hello world', 'hELLO WORLD'),
    ('', ''),
    ('e', 'E'),
    ('John Doe', 'jOHN dOE'),
    ('VeRyNiCe', 'vErYnIcE'),
    ('hi123', 'HI123')
]


@pytest.mark.parametrize('data', swap_case_test_data)
def test_swap_case(data):
    # noinspection PyArgumentList
    assert strings.swap_case(data[0]) == data[1]


censor_words_test_data = [
    (['hello world', ['hello']], '***** world'),
    (['Java is better than Python', ['Java']], '**** is better than Python'),
    (['Programming is fun', ['fun']], 'Programming is ***'),
    (['This tree is beautiful and green', ['tree', 'green']], 'This **** is beautiful and *****'),
    (['Nothing special', ['Alabama']], 'Nothing special'),
    (['Something special', ['Something', 'better']], '********* special'),
    (['wow Wow WOW', ['wow']], '*** Wow WOW')
]


@pytest.mark.parametrize('data', censor_words_test_data)
def test_censor_words(data):
    # noinspection PyArgumentList
    assert strings.censor_words(*data[0]) == data[1]


remove_duplicates_test_data = [
    ('hello nice nice world hello', 'hello nice world hello'),
    ('very good', 'very good'),
    ('hehe hehe', 'hehe'),
    ('cows cows cows cows cows', 'cows'),
    ('cows & cows & cows & cows', 'cows & cows & cows & cows'),
    ('cows&cows&cows&cows', 'cows&cows&cows&cows')
]


@pytest.mark.parametrize('data', remove_duplicates_test_data)
def test_remove_duplicates(data):
    # noinspection PyArgumentList
    assert strings.remove_duplicates(data[0]) == data[1]


parentheses_test_data = [
    ('(abc(1+2))', True),
    ('(lalala', False),
    ('(hello)world)', False),
    ('((()))', True),
    ('()()()', True),
    ('(what (is) this?)', True),
    ('(what (is) this?', False),
    (')(', False)
]


@pytest.mark.parametrize('data', parentheses_test_data)
def test_parentheses(data):
    # noinspection PyArgumentList
    assert strings.parentheses(data[0]) == data[1]
