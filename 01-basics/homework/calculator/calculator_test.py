import pytest
import calculator

calculator_test_data = [
    ('2 + 2', 4),
    ('2 + 2 * 2', 6),
    ('1 - 100 / 10 * 5', -49),
    ('0.1 * 0.1', 0.01),
    ('0.25 / 4', 0.06),
    ('1 + 1 + 100 / 100 + 1 + 1 + 1.1 + 1 + 1 * 250 + 1 + 1 + 1', 260.1),
    ('121', 121),
    ('11 - 0.000001', 11)
]


@pytest.mark.parametrize('data', calculator_test_data)
def test_calculate(data):
    # noinspection PyArgumentList
    assert calculator.calculate(data[0]) == data[1]
