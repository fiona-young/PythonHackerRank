import io
import sys
from unittest import TestCase

from Solutions.GreedyChallenges import main


class TestSolution(TestCase):
    def test_initial_case(self):
        input_string = '''5
1 2 3 17 10
'''

        result = '''3
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())




