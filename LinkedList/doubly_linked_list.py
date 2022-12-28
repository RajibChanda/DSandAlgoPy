class Node:
    '''
    Creates a node for the linked list whice contains the data 
    itself and the reference for the next node and previous node

    Args:
    data (int/float/char): item to be inserted in the linked list
    '''

    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.previous = None

    # whenever we call the Node object, this repr function will be called to represent data
    def __repr__(self):
        return str(self.data)


class DoublyLinkedList:
    '''
    Creates a linked list with given item.
    Performs few operations: inserts an item at the front or end
    '''

    def __init__(self):
        self.head = None
        self.tail = None

    # this operation inserts items at the end of the linked list, so we have to
    # manupulate the tail node in O(1) runnuing time
    def insert(self, data):

        new_node = Node(data)

        # when the list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        # there is atleast 1 item in the data structure, we keep inserting items at the end
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def traverse_forward(self):

        actual_node = self.head

        while actual_node is not None:
            print(f"{actual_node.data}")
            actual_node = actual_node.next

    def traverse_backward(self):

        actual_node = self.tail

        while actual_node is not None:
            print(f"{actual_node.data}")
            actual_node = actual_node.previous

    def remove_data(self, data):

        # if list is empty
        if self.head is None:
            return

        current_node = self.head
        previous_node = None

        # search for the node we want to remove
        while current_node is not None and current_node.data != data:
            previous_node = current_node
            current_node = current_node.next

        # data not found
        if current_node is None:
            return

        # if first item of the list is the searched item
        if previous_node is None:
            self.head = current_node.next
            current_node.next.previous = None

        # if the last item of the list is the searched item
        elif current_node.next is None:
            self.tail = previous_node
            previous_node.next = None

        else:
            previous_node.next = current_node.next
            current_node.next.previous = previous_node


if __name__ == '__main__':

    linked_list = DoublyLinkedList()
    linked_list.insert(10)
    linked_list.insert(20)
    linked_list.insert(30)

    linked_list.traverse_forward()

    linked_list.traverse_backward()

    linked_list.remove_data(20)

    linked_list.traverse_backward()
