import io
import sys
from unittest import TestCase

from Solutions.Section2.MissingNumbers import main


class TesMissingNumbers(TestCase):
    def test_initial_case(self):
        input_string = '''10
203 204 205 206 207 208 203 204 205 206
13
203 204 204 205 206 207 205 208 203 206 205 206 204
'''

        result = '''204 205 206
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())



    def test_case1(self):
        input_string = '''10
203 204 205 206 206 203 204 205 206
13
203 204 204 205 206 207 205 208 203 206 205 206 204
'''

        result = '''204 205 207 208
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())

    def test_case2(self):
        file_input = open('test_MissingNumbers.in')
        sys.stdin = file_input
        sys.stdout = io.StringIO()
        main()
        self.assertEqual("7251 7259 7276 7279 7292 7293", sys.stdout.getvalue().strip())

