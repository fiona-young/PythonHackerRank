import io
import sys
from unittest import TestCase

from Solutions.ImplementationChallenges.LisaWorkBook import main


class TestChocolateFeast(TestCase):
    def test_initial_case(self):
        input_string = '''5 3
4 2 6 1 10
'''

        result = '''4
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())
