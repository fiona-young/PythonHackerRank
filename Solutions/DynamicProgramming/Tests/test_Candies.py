import io
import sys
from unittest import TestCase

from Solutions.DynamicProgramming import main


class TestSolution(TestCase):
    def test_initial_case(self):
        input_string = '''3
1
2
2
'''

        result = '''4
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())

    def test_case1(self):
        input_string = '''10
2
4
2
6
1
7
8
9
2
1
'''

        result = '''19
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())

    def test_case2(self):
        input_string = '''10
9
8
7
6
5
5
4
3
2
1
'''

        result = '''30
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())

    def test_case3(self):
        input_string = '''10
1
2
3
1
5
5
4
3
2
1
'''

        result = '''24
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())

    def test_file_case1(self):
        file_input = open('test_Candies1.in')
        sys.stdin = file_input
        sys.stdout = io.StringIO()
        main()
        self.assertEqual('160929', sys.stdout.getvalue().strip())

    def test_file_case2(self):
        file_input = open('test_Candies2.in')
        sys.stdin = file_input
        sys.stdout = io.StringIO()
        main()
        self.assertEqual('5000050000', sys.stdout.getvalue().strip())


