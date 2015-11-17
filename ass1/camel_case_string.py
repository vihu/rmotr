"""
Write a function that receives a string and returns a camel case version of it.
Example:
    camel_case('hello world')  # Hello World
"""

def camel_case(a_string):
    return ' '.join(map(str.capitalize, a_string.split()))

import unittest

class CamelCaseTestCase(unittest.TestCase):
    def test_word_with_spaces(self):
        self.assertEquals(camel_case('testing 123 hello'), 'Testing 123 Hello')

    def test_single_word(self):
        self.assertEqual(camel_case('testing'), 'Testing')

    def test_empty_string(self):
        self.assertEqual(camel_case(''), '')

if __name__ == '__main__':
    unittest.main()
