from typing import Optional


class Node:
    def __init__(self, value) -> None:
        self.val = value
        self.next_node: Optional[Node] = None


class LinkedList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None

    def add_node(self, node):
        if self.head is None:
            self.head = node
            self.head.next_node = None
        else:
            last: Node = self.head
            while last.next_node is not None:
                last = last.next_node

            last.next_node = node
            last.next_node.next_node = None

    def add_nodes(self, node):
        if self.head is None:
            self.head = node
            self.head.next_node = None
        else:
            last: Node = self.head
            while last.next_node is not None:
                last = last.next_node

            last.next_node = node

    def __repr__(self) -> str:
        arr = list()

        curr: Optional[Node] = self.head

        while curr is not None:
            arr.append(curr.val)
            curr = curr.next_node

        return str(arr)


def mergeTwoLists(list1: Optional[LinkedList], list2: Optional[LinkedList]) -> Optional[LinkedList]:

    if list1 is None:
        return list2

    if list2 is None:
        return list1

    merged = LinkedList()

    last: Optional[Node] = None

    list1_node: Optional[Node] = list1.head
    list2_node: Optional[Node] = list2.head

    while list1_node is not None and list2_node is not None:
        curr = list1_node if (list1_node.val <= list2_node.val) else list2_node

        next: Optional[Node] = curr.next_node
        merged.add_node(curr)
        curr = next

        if (list1_node.val <= list2_node.val):
            list1_node = curr
        else:
            list2_node = curr

    if list1_node is not None:
        merged.add_nodes(list1_node)

    if list2_node is not None:
        merged.add_nodes(list2_node)

    return merged


def main():
    ll1 = LinkedList()

    for i in range(1, 5):
        node = Node(i)
        ll1.add_node(node)

    print(ll1)

    ll2 = LinkedList()

    for i in range(2, 5):
        node = Node(i)
        ll2.add_node(node)

    print(ll2)

    ll3 = mergeTwoLists(ll1, ll2)

    print(ll3)


if __name__ == "__main__":
    main()
