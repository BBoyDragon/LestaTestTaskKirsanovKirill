import unittest

from Task2.Buffers.CycleBufferArray import CycleBufferArray


class TestCycleBufferArray(unittest.TestCase):
    def setUp(self):
        self.buffer = CycleBufferArray(3)

    def test_enqueue(self):
        self.buffer.enqueue(1)
        self.buffer.enqueue(2)
        self.buffer.enqueue(3)
        self.assertEqual(self.buffer.pic(), 1)
        self.assertEqual(self.buffer._count, 3)

    def test_enqueue_overflow(self):
        self.buffer.enqueue(1)
        self.buffer.enqueue(2)
        self.buffer.enqueue(3)
        self.buffer.enqueue(4)
        self.assertEqual(self.buffer.pic(), 2)
        self.assertEqual(self.buffer._count, 3)

    def test_dequeue(self):
        self.buffer.enqueue(1)
        self.buffer.enqueue(2)
        self.buffer.enqueue(3)
        self.assertEqual(self.buffer.dequeue(), 1)
        self.assertEqual(self.buffer.dequeue(), 2)
        self.assertEqual(self.buffer._count, 1)

    def test_is_empty(self):
        self.assertTrue(self.buffer.is_empty())
        self.buffer.enqueue(1)
        self.assertFalse(self.buffer.is_empty())

    def test_pic(self):
        self.assertIsNone(self.buffer.pic())
        self.buffer.enqueue(1)
        self.assertEqual(self.buffer.pic(), 1)
        self.buffer.enqueue(2)
        self.assertEqual(self.buffer.pic(), 1)


if __name__ == '__main__':
    unittest.main()
