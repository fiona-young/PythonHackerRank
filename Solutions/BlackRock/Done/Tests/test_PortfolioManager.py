import io
import sys
from unittest import TestCase

from Solutions.BlackRock.Done.PortfolioManager import main


class TestSolution(TestCase):
    def test_initial_case(self):
        input_string = '''5
1 2 3 # # 4 # # 5
'''

        result = '''3
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())


    def test_case1(self):
        input_string = '''6
3 4 5 1 3 # 1 s

'''

        result = '''9
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())

    def test_case2(self):
        input_string = '''6
3 4 5 2 3 # 1
'''

        result = '''10
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())

    def test_case3(self):
        input_string = '''6
3 4 5 2 3 # 1 2 4 5
'''

        result = '''10
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())

    def test_case4(self):
        input_string = '''0
'''

        result = '''0
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


