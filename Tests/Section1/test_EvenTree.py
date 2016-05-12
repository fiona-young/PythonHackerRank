from unittest import TestCase
import sys
import io
from Section1.EvenTree import main


class TestEvenTree(TestCase):
    def test_initial_case(self):
        input_string = '''10 9
2 1
3 1
4 3
5 2
6 1
7 2
8 6
9 8
10 8
'''

        result = '''2
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())
