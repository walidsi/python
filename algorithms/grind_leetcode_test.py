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

    def test_invert_tree(self):
        # Empty tree
        self.assertEqual(invert_tree(None), None, "Wrong answer")
        one = TreeNode(1)  # No children
        self.assertEqual(invert_tree(one), one, "Wrong answer")
        # TODO: this is all I can write as unit tests right now for the binary tree inversion
        # I need a lot of thinking on how to code the building of the tree itself and how to code
        # part that will verify that it is inverted correctly. i.e. what leetcode does to check the
        # correctness of my implementation 😉
        # Tip: If you invert a binary tree twice, you should get the original back if your algorithm
        # is bug free.

    def test_is_anagram(self):
        self.assertEqual(is_anagram("anagram", "nagaram"), True, "Failed is_anagram")
        self.assertEqual(is_anagram("rat", "cat"), False, "Failed is_anagram")

    def test_search(self):
        self.assertEqual(search([-1, 0, 3, 5, 9, 12], 9), 4, "Failed search")
        self.assertEqual(search([-1, 0, 3, 5, 9, 12], 2), -1, "Failed search")


if __name__ == "__main__":
    unittest.main()
