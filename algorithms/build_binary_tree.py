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

    n = iter(items)
    tree = TreeNode(next(n))
    fringe = deque([tree])
    while True:
        head = fringe.popleft()
        try:
            val = next(n)
            if val is not None:
                head.left = TreeNode(val)
                fringe.append(head.left)

            val = next(n)
            if val is not None:
                head.right = TreeNode(val)
                fringe.append(head.right)
        except StopIteration:
            break

    return tree


def traverse_tree(root: Optional[TreeNode]) -> list:
    """Traverse a binary tree of integers using breadth-first travesal method 
    and return the values of the nodes in the tree as a list"""

    nums = list()

    if root is None:
        return nums

    node: TreeNode = root
    q = deque()

    nums.append(node.val)

    while (node is not None):
        def traverse_child(node: Optional[TreeNode]):
            if node:
                nums.append(node.val)
                q.append(node)
            elif len(q):
                nums.append('#')

        traverse_child(node.left)
        traverse_child(node.right)

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


def preorder_traveral(node: Optional[TreeNode]) -> None:
    """One kind of depth-first traversal"""
    if node is None:
        return

    print(node.val, end=',')

    preorder_traveral(node.left)
    preorder_traveral(node.right)


def bft_traverse_tree(root: Optional[TreeNode]) -> list:
    """Traverse a binary tree of integers using breadth-first travesal method 
    and return the values of the nodes in the tree as a list"""

    nums = list()

    if root is None:
        return nums

    q = deque()
    q.append(root)

    while len(q):
        node = q.popleft()
        if node is not None:
            nums.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            nums.append(None)

    # Remove trailing hashes
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] is None:
            nums.pop()
        else:
            break

    return nums


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    root = to_binary_tree(nums)
    nums2 = traverse_tree(root)
    drawtree.draw_level_order('[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')

    print('\n\n\n')

    nums = [1, 2, 3, 4, 5, 6, 7, None, None, 10]
    root = to_binary_tree(nums)
    nums2 = traverse_tree(root)
    nums2_str = nums2.__repr__()
    nums2_str = nums2_str.replace("'", "").replace(" ", "")
    drawtree.draw_level_order(nums2_str)

    print('\n\n\n')

    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    drawtree.draw_level_order('[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
    root = to_binary_tree(nums)
    preorder_traveral(root)

    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    root = to_binary_tree(nums)
    bft_traverse_tree(root)

    nums = [1, 2, 3, 4, 5, 6, 7, None, None, 10]
    root = to_binary_tree(nums)
    bft_traverse_tree(root)

    nums = ['A', 'B', 'C', 'D', 'E', 'F', 'G', None, None, 'H', None, None, None, 'I', 'J']
    root = to_binary_tree(nums)
    bft_traverse_tree(root)
