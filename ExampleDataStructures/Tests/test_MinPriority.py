from unittest import TestCase

from ExampleDataStructures.MinPriority import MinPriority


class TestMinPriority(TestCase):
    def test_min_priority_query(self):
        test_subject = MinPriority()
        test_subject.add(5,"five")
        self.assertEqual(test_subject.query(), "five")
        test_subject.add(7,"seven")
        test_subject.add(8,"eight")
        self.assertEqual(test_subject.query(), "five")
        test_subject.add(4,"four")
        self.assertEqual(test_subject.query(), "four")

    def test_min_heap_extract(self):
        test_subject = MinPriority()
        test_subject.add(5,"five")
        self.assertEqual(test_subject.query(), "five")
        test_subject.add(7,"seven")
        test_subject.add(8,"eight")
        self.assertEqual(test_subject.query(), "five")
        self.assertEqual(test_subject.extract(), "five")
        self.assertEqual(test_subject.query(), "seven")
        test_subject.add(4,"four")
        self.assertEqual(test_subject.query(), "four")
        self.assertEqual(test_subject.extract(), "four")
        self.assertEqual(test_subject.extract(), "seven")
        self.assertEqual(test_subject.extract(), "eight")