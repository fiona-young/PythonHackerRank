import io
import sys
from unittest import TestCase

from Solutions.BlackRock.TradeAnalysis import main


class TestSolution(TestCase):
    def test_initial_case(self):
        input_string = '''3
1 2 3
'''

        result = '''46
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())

    def test_case1(self):
        input_string = '''20
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
'''

        result = '''318540960
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())

    def test_case2(self):
        input_string = '''40
40279 78016 5855 69571 50542 22094 4829 80277 93584 8018 30713 37498 4595 34854 983 85458 33623 32555 29705 87228 18216 56205 95266 26181 65518 89705 75146 6256 27667 5336 81129 8797 77163 91986 80356 25267 70170 79425 96519 21198 96716 46352 94036 1867 8382 96264 85435 19398 76560 10949 71813 20735 44500 67318 39237 36631 67125 85220 56964 95571 18669 6021 73508 64207 61589 94422 14848 25336 10237 28968 65245 84047 6012 14475 76592 77398 57202 54716 6172 84509 93886 22998 81617 98967 21033 96164 85758 79711 68240 26651 2594 82966 14002 93478
'''

        result = '''143191814
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())

 #   def test_case1(self):
 #       file_input = open('GridChallenge.in')
 #       expected_output = open('GridChallenge.out')
 #       sys.stdin = file_input
 #       sys.stdout = io.StringIO()
 #       main()
 #       self.assertEqual(expected_output.read().strip(), sys.stdout.getvalue().strip())


