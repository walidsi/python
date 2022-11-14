from typing import List, Optional
import timeit


def two_sum(nums: List[int], target: int) -> List[int]:

    result = []
    for index in range(len(nums)):  # Order O(n^2)
        for index2 in range(index + 1, len(nums)):
            if nums[index] + nums[index2] == target:
                result = [index, index2]
                break

    return result


def two_sum2(nums: List[int], target: int) -> List[int]:
    num_idx_map = {}

    result = []

    # Order O(n) by using a hash table ro store looped over integers, clever!!
    for i, n in enumerate(nums):

        diff = target - n

        if diff in num_idx_map:
            result = [num_idx_map[diff], i]
            break
        else:
            num_idx_map[n] = i

    return result


def isValid(s: str) -> bool:
    if (len(s) % 2 != 0):
        return False

    stack = list()

    stack.append(s[0])

    for c in s[1:]:
        stack.append(c)

        if len(stack) >= 2:
            if (stack[-1] == ']' and stack[-2] == '[') or \
                (stack[-1] == '}' and stack[-2] == '{') or \
                    (stack[-1] == ')' and stack[-2] == '('):
                stack.pop()
                stack.pop()

    if len(stack) == 0:
        return True
    else:
        return False


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

    if list1 is None:
        return list2

    if list2 is None:
        return list1

    # Initialization
    start = list1 if (list1.val <= list2.val) else list2
    last = start
    if (list1.val <= list2.val):
        list1 = start.next
    else:
        list2 = start.next
    start.next = None

    while list1 is not None and list2 is not None:
        curr = list1 if (list1.val <= list2.val) else list2

        last.next = curr
        last = last.next
        curr = curr.next
        last.next = None

        if (list1.val <= list2.val):
            list1 = curr
        else:
            list2 = curr

    if list1 is not None:
        last.next = list1

    if list2 is not None:
        last.next = list2

    return start


def max_profit(prices: List[int]) -> int:
    """Returns max profit for a stock buy sell decision gives prices for consecutive days
    Example: [2, 1, 2, 1, 0, 1, 2], should return 2, i.e. 2 - 0. Obvious answer is O(n^2) brute
    force, loop inside loop, but we should do better. We can do that by keeping track of the global
    minimun and its index Key always compare max_profit to current profit.

    Args:
        prices (List[int]): list of prices

    Returns:
        int: max profit you can make or 0
    """

    max_profit: int = 0
    profit: int = 0

    length = len(prices)

    if length <= 1:
        return max_profit

    global_min_idx = -1

    # Set days for first sub array
    if prices[0] < prices[1]:
        global_min_idx = 0
    else:
        global_min_idx = 1

    max_profit = max(0, prices[1] - prices[global_min_idx])

    for day in range(2, len(prices)):
        profit = prices[day] - prices[global_min_idx]
        if profit >= max_profit:  # Found new maximum profit
            max_profit = profit
        elif prices[day] < prices[global_min_idx]:  # Found new global minimum
            global_min_idx = day

    return max_profit

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """Invert a binary tree such that for each node, the left and right child exchange places

    Args:
        root (Optional[TreeNode]): reference to the first node

    Returns:
        Optional[TreeNode]: reference to the first node of the inverted tree
    """

    if root is None:  # Base condition 1
        return None

    if root.left is None and root.right is None:  # Base condition 2
        return root

    # Invert children first using recurcive calls
    invert_tree(root.left)
    invert_tree(root.right)

    # invert current node
    tmp = root.left
    root.left = root.right
    root.right = tmp

    return root


######################## main() ##############################################################################


def main():
    print(timeit.timeit('two_sum([3, 12, 44, 11, 6, 3, 22, 11, 33, 44, 55, 66, 1, 4], 5)', globals=globals()))
    print(timeit.timeit('two_sum2([3, 12, 44, 11, 6, 3, 22, 11, 33, 44, 55, 66, 1, 4], 5)', globals=globals()))


if __name__ == "__main__":
    main()
