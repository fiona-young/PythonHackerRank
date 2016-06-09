import io
import sys
from unittest import TestCase

from Solutions.Zolando import main


class TestSolution(TestCase):
    def test_initial_case(self):
        input_string = '''11
1 150 0
1 3 10
2 40
1 143 59
2 59
1 100 60
2 60
1 159 61
2 61
2 120
2 121
'''

        result = '''150
150
143
159
159
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


