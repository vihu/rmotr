"""
Write a function that receives a list of numbers
and a list of terms and returns only the elements that are divisible
by all of those terms. You must use two nested list comprehensions to solve it.

Example:
        divisible_numbers([12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [2, 3])  # [12, 6]
"""

import unittest


def divisible_numbers(a_list, a_list_of_terms):
    # use 2 list comps
    # return [num for num in a_list if num%([a_list_of_terms[0]*k for k in a_list_of_terms[1:]][0]) == 0]
    # tycho --> [x for x in a_list if [x for y in a_list_of_terms if x % y == 0].count(x) == len(a_list_of_terms)
    return [x for x in a_list if len([x for y in a_list_of_terms if x % y == 0]) == len(a_list_of_terms)]


class DivisibleNumbersTestCase(unittest.TestCase):
    def test_many_divisible_numbers(self):
        self.assertEqual(set(divisible_numbers([12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
                                               [2, 3])), set([6, 12]))

    def test_one_divisible_numbers(self):
        self.assertEqual(divisible_numbers([16, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [2, 3, 4]), [12])

    def test_empty_list(self):
        self.assertEqual(divisible_numbers([], [5, 7]),  [])

    def test_both_empty_lists(self):
        self.assertEqual(divisible_numbers([], []),  [])

    def test_no_result(self):
        self.assertEqual(divisible_numbers([2, 4, 8], [5, 7]),  [])


if __name__ == '__main__':
    unittest.main()
