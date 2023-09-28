import unittest

from main import subarray

class TestFindUnsortedSubarray(unittest.TestCase):
    def test_sorted_array(self):
        nums = [1, 2, 3, 4, 5]
        self.assertEqual(subarray(nums), (-1, -1))

    def test_reverse_sorted_array(self):
        nums = [1, 2, 3, 4, 5]
        self.assertEqual(subarray(nums, True), (0, 4))

    def test_reverse_array(self):
        nums = [5, 4, 3, 2, 1]
        self.assertEqual(subarray(nums), (0, 4))

    def test_partially_sorted_array(self):
        nums = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
        self.assertEqual(subarray(nums), (3, 9))

    def test_partially_sorted_reverse_array(self):
        nums = [19, 18, 16, 7, 6, 12, 7, 11, 10, 7, 4, 2, 1]
        self.assertEqual(subarray(nums, True), (3, 9))

    def test_single_element_array(self):
        nums = [39]
        self.assertEqual(subarray(nums), (-1, -1))

if __name__ == '__main__':
    unittest.main()