from unittest import TestCase

from data_structures.stack import Stack


class TestStack(TestCase):
    def test_push(self):
        stack = Stack()
        stack.push("item1")
        stack.push("item2")
        self.assertEqual(2, stack.size())

    def test_pop(self):
        stack = Stack()
        item = "item1"
        stack.push(item)
        self.assertEqual(item, stack.pop())
        self.assertEqual(0, stack.size())

    def test_peek(self):
        stack = Stack()
        item = "item1"
        stack.push(item)
        self.assertEqual(item, stack.peek())
        self.assertEqual(1, stack.size())

    def test_is_empty(self):
        stack = Stack()
        item = "item1"
        self.assertTrue(stack.is_empty())
        stack.push(item)
        self.assertFalse(stack.is_empty())
