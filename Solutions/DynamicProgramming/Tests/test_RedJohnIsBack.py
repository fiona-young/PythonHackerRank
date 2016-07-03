import io
import sys
from unittest import TestCase

from Solutions.DynamicProgramming.RedJohnIsBack import main,Primes


class TestSolution(TestCase):
    def test_primes(self):
        test_subject = Primes()
        self.assertEqual(0,test_subject.count_primes_up_to(1))
        self.assertEqual(1,test_subject.count_primes_up_to(2))
        self.assertEqual(2,test_subject.count_primes_up_to(3))
        self.assertEqual(6,test_subject.count_primes_up_to(13))


    def test_initial_case(self):
        input_string = '''4
4
1
7
25
'''

        result = '''1
0
3
269
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())


    def test_case1(self):
        input_string = '''20
34
3
31
35
10
38
18
27
15
3
38
14
18
4
5
23
9
31
10
25
'''

        result = '''3385
0
1432
4522
6
10794
42
462
19
0
10794
15
42
1
2
155
4
1432
6
269
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())

    def test_case2(self):
        input_string = '''1
34
'''

        result = '''3385
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


