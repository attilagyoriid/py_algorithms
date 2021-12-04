from unittest import TestCase

from algorithms.stack.balanced_parenthesis import BalancedParenthesis


class TestBalancedParenthesis(TestCase):
    def test_check_happy(self):
        parenthesis = '[](){([[[]]])}'
        self.assertTrue(BalancedParenthesis.check(parenthesis))

    def test_check_fail(self):
        parenthesis = '[]({)([[[]]])}'
        self.assertFalse(BalancedParenthesis.check(parenthesis))
