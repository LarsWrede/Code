class Node:  # Style guide: convention how to write code - Capitalize first letter
    # Class is the blueprint

    # Function to initialize the node object
    def __init__(self, data=None):  # always store "self"
        self.data = data  # Assign data
        self.next = None  # Initialize
        # next as null
        # the last element always has his next pointer set to None

    def __str__(self):
        return str(self.data)


class LinkedList:  # Look up PEP 20 & PEP 8

    # Function to initialize the Linked
    # List object
    def __init__(self, data=None):  # This will create the first element of the list
        self.head = Node(data)
        self.tail = self.head
        self.size = 1

    def __str__(self):
        data = ""
        current_node = self.head
        while current_node is not None:
            data += str(current_node.data) + " -> "
            current_node = current_node.next
        return data

    def add(self, data):
        # New Element of Class Node with our data input
        self.tail.next = Node(data)
        self.tail = self.tail.next
        self.size += 1

    def at(self, index):
        if index >= self.size:
            raise Exception(f'Index {index} out of bound')
        current = self.head
        for i in range(index):
            current = current.next
        return current

    def insert(self, index, data):
        current_index = 0
        new_node = Node(data)
        current = self.head
        while current.next is not None:  # Loop durch die Linked List
            if current_index == index - 1:
                temp = current.next
                current.next = new_node
                new_node.next = temp
                self.size += 1
                return
            current = current.next
            current_index += 1
        raise Exception(f'Index {index} out of bound')

    def remove(self, index):
        if index >= self.size:
            raise Exception(f'Index {index} out of bound')
        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return

        current = self.head
        for i in range(index - 1):
            current = current.next

        # falls wir den letzten knoten löschen wollen, müssen wir unser self.tail aktuell halten
        if current.next is self.tail:
            self.tail = current

        current.next = current.next.next
        self.size -= 1

    def __len__(self):
        return self.size  # lieber precompute than recompute ;)
