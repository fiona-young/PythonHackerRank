import io
import sys
from unittest import TestCase

from Solutions.Codesprint2.Skeleton import main


class TestSolution(TestCase):
    def test_initial_case(self):
        input_string = '''    7 10 3
    1 4 3
    2 4 3
    2 3 2
    2 5 4
    4 6 6
    5 7 7
    1 2 1
    2 6 2
    1 6 2
    6 7 3
    1 7 5
    3 4 5
    3 6 2

'''

        result = '''17
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())

 #   def test_case1(self):
 #       file_input = open('GridChallenge.in')
 #       expected_output = open('GridChallenge.out')
 #       sys.stdin = file_input
 #       sys.stdout = io.StringIO()
 #       main()
 #       self.assertEqual(expected_output.read().strip(), sys.stdout.getvalue().strip())


