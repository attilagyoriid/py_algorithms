from unittest import TestCase

from algorithms.string_manipulation import StringManipulator


class TestStringManipulator(TestCase):
    def test_reverse_string(self):
        self.assertEqual("?uoy era woh ereht ,olleH", StringManipulator.reverse_string("Hello, there how are you?"))

    def test_reverse_word_order(self):
        self.assertEqual("you are how there Hello", StringManipulator.reverse_word_order("Hello there how are you"))



