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


if __name__ == "__main__":
    unittest.main()
