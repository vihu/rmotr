"""
Define a function that computes the length of a given list or string
You can't use the builtin `len` function, you must use a for loop.
Example:
    length('hello')  # Should return 5
"""

def length(a_string):
    count = 0
    for i in a_string:
        count += 1
    return count


# Don't change below this line! These tests should pass

import unittest

class LengthTestCase(unittest.TestCase):
    def test_length_multiple_words(self):
        self.assertEqual(length('hello world'), 11)

    def test_length_single_word(self):
        self.assertEqual(length('hello'), 5)

    def test_length_empty_string(self):
        self.assertEqual(length(''), 0)

if __name__ == '__main__':
    unittest.main()
