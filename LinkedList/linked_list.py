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


class LinkedList:
    '''
    Creates a linked list with given item.
    Performs few operations: inserts an item at the front or end, delets item
    '''

    def __init__(self):
        # this is the first node of the linked list
        self.head = None
        self.num_of_nodes = 0

    # O(1) constant running time
    def insert_start(self, data):
        self.num_of_nodes += 1
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
        self.num_of_nodes += 1
        new_node = Node(data)

        # check if the linked is empty
        if self.head is None:
            self.head = new_node

        else:
            current_node = self.head

            # we are checking for the last node
            # this is why is has O(N) linear running time complexity
            while current_node.next_node is not None:
                current_node = current_node.next_node

            # now insert the item at the last position of the list
            current_node.next_node = new_node

    # O(1) constant running time

    def size_of_list(self):
        return self.num_of_nodes

    # O(N) linear running time

    def traverse(self):
        current_node = self.head

        while current_node is not None:
            print(current_node)
            current_node = current_node.next_node

    # O(N) linear running time

    def remove(self, data):

        # the list is empty
        if self.head is None:
            return

        current_node = self.head
        previous_node = None

        # search for the item we want to remove (data)
        while current_node is not None and current_node.data != data:
            previous_node = current_node
            current_node = current_node.next_node

        # search miss
        if current_node is None:
            return

        # update the references
        # the head node is the one we want ot remove
        if previous_node is None:
            self.head = current_node.next_node

        else:
            # remove an internal node
            # remove the node by updating the pointers, NO NEED to DELETE the node
            # because the garbage collector will do that, just we need to update the reference
            previous_node.next_node = current_node.next_node


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.insert_start(5)
    linked_list.insert_start(7)
    linked_list.insert_start("E")
    linked_list.insert_end(17)
    linked_list.traverse()
    print('-------')
    linked_list.remove(7)
    linked_list.traverse()
