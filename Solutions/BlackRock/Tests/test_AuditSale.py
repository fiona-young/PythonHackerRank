import io
import random
import sys
from unittest import TestCase

from Solutions.BlackRock.AuditSale import main


class TestSolution(TestCase):
    def test_initial_case(self):
        input_string = '''3 2 1
5 10
6 60
8 40
'''

        result = '''1160
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())

    def test_second_case(self):
        input_string = '''15 10 5
56 23
20 67
64 80
82 55
40 50
153 99
18 26
14 63
64 32
76 34
46 43
188 25
151 75
129 30
141 37
'''

        result = '''1160
'''
        #for i in range(15):
         #   print("%s %s"%(random.randint(1,200),random.randint(20,100)))
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


