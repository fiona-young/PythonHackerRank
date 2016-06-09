import io
import sys
from unittest import TestCase

from Solutions.Section2.SherlockAndArray import main


class TestSherlockAndArray(TestCase):
    def test_initial_case(self):
        input_string = '''2
3
1 2 3
4
1 2 3 3
'''

        result = '''NO
YES
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())
