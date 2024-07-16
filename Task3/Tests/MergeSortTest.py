import unittest

from Task3.Sort import mergesort


class TestMergeSort(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(mergesort([]), [])

    def test_single_element_list(self):
        self.assertEqual(mergesort([5]), [5])

    def test_sorted_list(self):
        self.assertEqual(mergesort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        self.assertEqual(mergesort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_random_list(self):
        self.assertEqual(mergesort([64, 25, 12, 22, 11]), [11, 12, 22, 25, 64])

    def test_duplicate_elements(self):
        self.assertEqual(mergesort([5, 2, 5, 1, 2, 0]), [0, 1, 2, 2, 5, 5])

    def test_large_list(self):
        self.assertEqual(mergesort(list(range(100, 0, -1))), list(range(1, 101)))


if __name__ == '__main__':
    unittest.main()