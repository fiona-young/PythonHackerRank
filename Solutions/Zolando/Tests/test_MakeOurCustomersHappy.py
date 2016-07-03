import io
import sys
from unittest import TestCase

from Solutions.Zolando import main


class TestSolution(TestCase):
    def test_initial_case(self):
        input_string = '''2 1 1
3
A
A,B
C,A
'''

        result = '''2
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

