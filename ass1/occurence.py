"""
Write a function that receives a list and an element and returns how many occurrences
of that particular element are in the list.
**You can't use any function from the standard library.**

Example:
    occurrences([7, 1, 5, 8, 0, 7, 9, 1, 7], 7)  # The number 7 is repeated 3 times.
    > 3
Extras:
* Try with a for loop
* Try with a while loop
* Investigate special list methods or python libraries. You can use whatever you want now.
"""

def occurrences(a_list, an_element):
    return a_list.count(an_element)

# Don't change below this line! These tests should pass

import unittest

class OccurrencesTestCase(unittest.TestCase):
    def test_multiple_occurences(self):
        self.assertEqual(occurrences([7, 1, 5, 8, 0, 7, 9, 1, 7], 7), 3)
        self.assertEqual(occurrences([2, 8, 2], 2), 2)

    def test_one_occurrence(self):
        self.assertEqual(occurrences([2, 8, 2], 8), 1)
        self.assertEqual(occurrences([8], 8), 1)

    def test_no_occurrences(self):
        self.assertEqual(occurrences([2, 8, 2], 9), 0)
        self.assertEqual(occurrences([2], 9), 0)
        self.assertEqual(occurrences([], 9), 0)

if __name__ == '__main__':
    unittest.main()
