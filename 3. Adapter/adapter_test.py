# File: adapter_test.py

from unittest import TestCase, main
from simple_queue import SimpleQueue
from queue_to_stack_adapter import QueueToStackAdapter


class TestQueueToStackAdapter(TestCase):

    def test_queue_to_stack_adapter(self):
        q = SimpleQueue()
        qsa = QueueToStackAdapter(q)
        self.assertTrue(q.is_empty())
        self.assertTrue(qsa.is_empty())
        self.assertIsNone(qsa.pop())
        self.assertIs(qsa, qsa.push('Foo'))
        self.assertEqual('Foo', qsa.peek())
        self.assertFalse(q.is_empty())
        self.assertFalse(qsa.is_empty())
        self.assertIs(qsa, qsa.push('Bar'))
        self.assertEqual('Bar', qsa.peek())
        self.assertEqual(qsa, qsa.push('Baz').push('Quux'))
        self.assertEqual(4, q.size())
        self.assertEqual(4, qsa.size())
        self.assertEqual('Quux', qsa.peek())
        self.assertEqual('Quux', qsa.pop())
        self.assertEqual('Baz', qsa.peek())
        self.assertEqual('Baz', qsa.pop())
        self.assertEqual('Bar', qsa.peek())
        self.assertEqual('Bar', qsa.pop())
        self.assertEqual('Foo', qsa.peek())
        self.assertIs(qsa, qsa.push('Goo'))
        self.assertEqual('Goo', qsa.peek())
        self.assertEqual('Goo', qsa.pop())
        self.assertEqual('Foo', qsa.peek())
        self.assertEqual(1, qsa.size())
        self.assertEqual('Foo', qsa.pop())
        self.assertIsNone(qsa.peek())
        self.assertIsNone(qsa.pop())
        self.assertTrue(q.is_empty())
        self.assertTrue(qsa.is_empty())
        self.assertEqual(0, q.size())
        self.assertEqual(0, qsa.size())


if __name__ == '__main__':
    main()
