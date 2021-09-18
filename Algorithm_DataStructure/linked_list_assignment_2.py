#!/usr/bin/env python
# coding: utf-8


from time import perf_counter_ns


# Node class
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
        self.size = 1

    def __str__(self):
        data = ""
        current_node = self.head
        while current_node is not None:
            data += str(current_node.data) + " -> "
            current_node = current_node.next
        return data[:-1]

    def add(self, data):
        new_node = Node(data)  # New Element of Class Node with our data input
        current = self.head   # Element we are currently looking at
        # Iterate over each one of the nodes in the list, starting with head -> last node == None
        while current.next != None:
            current = current.next
        # Once we are at the last Node we can set the .next to new_node
        current.next = new_node

    def at(self, index):
        current_index = 0
        current = self.head
        while current != None:
            if current_index == index:
                return current.data
            current_index += 1

    def insert(self, index, data):
        pointer = []  # Node where the inserted Element should point to
        current_index = 0
        new_node = Node(data)
        current = self.head
        while current.next != None:  # Loop durch die Linked List
            last = current
            current = current.next
            if current_index == index:
                pointer = last.next
                last.next = new_node
                new_node.next = pointer
                return
            current_index += 1

    def remove(self, index):
        current_index = 0
        current = self.head
        while True:
            last = current
            current = current.next
            if current_index == index:
                # Deletes by setting the pointer from last note to be skipped past the current note
                last.next = current.next
                return
            current_index += 1

    def __len__(self):
        current = self.head
        # Counts how many nodes we have
        total = 0
        while current.next != None:
            total += 1
            current = current.next
        return total


x = LinkedList(7)
x.add(0)
x.add(1)
x.add(2)
x.add(3)
x.add(4)
# x.remove()
x.insert(3, 5)
str(x)


x.at(2)


time_start = perf_counter_ns()
test = LinkedList()
n = 50000
j = 1
while j <= n:
    test.add(j)
    j += 1
time_end = perf_counter_ns()
time_span = time_end - time_start


len(test)


time_in_sec_10000 = time_span / 1000000000
print("To create a Linked Links with n = 10.000 takes %d Seconds" %
      time_in_sec_10000)


time_in_sec_100000 = (time_span / 1000000000)
print("To create a Linked Links with n = 100.000 takes %d Seconds" %
      time_in_sec_100000)
