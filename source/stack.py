#!python

from linkedlist import LinkedList


# implement LinkedStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class LinkedStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any"""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack"""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise"""
        if self.list.size == 0:
            return True
        return False

    def length(self):
        """Return the number of items in this stack"""
        return self.list.length()

    def push(self, item):
        """Insert the given item on the top of this stack"""
        self.list.prepend(item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty"""
        if self.is_empty() is True:
            return None
        else:
            return self.list.head.data

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty"""
        if self.is_empty():
            raise ValueError('Stack is empty')
        else:
            first_item = self.list.head.data
            self.list.delete(first_item)
            return first_item


# implement ArrayStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class ArrayStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any"""
        # Initialize a new dynamic array to store the items
        self.list = list()
        if iterable:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack"""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise"""
        if self.length() is 0:
            return True
        return False

    def length(self):
        """Return the number of items in this stack"""
        return len(self.list)

    def push(self, item):
        """Insert the given item on the top of this stack"""
        self.list.append(item)  # Runtime analysis: avg O(1)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty"""
        if self.is_empty():
            return None
        else:
            return self.list[-1]

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty"""
        if self.is_empty():
            raise ValueError('Stack is empty')
        else:
            top_item = self.peek()
            self.list.remove(top_item)
            return top_item


# implement LinkedStack and ArrayStack above, then change the assignment below
# to use each of your Stack implementations to verify they each pass all tests
Stack = LinkedStack
# Stack = ArrayStack
