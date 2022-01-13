import pytest
import structures

kth_test_data = [
    (([4, 1, 17], 2), 4),
    (([4, 17, 1], 3), 17),
    (([-100], 1), -100),
    (([2, 2, 8, 1, 1, 7], 4), 2),
    ((list(set(range(1000))), 239), 238),
    (([(1, 2), (2, 1), (2, 0)], 2), (2, 0)),
    ((['10', '1', '2'], 2), '10'),
    (([[1, 2], [2, 1], [2, 0]], 2), [2, 0])
]


@pytest.mark.parametrize('data', kth_test_data)
def test_kts(data):
    # noinspection PyArgumentList
    assert structures.kth(*data[0]) == data[1]


head_tail_test_data = [
    (([1, 2, 3, 4, 5], 2), [1, 2, 4, 5]),
    (([1, 2, 3], 2), [1, 2, 2, 3]),
    (([10000], 1), [10000, 10000]),
    (([10, 8, 2], 0), []),
    (([1, 1, 2], 3), [1, 1, 2, 1, 1, 2]),
    ((list(range(100)), 33), list(range(33)) + list(range(67, 100))),
    (([[], []], 1), [[], []]),
    (([], 0), [])
]


@pytest.mark.parametrize('data', head_tail_test_data)
def test_head_tail(data):
    # noinspection PyArgumentList
    assert structures.head_tail(*data[0]) == data[1]


filter_sort_test_data = [
    ((['ava', 'xab', 'aboba'], 'x'), ['aboba', 'ava']),
    (([], 'x'), []),
    ((['', 'xx', 'Abab', 'xa'], 'A'), ['', 'xa', 'xx']),
    ((['c', 'b', 'a', 'e', 'd'], 'f'), ['a', 'b', 'c', 'd', 'e']),
    ((['x', 'alex', 'axe', 'xxx'], 'x'), []),
    ((['x y z', 'zz', 'xx', ''], 'z'), ['', 'xx']),
    ((['597', ' ', 'x y', '5 9 7', '87'], ' '), ['597', '87']),
    ((['a1', 'a2', 'a0'], 'A'), ['a0', 'a1', 'a2'])
]


@pytest.mark.parametrize('data', filter_sort_test_data)
def test_filter_sort(data):
    # noinspection PyArgumentList
    assert structures.filter_sort(*data[0]) == data[1]


build_dict_test_data = [
    ((['a', 'b', 'c'], (1, 2, 3)), {'a': 1, 'b': 2, 'c': 3}),
    (([], []), {}),
    (([(0, 1)], [[3, 3]]), {(0, 1): [3, 3]}),
    ((['a', 'a'], ['b', 'c']), {'a': 'c'}),
    (([0, 1, 2], [2, 1, 0]), {2: 0, 1: 1, 0: 2}),
    (([1] * 1000, list(range(1000))), {1: 999}),
    (([(), (1,), (1, 2)], [1, 1, 1]), {(): 1, (1,) : 1, (1, 2): 1}),
    (([0.1, 0.1 + 0.2], [1, 3]), {0.1: 1, 0.1 + 0.2: 3})
]


@pytest.mark.parametrize('data', build_dict_test_data)
def test_distance(data):
    # noinspection PyArgumentList
    assert structures.build_dict(*data[0]) == data[1]


compare_contents_test_data = [
    (([0, 1, 2], [2, 0, 1]), True),
    (([1, 2, 2], [2, 1, 1]), True),
    (([0, 1], [0, 0, 0, 1, 1, 1, 2]), False),
    (([], []), True),
    (([0, 0, 0, 0], [0]), True),
    (([()], [(), ()]), True),
    (([1, id(1)], [id(2), 1]), False),
    (([3, 2, 1, 4, 0], list(range(5)) * 1000), True)
]


@pytest.mark.parametrize('data', compare_contents_test_data)
def test_compare_contents(data):
    # noinspection PyArgumentList
    assert structures.compare_contents(*data[0]) == data[1]
