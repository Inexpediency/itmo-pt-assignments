import conditions
from pytest import mark


@mark.parametrize('data', [
    [[1, 2, 3], 2],
    [[3, 2, 1], 2],
    [[1, 3, 2], 2],
    [[1, 0, 0], 0],
    [[0, 1, 0], 0],
    [[1, 1, 0], 1],
    [[7, 7, 7], 7]
])
def test_median(data):
    assert conditions.median(*data[0]) == data[1]


@mark.parametrize('data', [
    [[[], 0], None],
    [[[], 1], None],
    [[[], -1], None],
    [[[1], 0], 1],
    [[[1], 1], None],
    [[[1], -1], 1],
    [[[1], -2], None],
    [[[1, 4, 3, 2], 0], 1],
    [[[1, 4, 3, 2], 1], 4],
    [[[1, 4, 3, 2], -1], 2],
    [[[1, 4, 3, 2], -2], 3],
    [[[1, 4, 3, 2], 4], None],
    [[[1, 4, 3, 2], -4], 1],
    [[[1, 4, 3, 2], -5], None],
    [[[1, 4, None, 2], 2], None],
])
def test_get_or_none(data):
    assert conditions.get_or_none(*data[0]) == data[1]


@mark.parametrize('data', [
    [0, False],
    [1, True],
    [2, True],
    [3, False],
    [4, True],
    [5, False],
    [6, False],
    [7, False],
    [8, True],
    [9, False],
    [2 ** 100, True],
    [2 ** 100 - 1, False],
    [2 ** 100 + 1, False],
    [-2 ** 100, False],
])
def test_is_power_of_two(data):
    assert conditions.is_power_of_two(data[0]) == data[1]


@mark.parametrize('data', [
    [[-1, 2, 3], True],
    [[1, 2, 2], False],
    [[2, 2, 3], False],
    [[3, 2, -1], True],
    [[3, 2, 2], False],
    [[2, 0, 0], False],
    [[7, 7, 7], False],
    [[8, 7, 9], False],
    [[4, 7, 6], False],
    [[1, 7, -3], False],
])
def test_is_monotonic(data):
    assert conditions.is_monotonic(*data[0]) == data[1]


@mark.parametrize('data', [
    [[0, 0, True], 0],
    [[0, 0, False], 0],
    [['x', 'y', True], 'x'],
    [['x', 'y', False], 'y'],
    [[10 ** 10, 'xyz', True], 10 ** 10],
    [[10 ** 10, 'xyz', False], 'xyz'],
])
def test_inline_if(data):
    assert conditions.inline_if(*data[0]) == data[1]
