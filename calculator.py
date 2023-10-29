class Calculator:
    @staticmethod
    def add(augend, addend):
        if not (isinstance(augend, (int, float)) and isinstance(addend, (int, float))):
            raise TypeError("Both augend and addend must be of type int or float")
        return augend + addend

    @staticmethod
    def subtract(minuend, subtrahend):
        return minuend - subtrahend

    @staticmethod
    def multiply(multiplicand, multiplier):
        return multiplicand * multiplier

    @staticmethod
    def divide(dividend, divisor):
        return dividend / divisor
