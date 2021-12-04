from unittest import TestCase

from data_structures.deque import Deque


class TestDeque(TestCase):
    def test_add_front(self):
        deque = Deque()
        deque.add_front("1")
        self.assertEqual(1, deque.size())
        self.assertEqual("1", deque.remove_front())

    def test_add_rear(self):
        deque = Deque()
        deque.add_rear("1")
        self.assertEqual(1, deque.size())
        self.assertEqual("1", deque.remove_rear())

    def test_is_empty(self):
        deque = Deque()
        self.assertTrue(deque.is_empty())
        deque.add_rear("1")
        self.assertFalse(deque.is_empty())
        deque.remove_rear()
        self.assertTrue(deque.is_empty())