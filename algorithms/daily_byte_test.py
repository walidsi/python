import unittest
from daily_byte import *


class TestDailyByte(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertEqual(is_palindrome('level'), True, 'Failed')
        self.assertEqual(is_palindrome('algorithm'), False, 'Failed')
        self.assertEqual(is_palindrome('A man, a plan, a canal: Panama.'), True, 'Failed')
        self.assertEqual(is_palindrome('A man , nam A'), True, 'Failed')

    def test_reverse_string(self):
        self.assertEqual(gb_reverse_string('Hello World'), 'dlroW olleH', 'Failed')
        self.assertEqual(gb_reverse_string_2('Hello World'), 'dlroW olleH', 'Failed')


if __name__ == "__main__":
    unittest.main()
