"""
This python file creates a hash table to store data. The hash system includes search,
insert, and delete operations. Each slot of the hash table contains a linked list to store the data.
The linked list for the slots is created in another file called linked, which is imported to this
file. The position of the data to the appropriate slot is found by applying module operation with
the size of the hash table. The data can be a string or integer type. The size of the hash table is
fixed and cannot be changed after creation.
"""

import linked


class HashTable:
    """ Creating a hash table class.
    """

    def __init__(self, M):
        """ The class takes the size of the hash table as an argument and creates a new hash table.

        Args:
            M (integer): size of the hash table.
        """
        self.M = M
        self.T = [None] * M

    def value(self, data):
        """ Takes the data as an argument and returns the integer value of the data.
        If the data is a negative integer, returns the absolute value of the integer by adding 1.
        Otherwise the integer value is returned.

        Args:
            data (string, integer): data of the hash table.

        Returns:
            integer: integer value of the data.
        """
        if isinstance(data, int):
            if data < 0:
                return abs(data) + 1
            return data
        string_value = 0
        for i in data:
            string_value += ord(i)
        return string_value

    def insert(self, data):
        """ Inserts the data into the hash table.

        Args:
            data (string, integer): data of the hash table.
        """
        position = self.value(data) % self.M
        if self.T[position] is None:  # If the slot in the hash table is empty
            L = linked.LinkedList()  # Create a new linked list for the empty slot
            L.append(data)
            print("item: " + "'" + str(data) + "'" + " is inserted to the hash table\n")
            self.T[position] = L
        else:
            # Check if the data already in the table
            found = self.T[position].search(data)
            if found != -1:
                print("item: " + "'" + str(data) +"'" + " already in the table\n")
                return
            # Data is appended at the end of the linked list in the appropriate slot
            self.T[position].append(data)
            print("item: " + "'" + str(data) + "'" + " is inserted to the hash table\n")

    def search(self, data):
        """ Searches for the given data in the hash table.

        Args:
            data (string, integer): data of the hash table.
        """
        position = self.value(data) % self.M
        if self.T[position] is None:  # Check if the data already in the table
            print("item: " + "'" + str(data) + "'" + " not in the table\n")
            return
        found = self.T[position].search(data)
        if found == -1:
            print("item: " + "'" + str(data) + "'" + " not in the table\n")
            return
        # Found data information is printed
        print("item: " + "'" + str(data) + "'" + " found in index:",
            found, "of the linked list in the hash table's slot:", position)
        print()

    def delete(self, data):
        """ Deletes the given data from the hash table.

        Args:
            data (string, integer): data of the hash table.
        """
        position = self.value(data) % self.M
        if self.T[position] is None:  # Check if the data already in the table
            print("item: " + "'" + str(data) + "'" + " not in the table\n")
            return
        found = self.T[position].search(data)
        if found == -1:
            print("item: " + "'" + str(data) + "'" + " not in the table\n")
            return
        # Found data information is deleted from the linked list in the appropriate slot.
        self.T[position].delete(found)
        print("item: " + "'" + str(data) + "'" + " is deleted from the hash table\n")

    def print(self):
        """ Prints the content of the hash table.
        """
        print("printing the content of the table: ")
        for index, value in enumerate(self.T):
            if value is not None:
                if value.len != 0:
                    print("the data in the slot", index, end=': ')
                    value.print()
                    print()
        print()


if __name__ == "__main__":
    # Initialize the hash table
    table = HashTable(3)
    print()
    # Insert the data into the hash table
    insert_list = [12, 'hashtable', 1234, 4328989, 'BM40A1500', -12456, 'aaaabbbbcccc']
    for i in insert_list:
        table.insert(i)
        table.print()
    # Search for the data in the hash table
    search_list = [-12456, 'hashtable', 1235]
    for i in search_list:
        table.search(i)
    # Delete the data from the hash table
    delete_list = ['BM40A1500', 1234, 'aaaabbbbcccc']
    for i in delete_list:
        table.delete(i)
    table.print()
