import io
import sys
from unittest import TestCase

from Solutions.GreedyChallenges import main


class TestTheGridChallenge(TestCase):
    def test_initial_case(self):
        input_string = '''3
1 2 2
1 2 3
'''

        result = '''3
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())

    def test_case1(self):
        file_input = open('BeautifulPairs.in')
        sys.stdin = file_input
        sys.stdout = io.StringIO()
        main()
        self.assertEqual('999', sys.stdout.getvalue().strip())



