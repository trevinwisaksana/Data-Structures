#!python

from hashtable import HashTable


class HashSet(object):

    def __init__(self, elements=None):
        """Initialize this hash set"""
        self.set = HashTable()
        self.size = 0  # Count number of element entries
        if elements:
            for item in elements:
                self.add(item)

    def keys(self):
        return self.set.keys()

    def contains(self, element):
        """Check whether element is in this set"""
        # Uses the built in contains method, returns True or False
        return self.set.contains(element)

    def add(self, element):
        """Add element to this set, if not present already"""
        # Adding the element to the set
        self.set.set(key=element, value=None)
        # Increment the size
        self.size += 1

    def remove(self, element):
        """Remove element from this set, if present"""
        # Removing the item
        self.set.delete(element)
        # Decrementing the size
        self.size -= 1

    def union(self, other_set):
        """Return the union of this set and other_set"""
        # Creating a new set
        new_set = HashSet()
        # Getting the elements from the other_set
        other_set_elements = other_set.set.keys()
        # Adding all the elements to the new_set
        for element in other_set_elements:
            new_set.add(element)
        # Adding all the elements within the current set to the new_set
        for element in self.set:
            new_set.add(element)
        return new_set

    def intersection(self, other_set):
        """Return the intersection of this set and other_set"""
        # Contains the elements that are common
        common_elements = []
        # Getting the elements from the other_set
        other_set_elements = other_set.set.keys()
        # HashSet current elements
        hash_set_elements = self.set.keys()
        # Iterate through the list
        for element in other_set_elements:
            if element in hash_set_elements:
                common_elements.append(element)
        return common_elements

    def difference(self, other_set):
        """Return the difference of this set and other_set"""
        # Contains the elements that are common
        common_elements = HashSet()
        # Getting the elements from the other_set
        other_set_elements = other_set.set.keys()
        # Getting the elements from current set
        current_set_elements = self.set.keys()
        # Iterate through the list
        for element in other_set_elements:
            if element not in current_set_elements:
                common_elements.add(element)
        # Iterathe through the second list
        for element in current_set_elements:
            if element not in other_set_elements:
                common_elements.add(element)
        return common_elements

    def is_subset(self, other_set):
        """Check whether other_set is a subset of this set"""
        # Check if an element is not in there
        other_set_elements = other_set.keys()
        # Loop through the other_set_elements
        for element in other_set_elements:
            if element not in self.keys():
                return False
        return True
