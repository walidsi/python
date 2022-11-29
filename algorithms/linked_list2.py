from typing import Optional, Tuple


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    """Reverses a linked list, returing the head of the reversed linked list"""
    def _reverseList(head) -> Tuple(Optional[ListNode], Optional[ListNode]):
        """Closure function to reverse a linked list recursively returning 
        new head and tail of sub-linked list at each stage"""
        if head is None:
            return (None, None)

        if head.next is None:
            return (head, None)

        if head.next.next is None:
            new_head = head.next  # tail is new head
            head.next = None  # New tail points to nothing after itself
            new_head.next = head  # new head point to current head as the new tail
            return (new_head, new_head.next)

        new_head, tail = _reverseList(head.next)

        # Append current head at the end of the recursively reversed linked list
        # Make sure it points to None to avoid infinite looping
        head.next = None
        tail.next = head
        return new_head, head

    new_head, _ = _reverseList(head)
    return new_head