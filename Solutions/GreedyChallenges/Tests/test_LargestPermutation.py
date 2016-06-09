import io
import sys
from unittest import TestCase

from Solutions.GreedyChallenges import main


class TestSolution(TestCase):
    maxDiff=None
    def test_initial_case(self):
        input_string = '''5 1
4 2 3 5 1
'''

        result = '''5 2 3 4 1
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())

    def test_case1(self):
        input_string = '''3 1
2 1 3
'''

        result = '''3 1 2
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())

    def test_case2(self):
        input_string = '''2 1
2 1
'''

        result = '''2 1
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())


    def test_case3(self):
        input_string = '''6 6
5 4 3 2 1 1
'''

        result = '''5 4 3 2 1 1
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())


    def test_case4(self):
        input_string = '''6 6
7 4 3 1 6 2
'''

        result = '''7 6 4 3 2 1
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())

    def test_case_file1(self):
        file_input = open('test_LargestPermutation.in')
        expected_output = open('test_LargestPermutation.out')
        sys.stdin = file_input
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(expected_output.read().strip(), sys.stdout.getvalue().strip())

