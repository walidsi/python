import unittest
from grind_leetcode import *
import build_binary_tree as bbt
from typing import Optional, List


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
        nums: List[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        root: Optional[TreeNode] = bbt.to_binary_tree(nums)
        root_inverted = invert_tree(root)
        root_inverted_inverted = invert_tree(root_inverted)
        nums_inverted_inverted = bbt.traverse_tree(root_inverted_inverted)
        self.assertEqual(nums, nums_inverted_inverted, "Failed to create and invert then invert again a binary tree")

    def test_is_anagram(self):
        self.assertEqual(is_anagram("anagram", "nagaram"), True, "Failed is_anagram")
        self.assertEqual(is_anagram("rat", "cat"), False, "Failed is_anagram")

    def test_search(self):
        self.assertEqual(search([-1, 0, 3, 5, 9, 12], 9), 4, "Failed search")
        self.assertEqual(search([-1, 0, 3, 5, 9, 12], 2), -1, "Failed search")

    def test_flood_fill(self):
        image = [[0, 0, 0], [0, 0, 0]]
        sr = 0
        sc = 0
        color = 0
        self.assertEqual(flood_fill(image, sr, sc, color), [[0, 0, 0], [0, 0, 0]], "Failed flood_fill")

        image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
        sr = 1
        sc = 1
        color = 2
        self.assertEqual(flood_fill(image, sr, sc, color), [[2, 2, 2], [2, 2, 0], [2, 0, 1]], "Failed flood_fill")

        image = [[0, 0, 0], [0, 0, 0]]
        sr = 1
        sc = 0
        color = 2
        self.assertEqual(flood_fill(image, sr, sc, color), [[2, 2, 2], [2, 2, 2]], "Failed flood_fill")

    def test_lowestCommonAncestor(self):
        nums = [6, 2, 8, 0, 4, 7, 9, 3, 5]
        root: TreeNode = bbt.to_binary_tree(nums)  # type: ignore
        self.assertEqual(lowestCommonAncestor(root, TreeNode(2), TreeNode(8)), TreeNode(6), "Failed lowestCommonAncestor")

        nums = [6, 2, 8, 0, 4, 7, 9, 3, 5]
        root: TreeNode = bbt.to_binary_tree(nums)  # type: ignore
        self.assertEqual(lowestCommonAncestor(root, TreeNode(2), TreeNode(4)), TreeNode(2), "Failed lowestCommonAncestor")

        nums = [2, 1]
        root: TreeNode = bbt.to_binary_tree(nums)  # type: ignore
        self.assertEqual(lowestCommonAncestor(root, TreeNode(2), TreeNode(1)), TreeNode(2), "Failed lowestCommonAncestor")

        print('All success!')


if __name__ == "__main__":
    unittest.main()
