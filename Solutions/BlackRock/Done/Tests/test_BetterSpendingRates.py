import io
import sys
from unittest import TestCase

from Solutions.BlackRock.Done.BetterSpending import main


class TestSolution(TestCase):
    def test_initial_case(self):
        input_string = '''5000 5.5 3 1
29 42 37
'''

        result = '''4083.843
4091.584 - 28 42 38
4091.494 - 28 43 37
4084.348 - 29 41 38
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())

    def test_case2(self):
        input_string = '''100000 5.5 20 15
99 27 96 29 32 74 85 1 43 37 32 56 46 8 48 85 1 37 79 94
'''

        result = '''114
0
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())

    def test_case3(self):
        input_string = '''5000 5.5 3 2
45 30 36
'''

        result = '''4105.745
4114.278 - 45 28 38
4112.555 - 46 28 37
4111.845 - 44 29 38
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


