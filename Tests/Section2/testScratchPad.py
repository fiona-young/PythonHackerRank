from unittest import TestCase
from Section2.ScratchPad import FenwickRangeFinder, Fenwick
import random


class TestScratchPad(TestCase):
    def test_fenwick_range(self):
        test_subject = FenwickRangeFinder(20)
        for i in [13, 3, 14, 18, 1, 9, 7, 10, 4, 2, 11, 15, 12, 8]:
            test_subject.add(i)
        self.assertEquals(3,test_subject.range_count(2,5))
        self.assertEquals(4,test_subject.range_count(2,7))
        self.assertEquals(5,test_subject.range_count(0,7))
        self.assertEquals(14,test_subject.range_count(0,20))

    def test_fenwick_tree2(self):
        test_subject = Fenwick(11)
        for key,value in enumerate([3, 2, -1, 6, 5, 4, -3, 3, 7, 2, 3]):
            test_subject.update(key, value)
        for key,expected_value in enumerate([3, 5, 4, 10, 15, 19, 16, 19, 26, 28, 31]):
            self.assertEquals(expected_value,test_subject.query(key))
        test_subject.update(3,10)
        for key,expected_value in enumerate([3, 5, 4, 14, 19, 23, 20, 23, 30, 32, 35]):
            self.assertEquals(expected_value,test_subject.query(key))


