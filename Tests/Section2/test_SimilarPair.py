from unittest import TestCase
import sys
import io
from Section2.SimilarPair import main


class TestCutTheTree(TestCase):
    def test_initial_case(self):
        input_string = '''5 2
3 2
3 1
1 4
1 5
'''

        result = '''4
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())

    def test_case_file1(self):
        file_input = open('test_SimilarPair.in')
        sys.stdin = file_input
        sys.stdout = io.StringIO()
        main()
        self.assertEqual("3628", sys.stdout.getvalue().strip())
