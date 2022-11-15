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

    def test_is_closed_loop(self):
        self.assertEqual(is_closed_loop('LR'), True, 'Failed is_closed_loop')
        self.assertEqual(is_closed_loop('URURD'), False, 'Failed is_closed_loop')
        self.assertEqual(is_closed_loop('RUULLDRD'), True, 'Failed is_closed_loop')

    def test_is_capitalized_correctly(self):
        self.assertEqual(is_capitalized_correctly('USA'), True, 'Failed is_capitalized_correctly')
        self.assertEqual(is_capitalized_correctly('Calvin'), True, 'Failed is_capitalized_correctly')
        self.assertEqual(is_capitalized_correctly('compUter'), False, 'Failed is_capitalized_correctly')
        self.assertEqual(is_capitalized_correctly('coding'), True, 'Failed is_capitalized_correctly')

    def test_bianry_sum(self):
        self.assertEqual(binary_sum('100', '1'), '101', 'Failed binary_sum')
        self.assertEqual(binary_sum('11', '1'), '100', 'Failed binary_sum')
        self.assertEqual(binary_sum('1', '0'), '1', 'Failed binary_sum')
        self.assertEqual(binary_sum('101011101', '1011111'), '110111100', 'Failed binary_sum')


if __name__ == "__main__":
    unittest.main()
