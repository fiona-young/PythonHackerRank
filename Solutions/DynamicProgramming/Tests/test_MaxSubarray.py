import io
import sys
from unittest import TestCase

from Solutions.DynamicProgramming import main


class TestSolution(TestCase):
    def test_initial_case(self):
        input_string = '''2
4
1 2 3 4
6
2 -1 2 3 4 -5
'''

        result = '''10 10
10 11
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())

    def test_case1(self):
        input_string = '''6
1
1
6
-1 -2 -3 -4 -5 -6
2
1 -2
3
1 2 3
1
-10
6
1 -1 -1 -1 -1 5
'''

        result = '''1 1
-1 -1
1 1
6 6
-10 -10
5 6
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())

    def test_file1(self):
        result = '''2617065 172083036
1274115 193037987
2202862 163398048
2454939 240462364
3239908 186256172
2486039 202399661
1092777 137409985
962621 135978139
3020911 224370860
1755033 158953999
'''
        file_input = open('test_MaxSubarray1.in')
        sys.stdin = file_input
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue().strip())


