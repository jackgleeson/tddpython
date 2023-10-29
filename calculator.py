class Calculator:

    def add(self, augend, addend):
        self._check_number_type(augend, addend)
        return augend + addend

    def subtract(self, minuend, subtrahend):
        self._check_number_type(minuend, subtrahend)
        return minuend - subtrahend

    def multiply(self, multiplicand, multiplier):
        self._check_number_type(multiplicand, multiplier)
        return multiplicand * multiplier

    def divide(self, dividend, divisor):
        self._check_number_type(dividend, divisor)
        if divisor == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        return dividend / divisor

    @staticmethod
    def _check_number_type(*args):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise TypeError("Arguments must be of type int or float")
