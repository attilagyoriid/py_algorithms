from unittest import TestCase

from data_structures.queue_with_stacks import QueueWithStacks


class TestQueueWithStacks(TestCase):
    def test_enqueue(self):
        qws = QueueWithStacks()
        qws.enqueue(1)
        self.assertTrue(1, qws.dequeue())
