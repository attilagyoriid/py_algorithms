from unittest import TestCase

from algorithms.recursion.fibonacci import Fibonacci


class TestFibonacci(TestCase):
    def test_calculate(self):
        f = Fibonacci()
        self.assertEqual(3, f.calculate(4))
