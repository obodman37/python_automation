import unittest
from app.calc import Calculator
from parameterized import parameterized


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    @parameterized.expand([
        ('Division negative number', 6, -3, -2.0),
        ('Division zero', -2, 0, ZeroDivisionError),
        ('Division float by int', 5.0, 2, 2.5),
        ('Division number by one', 0, 5, 0.0),
    ])

    def test_div_functionality(self, _, a, b, expected_result):
        if b == 0:
            with self.assertRaises(expected_result):
                self.calc.div(a, b)
        else:
            self.assertEqual(self.calc.div(a, b), expected_result)

    @parameterized.expand([
        ('Mult floats', 2.1, 6, 12.6),
        ('Mult negative numbers', -3, -5, 15),
        ('Mult number by one', 7, 1, 7),
        ('Mult number by zero', 7, 0, 0),
    ])
    def test_mult_functionality(self, _, a, b, expected_result):
        self.assertEqual(round(self.calc.mult(a, b), 1), expected_result)

    @parameterized.expand([
        ('Subtract positive numbers', 8, 3, 5),
        ('Subtract negative numbers', -5, -3, -2),
        ('Subtract number from zero', 0, 6, -6),
        ('Subtract zero from number', 5, 0, 5),
    ])
    def test_subtract_functionality(self, _, a, b, expected_result):
        self.assertEqual(self.calc.substract(a, b), expected_result)

    @parameterized.expand([
        ('Power positive numbers', 2, 3, 8),
        ('Power negative number', -3, 3, -27),
        ('Power negative sign', 3, -4, 0.012),
        ('Power negative sign and number', -1, -1, -1.0),
    ])
    def test_power_functionality(self, _, a, b, expected_result):
        self.assertEqual(round(self.calc.power(a, b), 3), expected_result)

    @parameterized.expand([
        ('Square root of positive number', 9, 3.0),
        ('Square root of one', 1, 1.0),
        ('Square root of zero', 0, 0.0),
        ('Square root of negative number', -4, ValueError),
    ])
    def test_square_root_functionality(self, _, a, expected_result):
        if a < 0:
            with self.assertRaises(expected_result):
                self.calc.square_root(a)
        else:
            self.assertEqual(round(self.calc.square_root(a), 3), expected_result)

if __name__ == '__main__':
    unittest.main()
