import sys
sys.path.append('/github-repos/HTMLTestRunner/')
import HTMLTestRunner  # type: ignore

sys.path.append('/github-repos/HTMLTestRunner-oldani/')
import HtmlTestRunner.runner  # type: ignore

import unittest
from daily_byte import *
from typing import List, Tuple


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

    def test_is_palindrome_recursive(self):
        test_strings: List[Tuple[str, bool]] = [('abcba', True),
                                                ('foobof', False),
                                                ('ofobof', False),
                                                ('abccab', False),
                                                ('fobofo', False),
                                                ('bddb', True),
                                                ('dbbeabdaccccadbaebbd', True)]

        for tup in test_strings:
            with self.subTest(tup[0], expected_result=tup[1]):
                self.assertEqual(is_palindrome_recursive(tup[0]), tup[1])


if __name__ == "__main__":
    to_file: bool = True
    to_txt: bool = False
    is_twan: bool = True

    if to_file:
        suite = unittest.TestSuite([unittest.defaultTestLoader.loadTestsFromTestCase(TestDailyByte)])
        if to_txt:
            fp = open('daily_byte_tests.txt', 'w')
            unittest.TextTestRunner(fp).run(suite)
            fp.close()
        elif is_twan:
            fp = open('daily_byte_tests.html', 'w')
            HTMLTestRunner.HTMLTestRunner(fp).run(suite)
            fp.close()
        else:
            HtmlTestRunner.runner.HTMLTestRunner().run(suite)
    else:
        unittest.main()
