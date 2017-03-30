#!python

from string_search import find, find_index, find_all_indexes
import unittest


class TestPalindromes(unittest.TestCase):

    def test_find_with_pattern_strings(self):
        # simple patterns
        assert find('Hello', 'll') is True
        assert find('A') is True
        assert find('BB') is True
        assert find('LOL') is True
        assert find('noon') is True
        assert find('radar') is True
        assert find('racecar') is True

    def test_find_with_non_patterned_strings(self):
        # simple patterns
        assert find('abksdf', 'aa') is False
        assert find('A') is True
        assert find('BB') is True
        assert find('LOL') is True
        assert find('noon') is True
        assert find('radar') is True
        assert find('racecar') is True


if __name__ == '__main__':
    unittest.main()
