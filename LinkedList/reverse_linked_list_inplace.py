class Node:
    '''
    Creates a node for the linked list whice contains the data 
    itself and the reference for the next node

    Args:
        data: a value that is to be stored in the list
    '''

    def __init__(self, data) -> None:
        self.data = data
        self.next_node = None

    # whenever we call the Node object, this repr function will be called to represent data
    def __repr__(self):
        return str(self.data)


class LinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0

    # O(N) running time complexity
    def reverse(self):

        current_node = self.head
        previous_node = None
        next_node = None

        while current_node:
            next_node = current_node.next_node
            current_node.next_node = previous_node
            previous_node = current_node
            current_node = next_node

        self.head = previous_node

    # O(1) constant running time
    def insert_start(self, data):
        self.size += 1
        new_node = Node(data)

        # check if the linked is empty
        if self.head is None:
            self.head = new_node

        else:
            # we have to update the reference
            new_node.next_node = self.head
            self.head = new_node

    # O(N) linear time
    def insert_end(self, data):
        self.size += 1
        new_node = Node(data)

        # check if the linked is empty
        if self.head is None:
            self.head = new_node

        else:
            actual_node = self.head

            # we are checking for the last node
            # this is why is has O(N) linear running time complexity
            while actual_node.next_node is not None:
                actual_node = actual_node.next_node

            # now insert the item at the last position of the list
            actual_node.next_node = new_node

    # O(N) linear running time
    def traverse(self):
        actual_node = self.head

        while actual_node is not None:
            print(actual_node)
            actual_node = actual_node.next_node


if __name__ == '__main__':
    linked_list = LinkedList()

    linked_list.insert_start(1)
    linked_list.insert_start(2)
    linked_list.insert_start(3)
    linked_list.insert_start(4)
    linked_list.insert_start(5)

    linked_list.traverse()

    linked_list.reverse()

    print(f"Reversed list:")
    linked_list.traverse()
