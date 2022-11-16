from typing import Optional, List
import drawtree
from collections import deque


class TreeNode:
    def __init__(self, val: int, left=None, right=None) -> None:
        self.val = val
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right

    def __repr__(self) -> str:
        return f"val: {self.val}, left: {self.left}, right: {self.right}"

    def __str__(self) -> str:
        return str(self.val)

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, self.__class__):
            if self.val == __o.val:
                return True
        return False


def to_binary_tree(items: list[int]) -> Optional[TreeNode]:
    """Create BT from list of values."""
    n = len(items)
    if n == 0:
        return None

    def inner(index: int = 0) -> Optional[TreeNode]:
        """Closure function using recursion bo build tree"""
        if n <= index or items[index] is None:
            return None

        node = TreeNode(items[index])
        node.left = inner(2 * index + 1)
        node.right = inner(2 * index + 2)
        return node

    return inner()


def traverse_node(node: Optional[TreeNode], nums: List[int]) -> List[int]:
    if node == None:
        return nums

    if node.left:
        nums.append(node.left.val)

    if node.right:
        nums.append(node.right.val)

    return nums


def traverse_tree(root: Optional[TreeNode]) -> List[int]:
    """Traverse a binary tree of integers and return the values in it as a list"""

    nums: List[int] = list()

    if root is None:
        return nums

    node: TreeNode = root
    q = deque()

    nums.append(node.val)

    while (node is not None):
        nums = traverse_node(node, nums)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

        if len(q):
            node = q.popleft()
        else:
            break

    return nums


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    root = to_binary_tree(nums)

    nums2 = traverse_tree(root)
    drawtree.draw_level_order('[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
