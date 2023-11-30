import unittest

from lab6.src.KMP_search import KMPSearch


class TestKMPSearch(unittest.TestCase):
    def test_kmp_search_basic(self):
        haystack = "ABABDABACDABABCABAB"
        needle = "ABABCABAB"
        result = KMPSearch(needle, haystack)
        self.assertEqual(result, [10])

    def test_kmp_search_multiple_occurrences(self):
        haystack = "AABAACAADAABAABA"
        needle = "AABA"
        result = KMPSearch(needle, haystack)
        self.assertEqual(result, [0, 9, 12])

    def test_kmp_search_no_occurrence(self):
        haystack = "ABCDEF"
        needle = "XYZ"
        result = KMPSearch(needle, haystack)
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
