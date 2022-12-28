"""
Suppose we have a standard linked list. Construct an in-place 
(without extra memory) algorithm thats able to find the middle node!
"""


class Node:

    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList:

    def __init__(self) -> None:
        self.head = None
        self.size = 0

    def get_moddle_node(self):

        fast_pointer = self.head
        slow_pointer = self.head

        # while the fast pointer reaches the last node, the slow pointer is on the middle node
        while fast_pointer.next_node and fast_pointer.next_node.next_node:
            fast_pointer = fast_pointer.next_node.next_node
            slow_pointer = slow_pointer.next_node

        return slow_pointer

    def insert(self, data):

        self.size = self.size + 1
        new_node = Node(data)

        # check if the linked is empty
        if self.head is None:
            self.head = new_node

        else:
            # we have to update the reference
            new_node.next_node = self.head
            self.head = new_node

    def traverse_list(self):

        actual_node = self.head

        while actual_node:
            print(f"{actual_node.data}")
            actual_node = actual_node.next_node


if __name__ == '__main__':
    linked_list = LinkedList()

    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)
    linked_list.insert(4)

    print(f"Middle node: {linked_list.get_moddle_node().data}")
