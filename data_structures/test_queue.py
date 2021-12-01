from unittest import TestCase

from data_structures.queue import Queue


class TestQueue(TestCase):
    def test_enqueue(self):
        queue = Queue()
        queue.enqueue("item1")
        queue.enqueue("item2")
        self.assertEqual(2, queue.size())

    def test_dequeue(self):
        queue = Queue()
        item = "item1"
        queue.enqueue(item)
        self.assertEqual(item, queue.dequeue())

    def test_is_empty(self):
        queue = Queue()
        self.assertTrue(queue.is_empty())
