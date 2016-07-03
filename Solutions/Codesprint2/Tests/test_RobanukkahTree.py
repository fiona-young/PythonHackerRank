import io
import sys
from unittest import TestCase

from Solutions.Codesprint2.RobanukkahTree import main, get_choose_cat_from_slots


class TestRobanukkahTree(TestCase):
    def test_initial_case(self):
        input_string = '''3 3 2
4 6
1 1
'''

        result = '''408
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())

    def test_single(self):
        input_string = '''1 3 2
4 6
'''

        result = '''172800
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())

    def test_choose(self):
        self.assertEqual(15,get_choose_cat_from_slots(4,3))
        self.assertEqual(20,get_choose_cat_from_slots(3,4))
 #   def test_case1(self):
 #       file_input = open('GridChallenge.in')
 #       expected_output = open('GridChallenge.out')
 #       sys.stdin = file_input
 #       sys.stdout = io.StringIO()
 #       main()
 #       self.assertEqual(expected_output.read().strip(), sys.stdout.getvalue().strip())


