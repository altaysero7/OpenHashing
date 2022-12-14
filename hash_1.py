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
        """ Takes the data as an argument and returns the string value of the data.

        Args:
            data (string, integer): data of the hash table.

        Returns:
            integer: hash function's specific value of the data.
        """
        data = str(data) # The data is converted into a string to make the function work with integers too
        string_value = 0
        for char in data:
            string_value += ord(char)  # Every character's Unicode is summed
        # The string value is powered with 2 to make the hash table as distributed as possible with larger numbers.
        # In case to avoid any collision, the first character of the data is substracted from the final string value.
        string_value = (string_value**2)-ord(data[0])
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
