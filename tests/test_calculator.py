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

    def test_large_numbers(self):
        result = self.calculator.add(int(1e50), int(1e50))
        self.assertEqual(result, int(2e50))

    def test_negative_numbers(self):
        result = self.calculator.subtract(-5, -3)
        self.assertEqual(result, -2)

    def test_floats(self):
        result = self.calculator.multiply(5.5, 4.2)
        self.assertAlmostEqual(result, 23.1)

    def test_zero(self):
        result = self.calculator.divide(0, 5)
        self.assertEqual(result, 0)

    def test_mixed_sign(self):
        result = self.calculator.add(5, -3)
        self.assertEqual(result, 2)

    def test_type_error(self):
        with self.assertRaises(TypeError):
            self.calculator.add("five", "three")

    def test_return_type(self):
        result = self.calculator.subtract(6, 3)
        self.assertIsInstance(result, int)
        result = self.calculator.subtract(3.3, 1.1)
        self.assertIsInstance(result, float)


if __name__ == '__main__':
    unittest.main()
