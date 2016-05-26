from unittest import TestCase
import sys
import io
from Section2.IceCreamParlor import main

class TestIceCreamParlor(TestCase):
    def test_initial_case(self):
        input_string = '''2
4
5
1 4 5 3 2
4
4
2 2 4 3
'''

        result = '''1 4
1 2
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())
