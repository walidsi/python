import unittest
from daily_byte import *


class TestDailyByte(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertEqual(is_palindrome('level'), True)
        self.assertEqual(is_palindrome('algorithm'), False)
        self.assertEqual(is_palindrome('A man, a plan, a canal: Panama.'), True)
        self.assertEqual(is_palindrome('A man , nam A'), True)

    def test_reverse_string(self):
        self.assertEqual(gb_reverse_string('Hello World'), 'dlroW olleH')
        self.assertEqual(gb_reverse_string_2('Hello World'), 'dlroW olleH')

    def test_is_closed_loop(self):
        self.assertEqual(is_closed_loop('LR'), True)
        self.assertEqual(is_closed_loop('URURD'), False)
        self.assertEqual(is_closed_loop('RUULLDRD'), True)

    def test_is_capitalized_correctly(self):
        self.assertEqual(is_capitalized_correctly('USA'), True)
        self.assertEqual(is_capitalized_correctly('Calvin'), True)
        self.assertEqual(is_capitalized_correctly('compUter'), False)
        self.assertEqual(is_capitalized_correctly('coding'), True)

    def test_bianry_sum(self):
        self.assertEqual(binary_sum('100', '1'), '101')
        self.assertEqual(binary_sum('11', '1'), '100')
        self.assertEqual(binary_sum('1', '0'), '1')
        self.assertEqual(binary_sum('101011101', '1011111'), '110111100')

    def test_find_longest_common_prefix(self):
        self.assertEqual(find_longest_common_prefix(["colorado", "color", "cold"]), 'col')
        self.assertEqual(find_longest_common_prefix(["a", "b", "c"]), "")
        self.assertEqual(find_longest_common_prefix(["spot", "spotty", "spotted"]), "spot")

    def test_is_valid_palindrome_with_removal(self):
        self.assertEqual(is_valid_palindrome_with_removal('abcba'), True)
        self.assertEqual(is_valid_palindrome_with_removal('foobof'), True)
        self.assertEqual(is_valid_palindrome_with_removal('ofobof'), True)
        self.assertEqual(is_valid_palindrome_with_removal('abccab'), False)
        self.assertEqual(is_valid_palindrome_with_removal('fobofo'), True)
        self.assertEqual(is_valid_palindrome_with_removal('bddb'), True)
        self.assertEqual(is_valid_palindrome_with_removal('"dbbeabdaccccadbaebbd"'), True)


if __name__ == "__main__":
    unittest.main()
