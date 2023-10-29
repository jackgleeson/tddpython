from calculator import Calculator
import unittest


class TestCalculator(unittest.TestCase):

    def test_add(self):
        calculator = Calculator
        result = calculator.add(5, 3)
        self.assertEqual(result, 8)

    def test_subtract(self):
        calculator = Calculator
        result = calculator.subtract(6, 5)
        self.assertEqual(result, 1)
