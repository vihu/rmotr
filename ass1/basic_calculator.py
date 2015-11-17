"""
Write a function that receives 2 numbers and performs simple calculations
(additions, subtractions, multiplications and divisions)
based on a string parameter.
    calculator(2, 3, 'add')       # Should return 5
    calculator(7, 3, 'subtract')  # Should return 4
    calculator(2, 7, 'multiply')  # Should return 14
    calculator(8, 4, 'divide')    # Should return 2
    calculator(5, 2, 'divide')    # Should return 2.5 ATTENTION!
"""


def calculator(param1, param2, operation):
    if operation == 'add':
        return param1 + param2
    elif operation == 'subtract':
        return param1 - param2
    elif operation == 'multiply':
        return param1 * param2
    elif operation == 'divide':
        return param1 / (param2 + 0.0)



# Don't change below this line! These tests should pass

import unittest

class CalculatorTestCase(unittest.TestCase):
    def test_simple_addition(self):
        "Should add two numbers"
        self.assertEqual(calculator(2, 3, 'add'), 5)

    def test_simple_subtraction(self):
        "Should subtract two numbers"
        self.assertEqual(calculator(7, 3, 'subtract'), 4)

    def test_simple_multiplication(self):
        "Should multiply two numbers"
        self.assertEqual(calculator(2, 7, 'multiply'), 14)

    def test_simple_divition(self):
        "Should divide two integer numbers with an integer result"
        self.assertEqual(calculator(8, 4, 'divide'), 2)

    def test_simple_divition(self):
        "Should divide two integer numbers with an float result"
        self.assertEqual(calculator(5, 2, 'divide'), 2.5)

if __name__ == '__main__':
    unittest.main()
