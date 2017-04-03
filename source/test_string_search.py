#!python

from string_search import find, find_index, find_all_indexes
import unittest


class TestPalindromes(unittest.TestCase):

    def test_find_with_pattern_strings(self):
        # simple patterns
        assert find('Hello', 'll') is True
        assert find('Trevin', 'vin') is True

    def test_find_with_non_patterned_strings(self):
        # simple patterns
        assert find('abksdf', 'aa') is False
        assert find('', 'aa') is False

    def test_find_index_with_pattern_strings(self):
        # simple patterns
        assert find('Hello', 'll') == 2
        assert find('Trevin', 'vin') == 2

    def test_find_index_with_non_patterned_strings(self):
        # simple patterns
        assert find('abksdf', 'aa') == None
        assert find('', 'aa') == None


if __name__ == '__main__':
    unittest.main()
