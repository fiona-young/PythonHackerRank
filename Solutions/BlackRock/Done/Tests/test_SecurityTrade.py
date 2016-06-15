import io
import sys
from unittest import TestCase

from Solutions.BlackRock.Done.SecurityTrade import main


class TestSolution(TestCase):
    def test_initial_case(self):
        input_string = '''2
10 2 40
p1 16
p2 134
'''

        result = '''p1 0
p2 40
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())


    def test_case1(self):
        input_string = '''3
10 2 60
p1 20
p2 20
p3 20
'''

        result = '''p1 20
p2 20
p3 20
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())

    def test_case2(self):
        input_string = '''5
14 5 999
p01 364
p02 179
p03 354
p04 334
p05 119
'''

        result = '''p01 364
p02 0
p03 354
p04 0
p05 0
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())

    def test_case3(self):
        input_string = '''3
10 2 20
p1 20
p2 20
p3 20
'''

        result = '''p1 10
p2 0
p3 10
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())

    def test_case4(self):
        input_string = '''3
9 2 27
p1 20
p2 20
p3 20
'''

        result = '''p1 9
p2 9
p3 9
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


