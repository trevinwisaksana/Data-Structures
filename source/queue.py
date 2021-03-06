#!python

from linkedlist import LinkedList


# implement LinkedQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class LinkedQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any"""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue"""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise"""
        if self.list.is_empty():
            return True
        else:
            return False

    def length(self):
        """Return the number of items in this queue"""
        return self.list.size

    def enqueue(self, item):
        """Insert the given item at the back of this queue"""
        # We append because its faster
        self.list.append(item)

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty"""
        if self.is_empty():
            return None
        else:
            return self.list.head.data

    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty"""
        if self.is_empty():
            raise ValueError("Queue is empty")
        else:
            item_in_front = self.front()
            self.list.delete(item_in_front)
            return item_in_front


# implement ArrayQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class ArrayQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any"""
        # Initialize a new dynamic array to store the items
        self.list = list()
        if iterable:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue"""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise"""
        if self.length() == 0:
            return True
        else:
            return False

    def length(self):
        """Return the number of items in this queue"""
        return len(self.list)

    def enqueue(self, item):
        """Insert the given item at the back of this queue"""
        self.list.append(item)

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty"""
        if self.is_empty():
            return None
        else:
            front_item = self.list[0]
            return front_item

    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty"""
        if self.is_empty():
            raise ValueError("Queue is empty")
        else:
            front_item = self.front()
            self.list.remove(front_item)
            return front_item


# implement LinkedQueue and ArrayQueue above, then change the assignment below
# to use each of your Queue implementations to verify they each pass all tests
Queue = LinkedQueue
# Queue = ArrayQueue
