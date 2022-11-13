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

    start: ListNode = None
    last: ListNode = None
    curr: ListNode = None

    while list1 is not None and list2 is not None:
        curr = list1 if (list1.val <= list2.val) else list2

        if start is None:
            start = curr
            curr = curr.next
            start.next = None
            last = start
        else:
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


def main():
    print(timeit.timeit('two_sum([3, 12, 44, 11, 6, 3, 22, 11, 33, 44, 55, 66, 1, 4], 5)', globals=globals()))
    print(timeit.timeit('two_sum2([3, 12, 44, 11, 6, 3, 22, 11, 33, 44, 55, 66, 1, 4], 5)', globals=globals()))


if __name__ == "__main__":
    main()
