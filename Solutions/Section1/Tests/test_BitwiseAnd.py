import io
import sys
from unittest import TestCase

from Solutions.Section1.BitwiseAnd import main


class TestBitwiseAnd(TestCase):
    def test_initial_case(self):
        input_string = '''3
5 2
8 5
2 2
'''

        result = '''1
4
0
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())
