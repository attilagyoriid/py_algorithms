from unittest import TestCase

from algorithms.array_element_finder import ArrayElementFinder


class TestArrayElementFinder(TestCase):
    def test_find_first_non_matching_element(self):
        self.assertEqual(ArrayElementFinder.find_first_non_matching_element([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6]), 5)
