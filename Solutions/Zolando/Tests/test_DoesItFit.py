import io
import sys
from unittest import TestCase

from Solutions.Zolando import main


class TestSolution(TestCase):
    def test_initial_case(self):
        input_string = '''4 5
3
R 1 2
R 5 5
C 2
'''

        result = '''YES
NO
YES
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())

    def test_case1(self):
        input_string = '''900 500
2
R 1053 27
C 251
'''

        result = '''YES
NO
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


