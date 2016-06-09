import random
from unittest import TestCase

import ExampleDataStructures.RangeFinder


class TestRangeFinder(TestCase):
    def test_initial_case(self):
        test_subject = ExampleDataStructures.RangeFinder.RangeFinder()
        for i in [13, 3, 14, 18, 1, 9, 7, 10, 4, 2, 11, 15, 12, 8]:
            test_subject.add(i)
        self.assertEquals(3,test_subject.range_count(2,5))
        self.assertEquals(4,test_subject.range_count(2,7))
        self.assertEquals(5,test_subject.range_count(0,7))
        self.assertEquals(14,test_subject.range_count(0,20))

    def test_second_case(self):
        test_subject = ExampleDataStructures.RangeFinder.RangeFinder()
        for i in [13, 3, 14, 18, 1, 9, 7, 10, 4, 2, 15, 12, 8, 11]:
            test_subject.add(i)
        test_subject.remove(13)
        test_subject.remove(7)
        test_subject.remove(10)
        test_subject.remove(11)
        self.assertEquals(3,test_subject.range_count(2,5))
        self.assertEquals(3,test_subject.range_count(2,7))
        self.assertEquals(4,test_subject.range_count(0,7))
        self.assertEquals(10,test_subject.range_count(0,20))

    def test_list_case(self):
        test_subject = ExampleDataStructures.RangeFinder.RangeFinder()
        my_list =  list(range(10,91))
        random.shuffle(my_list)
        my_list = [44, 15, 25, 26, 59, 54, 55, 18, 29, 47, 22, 89, 88, 11, 20, 66, 13, 51, 78, 69, 81, 61, 46, 56, 64,
                   52, 37, 23, 73, 10, 63, 16, 85, 43, 70, 87, 84, 14, 90, 76, 58, 34, 53, 71, 35, 41, 49, 72, 36, 38,
                   39, 24, 21, 33, 30, 77, 27, 32, 12, 65, 67, 19, 86, 42, 83, 57, 62, 28, 45, 48, 50, 79, 60, 80, 68,
                   82, 40, 74, 75, 17, 31]
        for i in my_list:
            test_subject.add(i)
        my_list_remove = list(range(30,40))
        random.shuffle(my_list_remove)
        my_list_remove = [38, 33, 32, 39, 30, 35, 37, 36, 34, 31]
        for i in my_list_remove:
            if i == 37:
                a = 1
            test_subject.remove(i)
        self.assertEquals(0,test_subject.range_count(2,5))
        self.assertEquals(6,test_subject.range_count(2,15))
        self.assertEquals(13,test_subject.range_count(78,100))
        self.assertEquals(71,test_subject.range_count(0,100))
