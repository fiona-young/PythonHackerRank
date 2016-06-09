import io
import sys
from unittest import TestCase

from Solutions.Section1.NestedLogic import main


class TestEvenTree(TestCase):
    def test_initial_case(self):
        input_string = '''9 6 2015
6 6 2015
'''

        result = '''45
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())
