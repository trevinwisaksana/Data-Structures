#!python

from hashset import HashSet
import unittest

class HashSetTest(unittest.TestCase):

    def test_init(self):
        hs = HashSet()
        assert hs.size == 0

    def test_size(self):
        hs = HashSet()
        assert hs.size == 0
        hs.add('I')
        assert hs.size == 1
        hs.add('V')
        assert hs.size == 2
        hs.add('X')
        assert hs.size == 3

    def test_contains(self):
        hs = HashSet()
        hs.add('I')
        hs.add('V')
        hs.add('X')
        assert hs.contains('I') is True
        assert hs.contains('V') is True
        assert hs.contains('X') is True

    def test_remove(self):
        hs = HashSet()
        hs.add('I')
        hs.add('V')
        hs.add('X')
        assert hs.size == 3
        hs.remove('I')
        hs.remove('X')
        assert hs.size == 1
        with self.assertRaises(KeyError):
            hs.remove('X')  # Key no longer exists
        with self.assertRaises(KeyError):
            hs.remove('A')  # Key does not exist

    def test_union(self):
        hs = HashSet()
        hs.add('A')
        hs.add('B')
        hs.add('C')
        other_set = HashSet()
        other_set.add('D')
        other_set.add('E')
        other_set.add('F')
        new_set = hs.union(other_set)
        # Asserting the values of each element is difficult as it
        # is sorted by an arbitrary value
        # assert hs.set.items() == ['A', 'B', 'C', 'D', 'E', 'F']
        assert new_set.size == 6

    def test_intersection(self):
        hs = HashSet()
        hs.add('A')
        hs.add('B')
        hs.add('C')
        other_set = HashSet()
        other_set.add('A')
        other_set.add('B')
        other_set.add('F')
        assert hs.intersection(other_set) == ['A', 'B']

    def test_difference(self):
        hs = HashSet()
        other_set = HashSet()
        hs.add('A')
        hs.add('B')
        hs.add('C')
        other_set.add('A')
        other_set.add('B')
        other_set.add('F')
        difference = hs.difference(other_set)
        assert difference.keys() == ['C', 'F']

    def test_is_subset(self):
        hs = HashSet()
        other_set = HashSet()
        hs.add('A')
        hs.add('B')
        hs.add('C')
        hs.add('D')
        other_set.add('A')
        other_set.add('B')
        other_set.add('C')
        assert hs.is_subset(other_set) == True


if __name__ == '__main__':
    unittest.main()
