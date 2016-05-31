from unittest import TestCase
import sys
import io
from ImplementationChallenges.ChocolateFeast import main

class TestChocolateFeast(TestCase):
    def test_initial_case(self):
        input_string = '''3
10 2 5
12 4 4
6 2 2
'''

        result = '''6
3
5
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())
