import pytest
import lists


sum_some_test_data = [
    ([[1, 2, 3], [0, 1, 1]], 5),
    ([[2, 4, 6, 8], [0, 1, 2, 3]], 20),
    ([[2, 4, 6, 8], [0, 3]], 10),
    ([[], []], 0),
    ([[1, 2, 3], []], 0)
]


@pytest.mark.parametrize('data', sum_some_test_data)
def test_sum_some(data):
    # noinspection PyArgumentList
    assert lists.sum_some(*data[0]) == data[1]


replace_range_test_data = [
    ([[1, 2, 3, 4], [7, 8, 9], 0, 1], [7, 8, 9, 3, 4]),
    ([[1, 2, 3, 4], [], 0, 1], [3, 4]),
    ([[1, 2, 3, 4], [7], 0, 0], [7, 2, 3, 4]),
    ([[1, 2], [7, 7, 7, 7], 0, 1], [7, 7, 7, 7])
]


@pytest.mark.parametrize('data', replace_range_test_data)
def test_replace_range(data):
    # noinspection PyArgumentList
    assert lists.replace_range(*data[0]) == data[1]


sum_list_test_data = [
    ([1, 2, 3], 6),
    ([1, 1, 1, 1], 4),
    ([8], 8),
    ([], 0),
    ([-1, 1, -2, 2], 0)
]


@pytest.mark.parametrize('data', sum_list_test_data)
def test_sum_list(data):
    # noinspection PyArgumentList
    assert lists.sum_list(data[0]) == data[1]


signs_test_data = [
    ([2, 8, 4, 4], [2, '<', 8, '>', 4, '=', 4]),
    ([1, 1], [1, '=', 1]),
    ([1, 2, 3], [1, '<', 2, '<', 3]),
    ([-300, -200, -100], [-300, '<', -200, '<', -100])
]


@pytest.mark.parametrize('data', signs_test_data)
def test_signs(data):
    # noinspection PyArgumentList
    assert lists.signs(data[0]) == data[1]
