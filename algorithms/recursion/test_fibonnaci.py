from unittest import TestCase

from algorithms.recursion.fibonnaci import Fibonnaci


class TestFibonnaci(TestCase):
    def test_calculate(self):
        f = Fibonnaci()
        self.assertEqual(3, f.calculate(4))
