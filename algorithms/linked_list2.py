from typing import Optional, Tuple, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    """Reverses a linked list, returing the head of the reversed linked list"""
    def _reverseList(head) -> Tuple[Optional[ListNode], Optional[ListNode]]:
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


def linked_list_to_list(head: ListNode) -> List[int]:
    node = head
    ll = []
    while node is not None:
        ll.append(node.val)
        node = node.next
    return ll


def main():
    nums = [1, 2, 3, 4, 5]
    head = ListNode(nums[0])
    curr = head
    for n in nums[1:]:
        node = ListNode(n)
        curr.next = node
        curr = node

    print(linked_list_to_list(head))

    new_head = reverseList(head)

    print(linked_list_to_list(new_head))


if __name__ == "__main__":
    main()