from calculator import Calculator
import unittest


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        result = self.calculator.add(5, 3)
        self.assertEqual(result, 8)

    def test_subtract(self):
        result = self.calculator.subtract(6, 5)
        self.assertEqual(result, 1)

    def test_multiply(self):
        result = self.calculator.multiply(6, 5)
        self.assertEqual(result, 30)

    def test_divide(self):
        calculator = Calculator()
        result = calculator.divide(6, 3)
        self.assertEqual(result, 2)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calculator.divide(6, 0)
