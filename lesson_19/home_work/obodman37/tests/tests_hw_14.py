import pytest

@pytest.mark.parametrize("a, b, expected_result", [
    (2, 3, 6),
    (-2, -2, 4),
    (0, 0, 0),
    (1.1, 1.1, 1.21),
    (1, 5, 5),
    (5, 0, 0)
])
def test_mult_functionality(calc, a, b, expected_result):
    result = calc.mult(a, b)
    assert round(result, 10) == round(expected_result, 10)


@pytest.mark.parametrize("a, b, expected_result", [
    (6, 3, 2),
    (-2, -2, 1),
    (0, 5, 0),
    (1.1, 1.1, 1.0),
    (5, 2, 2.5),
    (10, 3, 3.3333333333333335)
])
def test_div_functionality(calc, a, b, expected_result):
    if b == 0:
        with pytest.raises(ZeroDivisionError):
            calc.div(a, b)
    else:
        result = calc.div(a, b)
        assert result == expected_result


@pytest.mark.parametrize("a, b, expected_result", [
    (6, 3, 3),
    (-2, -2, 0),
    (0, 5, -5),
    (1.1, 1.1, 0.0),
    (5, 2, 3),
    (10, 3, 7)
])
def test_subtract_functionality(calc, a, b, expected_result):
    result = calc.substract(a, b)
    assert result == expected_result


@pytest.mark.parametrize("a, b, expected_result", [
    (2, 3, 8),
    (-2, 2, 4),
    (0, 0, 1.0),
    (1.1, 1.1, 1.12),
    (5, 2, 25),
    (10, 3, 1000)
])
def test_power_functionality(calc, a, b, expected_result):
    result = calc.power(a, b)
    assert round(result, 1) == round(expected_result, 1)


@pytest.mark.parametrize("a, expected_result", [
    (4, 2),
    (-4, ValueError),
    (0, 0.0),
    (1.21, 1.1),
    (10000, 100)
])
def test_square_root_functionality(calc, a, expected_result):
    if a < 0:
        with pytest.raises(ValueError):
            calc.square_root(a)
    else:
        result = calc.square_root(a)
        assert result == expected_result