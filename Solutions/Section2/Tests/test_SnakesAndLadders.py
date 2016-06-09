import io
import sys
from unittest import TestCase

from Solutions.Section2 import main


class TestMinimumPenaltyPath(TestCase):
    def test_initial_case(self):
        input_string = '''2
3
32 62
42 68
12 98
7
95 13
97 25
93 37
79 27
75 19
49 47
67 17
4
8 52
6 80
26 42
2 72
9
51 19
39 11
37 29
81 3
59 5
79 23
53 7
43 33
77 21
'''

        result = '''3
5
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())
