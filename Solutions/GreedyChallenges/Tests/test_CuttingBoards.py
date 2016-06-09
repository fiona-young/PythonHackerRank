import io
import sys
from unittest import TestCase

from Solutions.GreedyChallenges.CuttingBoards import main


class TestSolution(TestCase):
    def test_initial_case(self):
        input_string = '''1
2 2
2
1
'''

        result = '''4
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())

    def test_case1(self):
        input_string = '''1
6 4
2 1 3 1 4
4 1 2
'''

        result = '''42
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


