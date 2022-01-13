import pytest
import numeric

triangle_test_data = [
    ((1, 2, 3), False),
    ((7, 5, 2), False),
    ((3, 1, 1), False),
    ((4.5, 8.2, 3.7), False),
    ((4.5, 8.1, 7.3), True),
    ((0.1, 0.2, 0.3), True),
    ((2, 2, 3), True),
    ((1, 2, 3 - 1e-10), True)
]


@pytest.mark.parametrize('data', triangle_test_data)
def test_triangle(data):
    # noinspection PyArgumentList
    assert numeric.triangle(*data[0]) == data[1]


divide_test_data = [
    ((1, 1), 1),
    ((7, 2), 6),
    ((1000000, 1), 1000000),
    ((239, 74), 222),
    ((2729, 13), 2717),
    ((100, 100), 100),
    ((100, 101), 0),
    ((1023, 512), 512)
]


@pytest.mark.parametrize('data', divide_test_data)
def test_divide(data):
    # noinspection PyArgumentList
    assert numeric.divide(*data[0]) == data[1]


add_float_test_data = [
    ((0.1, 0.2), 0.3),
    ((0.1, 0.5), 0.6),
    ((7.7, 3.3), 11.0),
    ((99.9, 117.7), 217.6),
    ((-0.1, 0.2), 0.1),
    ((-0.3, 0.2), -0.1),
    ((-100.8, 101.7), 0.9),
    ((-0.1, 2e100 + 0.3), 2e100 + 0.2)
]


@pytest.mark.parametrize('data', add_float_test_data)
def test_add_float(data):
    # noinspection PyArgumentList
    assert numeric.add_float(*data[0]) == data[1]


distance_test_data = [
    ((1, 2), 1),
    ((2 ** 100 - 1, 2 ** 100 + 2 ** 50), 2 ** 50 + 1),
    ((6, 2), 4),
    ((99, -1e10 - 1), 1e10 + 100),
    ((0, 0), 0),
    ((-200, -200), 0),
    ((-199, -1), 198),
    ((-1e100, 1e100), 2e100)
]


@pytest.mark.parametrize('data', distance_test_data)
def test_distance(data):
    # noinspection PyArgumentList
    assert numeric.distance(*data[0]) == data[1]


compare_power_test_data = [
    ((0.1, 0.2, 0.2, 0.1), -1),
    ((3, 19, 10, 9), 1),
    ((2, 100, 10, 30), 1),
    ((1, 0.013, 1, 67.4378), 0),
    ((19, 27, 2, 114.69404286297681), -1),
    ((8, 137, 4, 205.5), 0),
    ((4, 4, 2, 8.0000001), -1),
    ((1.87381742, 11, 10, 3), -1)
]


@pytest.mark.parametrize('data', compare_power_test_data)
def test_compare_power(data):
    # noinspection PyArgumentList
    assert numeric.compare_power(*data[0]) == data[1]
