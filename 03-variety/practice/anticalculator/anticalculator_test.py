import pytest
import anticalculator


anti_calculate_test_data = [
    (10, 2),
    (0, 1),
    (25, 3),
    (25, 4),
    (11, 5),
    (173, 0),
    (173, 4)
]


@pytest.mark.parametrize('data', anti_calculate_test_data)
def test_anti_calculate(data):
    # noinspection PyArgumentList
    output = anticalculator.anti_calculate(*data)
    assert eval(output) == data[0]
    assert output.count('+') + output.count('-') + output.count('*') == data[1]

