from unittest import TestCase

from algorithms.recursion.reverse_string import ReverseString


class TestReverseString(TestCase):
    def test_reverse(self):

        expected = "abcde"
        rev = ReverseString()
        self.assertEqual(expected, rev.reverse("edcba"))
