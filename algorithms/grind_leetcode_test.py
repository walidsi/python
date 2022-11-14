import unittest
from grind_leetcode import *


class TestGrindLeetCode(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_two_sum(self):
        self.assertEqual(two_sum([3, 2, 4], 6), [1, 2], "Failed to find two sum of 6")

    def test_two_sum2(self):
        self.assertEqual(two_sum2([3, 2, 4], 6), [1, 2], "Failed to find two sum of 6")

    def test_isValid(self):
        self.assertEqual(isValid('[](){}'), True, "Failed")
        self.assertEqual(isValid('[()]{}'), True, "Failed")
        self.assertEqual(isValid('[(]{}]'), False, "Failed")
        self.assertEqual(isValid('()'), True, "Failed")
        self.assertEqual(isValid("(){}}{"), False, "Failed")

    def test_max_profitl(self):
        self.assertEqual(max_profit([3, 3, 5, 0, 0, 3, 1, 4]), 4, "Wrong answer")
        self.assertEqual(max_profit([2, 1, 2, 1, 0, 1, 2]), 2, "Wrong answer")
        self.assertEqual(max_profit([7, 1, 5, 3, 6, 4]), 5, "Wrong answer")
        self.assertEqual(max_profit([7, 6, 4, 3, 1]), 0, "Wrong answer")
        self.assertEqual(max_profit([1, 2]), 1, "Wrong answer")
        self.assertEqual(max_profit([2, 4, 1]), 2, "Wrong answer")


if __name__ == "__main__":
    unittest.main()
