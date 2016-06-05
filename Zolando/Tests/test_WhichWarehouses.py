import io
import sys
from unittest import TestCase

from Zolando.WhichWarehouses import main
import random

class TestSolution(TestCase):
    def test_initial_case(self):
        input_string = '''2 3 2
1 0
0 1
1 1
2 0
0 1
'''

        result = '''2
-1
1
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())

    def test_case1(self):
        input_string = '''0 3 2
1 1
2 0
0 1
'''

        result = '''-1
-1
-1
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())

    def test_case2(self):
        input_string = '''2 3 0
'''

        result = '''0
0
0
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())

    def test_case3(self):
        input_string = '''2 0 2
1 0
0 1
'''

        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual("", sys.stdout.getvalue())

    def test_case4(self):
        W = 16
        B = 10
        P = 10

        f = open('test_WhichWarehouses1.in','w')
        f.write('%s %s %s\n'%(W,B,P))
        item_max = 1000000000
        for i in range(W):
            f.write(" ".join([str(10) for a in range(P)])+"\n")
        for i in range(P):
            f.write(" ".join([str(15*(i+1)) for a in range(P)])+"\n")
        input_string = '''2 0 2
1 0
0 1
'''

        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual("", sys.stdout.getvalue())

    def test_case5(self):
        input_string = '''16 10 10
10 10 10 10 10 10 10 10 10 10
10 10 10 10 10 10 10 10 10 10
10 10 10 10 10 10 10 10 10 10
10 10 10 10 10 10 10 10 10 10
10 10 10 10 10 10 10 10 10 10
10 10 10 10 10 10 10 10 10 10
10 10 10 10 10 10 10 10 10 10
10 10 10 10 10 10 10 10 10 10
10 10 10 10 10 10 10 10 10 10
10 10 10 10 10 10 10 10 10 10
10 10 10 10 10 10 10 10 10 10
10 10 10 10 10 10 10 10 10 10
10 10 10 10 10 10 10 10 10 10
10 10 10 10 10 10 10 10 10 10
10 10 10 10 10 10 10 10 10 10
10 10 10 10 10 10 10 10 10 10
15 15 15 15 15 15 15 15 15 15
30 30 30 30 30 30 30 30 30 30
45 45 45 45 45 45 45 45 45 45
60 60 60 60 60 60 60 60 60 60
75 75 75 75 75 75 75 75 75 75
90 90 90 90 90 90 90 90 90 90
105 105 105 105 105 105 105 105 105 105
120 120 120 120 120 120 120 120 120 120
135 135 135 135 135 135 135 135 135 135
250 150 150 150 150 150 150 150 150 150

'''

        result = '''2
-1
1
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())

    def test_case6(self):
        input_string = '''5 3 1
1
2
2
2
2
8
5
8
'''

        result = '''4
3
4
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


