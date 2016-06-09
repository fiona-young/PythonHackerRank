import io
import sys
from unittest import TestCase

from Solutions.Section2 import main


#from Tests.MinimumPenaltyPathOther import main

class TestMinimumPenaltyPath(TestCase):
    def test_initial_case(self):
        input_string = '''3 4
1 2 1
1 2 1000
2 3 3
1 3 100
1 3
'''

        result = '''3
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())



    def test_case1(self):
        file_input = open('test_MinPP1.in')
        sys.stdin = file_input
        sys.stdout = io.StringIO()
        main()
        self.assertEqual("183", sys.stdout.getvalue().strip())

    def test_case2(self):
        file_input = open('test_MinPP2.in')
        sys.stdin = file_input
        sys.stdout = io.StringIO()
        main()
        self.assertEqual("95", sys.stdout.getvalue().strip())

    def test_duplicate_case(self):
        input_string = '''4 5
1 2 1
1 2 2
2 3 10
3 4 1
3 4 2
1 4
'''

        result = '''10
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())

    def test_duplicate_case1(self):
        input_string = '''8 9
1 2 1
1 3 2
2 4 1
3 4 2
4 5 10
5 6 1
5 7 2
6 8 1
7 8 2
1 8
'''

        result = '''10
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())