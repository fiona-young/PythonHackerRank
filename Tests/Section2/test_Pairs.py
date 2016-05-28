from unittest import TestCase
import sys
import io
from Section2.Pairs import main


class TestCutTheTree(TestCase):
    def test_initial_case(self):
        input_string = '''5 2
1 5 3 4 2
'''

        result = '''3
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())

