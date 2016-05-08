from Section1.MinHeap import MinHeap
from unittest import TestCase


class TestMatrix(TestCase):
    def test_min_heap_query(self):
        test_subject = MinHeap()
        test_subject.add(5)
        self.assertEqual(test_subject.query(), 5)
        test_subject.add(7)
        test_subject.add(8)
        self.assertEqual(test_subject.query(), 5)
        test_subject.add(4)
        self.assertEqual(test_subject.query(), 4)

    def test_min_heap_extract(self):
        test_subject = MinHeap()
        test_subject.add(5)
        self.assertEqual(test_subject.query(), 5)
        test_subject.add(7)
        test_subject.add(8)
        self.assertEqual(test_subject.query(), 5)
        self.assertEqual(test_subject.extract(), 5)
        self.assertEqual(test_subject.query(), 7)
        test_subject.add(4)
        self.assertEqual(test_subject.query(), 4)
        self.assertEqual(test_subject.extract(), 4)
        self.assertEqual(test_subject.extract(), 7)
        self.assertEqual(test_subject.extract(), 8)