from unittest import TestCase
import sys
import io
from Section2.CutTheTree import main


class TestCutTheTree(TestCase):
    def test_initial_case(self):
        input_string = '''6
100 200 100 500 100 600
1 2
2 3
2 5
4 5
5 6
'''

        result = '''400
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())

    def test_case_file1(self):
        file_input = open('test_CutTheTree1.in')
        sys.stdin = file_input
        sys.stdout = io.StringIO()
        main()
        self.assertEqual("3628", sys.stdout.getvalue().strip())
