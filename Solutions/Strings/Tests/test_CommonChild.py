import io
import sys
from unittest import TestCase

from Solutions.Strings.CommonChild import main


class TestSolution(TestCase):
    def test_initial_case(self):
        input_string = '''PRESENTS
SERPENTS
'''

        result = '''5
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())

    def test_case4(self):
        input_string = '''TERRACED
CRATERED
'''

        result = '''5
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())

    def test_case2(self):
        input_string = '''HARRY
SALLY
'''

        result = '''2
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())

    def test_case_file1(self):
        file_input = open('commonChild.in')
        result = '''1618
'''
        sys.stdin = file_input
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result.strip(), sys.stdout.getvalue().strip())


