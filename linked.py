"""
This python file creates a new linked list to store data. The linked list includes append,
delete, and search operations.
"""


class Node:
    """ Creating a node class for the linked list of nodes.
    """

    def __init__(self, data, next):
        """ The class takes the data and the next node as arguments.

        Args:
            data (any tpe): the data of the node.
            next (None): the pointer to the next node.
        """
        self.data = data
        self.next = next


class LinkedList:
    """ Creating a linked list class to store the data.
    """

    def __init__(self):
        """ The class creates a head, tail, and the length of the list.
        """
        self.tail = None
        self.head = None
        self.len = 0

    def append(self, data):
        """ Appends the data at the end of the list.

        Args:
            data (any type): the data of the node.
        """
        new = Node(data, None)  # A new node is created for storing the data
        # If the head is empty, new node is the head (and the tail)
        if self.head is None:
            self.head = new
            new.next = self.tail
            self.tail = new
        else:
            self.tail.next = new
            self.tail = new
        self.len += 1

    def delete(self, index):
        """ Deletes the data from the linked list.

        Args:
            index (integer): the index of the data to be deleted.
        """
        if index >= self.len:  # Returns if the index is greater than the list size
            return
        itr = self.head
        if index == 0:  # If the node is the head
            self.head = itr.next
            self.len -= 1
            return
        index_itr = 0
        while itr:  # Search for the data by looping through the list
            if index == index_itr:
                break
            prev = itr
            itr = itr.next
            index_itr += 1
        prev.next = itr.next
        self.len -= 1

    def search(self, data):
        """ Searchs for the data in the linked list.

        Args:
            data (any type): the data of the node.

        Returns:
            integer: returns the index of the found data. Returns -1 if the data not found.
        """
        index_itr = 0
        itr = self.head
        while itr:  # Search for the data by looping through the list
            if itr.data == data:
                return index_itr
            itr = itr.next
            index_itr += 1
        return -1

    def print(self):
        """ Prints the content of the linked list.
        """
        itr = self.head
        while itr:
            print(itr.data, end='->')
            itr = itr.next
