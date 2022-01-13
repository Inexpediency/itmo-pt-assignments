import pytest
from inspect import getmembers, isfunction, getsource
import oneline_hard
from io import StringIO


def test_no_new_functions():
    fs = getmembers(oneline_hard, isfunction)
    assert set(map(lambda x: x[0], fs)) == {'increase_ints', 'weird_condition', 'index_of_median'}


@pytest.mark.parametrize('f', [
    oneline_hard.increase_ints,
    oneline_hard.weird_condition,
    oneline_hard.index_of_median
])
def test_one_line(f):
    source = [x.strip() for x in getsource(f).split('\n') if len(x.strip()) > 0]
    code = [line for line in source if not line.startswith(f'def {f.__name__}') and not line.startswith('"""')]
    assert len(code) == 1


increase_ints_test_data = [
    (set(), set()),
    ({1, 2}, {2, 3}),
    ({0, 1, '0.1', '12', 0.2}, {1, 2, '0.1', '12', 0.2}),
    ({(1, 2)}, {(1, 2)}),
    ({3.0, 4}, {3.0, 5}),
    ({(1, 2), 3.0, '10'}, {(1, 2), 3.0, '10'})
]


@pytest.mark.parametrize('data', increase_ints_test_data)
def test_increase_ints(data):
    assert oneline_hard.increase_ints(data[0]) == data[1]


weird_condition_test_data = [
    (([2, 6, 10], [3, 12, 6], 2, 3, 5), True),
    (([2, 6, 10], [3, 12, 6], 2, 3, 4), True),
    (([], [3, 12, 6], 100, 3, 3), True),
    (([2, 6, 10], [], 2, 99, 2), True),
    (([], [], 17, 70, 13), True),
    (([2, 6, 10, 15], [3, 12, 6], 2, 3, 5), False),
    (([2, 6, 10], [3, 12, 6, 8], 2, 3, 5), False),
    (([2, 6, 10], [3, 12, 6], 2, 3, 6), False),
    (([], [3, 12, 6], 2, 6, 1), False),
    (([44, 2, 8, 12, 24], [3, 12, 15, 6], 2, 3, 6), False)
]


@pytest.mark.parametrize('data', weird_condition_test_data)
def test_weird_condition(data):
    assert oneline_hard.weird_condition(*data[0]) == data[1]


index_of_median_test_data = [
    ([1], 0),
    ([3, 1, 2], 2),
    (list(range(1001)), 500),
    ([100, 10, 9, -4, 17, 23, -133], 1),
    ([1, 2, 3, 4, -1, -2, -3, -4, -5], 4),
    ([10 ** 21, 10 ** 20, -1, 0, -2], 3)
]


@pytest.mark.parametrize('data', index_of_median_test_data)
def test_index_of_median(data):
    assert oneline_hard.index_of_median(data[0]) == data[1]
