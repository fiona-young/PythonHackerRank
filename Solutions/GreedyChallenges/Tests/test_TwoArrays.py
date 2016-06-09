import io
import sys
from unittest import TestCase

from Solutions.GreedyChallenges import main


class TestTwoArrays(TestCase):
    def test_initial_case(self):
        input_string = '''2
3 10
2 1 3
7 8 9
4 5
1 2 2 1
3 3 3 4
'''

        result = '''YES
NO
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())




