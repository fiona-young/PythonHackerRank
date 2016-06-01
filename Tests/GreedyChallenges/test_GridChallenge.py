from unittest import TestCase
import sys
import io
from GreedyChallenges.GridChallenge import main

class TestTheGridChallenge(TestCase):
    def test_initial_case(self):
        input_string = '''1
5
ebacd
fghij
olmkn
trpqs
xywuv
'''

        result = '''YES
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())

    def test_case1(self):
        file_input = open('GridChallenge.in')
        expected_output = open('GridChallenge.out')
        sys.stdin = file_input
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(expected_output.read().strip(), sys.stdout.getvalue().strip())

