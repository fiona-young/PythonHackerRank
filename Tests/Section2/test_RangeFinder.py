from unittest import TestCase
import Section2.RangeFinder


class TestRangeFinder(TestCase):
    def test_initial_case(self):
        test_subject = Section2.RangeFinder.RangeFinder()
        for i in [13, 3, 14, 18, 1, 9, 7, 10, 4, 2, 11, 15, 12, 8]:
            test_subject.add(i)
        self.assertEquals(3,test_subject.range_count(2,5))
        self.assertEquals(4,test_subject.range_count(2,7))
        self.assertEquals(5,test_subject.range_count(0,7))
        self.assertEquals(14,test_subject.range_count(0,20))

    def test_second_case(self):
        test_subject = Section2.RangeFinder.RangeFinder()
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
