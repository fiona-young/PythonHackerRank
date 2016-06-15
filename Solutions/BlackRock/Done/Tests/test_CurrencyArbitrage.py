import io
import sys
import random
from unittest import TestCase

from Solutions.BlackRock.Done.CurrencyArbitrage import main


class TestSolution(TestCase):
    def test_initial_case(self):
        input_string = '''2
1.1837 1.3829 0.6102
1.1234 1.2134 1.2311
'''

        result = '''114
0
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())

    def test_write_case(self):
        #f = open('test_Currency1.in','w')
        max_val = 200000
        #print('100000 5.5 20 15\n')
        #print(" ".join([str(random.randint(1,100)) for a in range(20)])+"\n")
        count =500
        num1 = 100
        num2 = 800
        print(count)
        print(" ".join([str(random.randint(1,num1)) for a in range(count)]))
        print(" ".join([str(random.randint(1,num2)) for a in range(count)]))
        #self.assertEqual(result, sys.stdout.getvalue())

 #   def test_case1(self):
 #       file_input = open('GridChallenge.in')
 #       expected_output = open('GridChallenge.out')
 #       sys.stdin = file_input
 #       sys.stdout = io.StringIO()
 #       main()
 #       self.assertEqual(expected_output.read().strip(), sys.stdout.getvalue().strip())


