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


def to_binary_tree(items: list[int]) -> TreeNode:
    """Create BT from list of values. Assumes non empty list and that first element in list is not null"""
    n = len(items)

    def inner(index: int = 0) -> Optional[TreeNode]:
        """Closure function using recursion bo build tree"""
        if n <= index or items[index] is None:
            return None

        node = TreeNode(items[index])
        node.left = inner(2 * index + 1)
        node.right = inner(2 * index + 2)
        return node

    return inner()  # type:ignore


def traverse_tree(root: Optional[TreeNode]) -> list:
    """Traverse a binary tree of integers and return the values in it as a list"""

    nums = list()

    if root is None:
        return nums

    node: TreeNode = root
    q = deque()

    nums.append(node.val)

    while (node is not None):
        if node.left:
            nums.append(node.left.val)
            q.append(node.left)
        elif len(q):
            nums.append('#')

        if node.right:
            q.append(node.right)
            nums.append(node.right.val)
        elif len(q):
            nums.append('#')

        if len(q):
            node = q.popleft()
        else:
            break

    # Trim trailing hashes
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] == '#':
            nums.pop()
        else:
            break

    return nums


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    root = to_binary_tree(nums)
    nums2 = traverse_tree(root)
    drawtree.draw_level_order('[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')

    print('\n')

    nums = [1, 2, 3, 4, 5, 6, 7, None, None, 10]
    root = to_binary_tree(nums)
    nums2 = traverse_tree(root)
    nums2_str = nums2.__repr__()
    nums2_str = nums2_str.replace("'", "").replace(" ", "")
    drawtree.draw_level_order(nums2_str)
