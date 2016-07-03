import io
import sys
from unittest import TestCase

from Solutions.Codesprint2.Finished.AorB import main


class TestSolution(TestCase):
    def test_initial_case(self):
        input_string = '''3
8
2B
9F
58
5
B9
40
5A
2
91
BE
A8
'''

        result = '''8
58
18
42
-1
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


