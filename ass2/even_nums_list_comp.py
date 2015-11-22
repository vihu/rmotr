"""
Write a function that receives a list of numbers and returns only the even
elements. You must use List comprehensions to solve it.

Example:
        evens = even_numbers([5, 4, 3, 2, 1])  # [4, 2]

"""

import unittest


def even_numbers(a_list):
    # return even nums from a_list
    return [num for num in a_list if num % 2 == 0]


class EvenNumberTestCase(unittest.TestCase):
    def test_multiple_even_numbers(self):
        self.assertEqual(even_numbers([5, 4, 3, 2, 1]), [4, 2])

    def test_one_even_numbers(self):
        self.assertEqual(even_numbers([5, 4, 3, 7, 9, 1]), [4])

    def test_no_even_numbers(self):
        self.assertEqual(even_numbers([5, 3, 7, 9, 1]), [])

    def test_empty_list_even_numbers(self):
        self.assertEqual(even_numbers([]), [])


if __name__ == '__main__':
    unittest.main()
