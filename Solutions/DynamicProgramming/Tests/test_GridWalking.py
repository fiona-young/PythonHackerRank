import io
import sys
from unittest import TestCase

from Solutions.DynamicProgramming.GridWalking import main


class TestSolution(TestCase):
    def test_case6(self):
        input_string = '''1
3 60
19 68 47
38 76 75
'''

        result = '''437196977
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())


    def test_initial_case(self):
        input_string = '''1
2 3
1 1
2 3
'''

        result = '''12
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())

    def test_case1(self):
        input_string = '''10
1 287
44
78
1 236
25
87
1 122
41
63
1 260
7
64
1 127
3
73
1 69
6
68
1 231
14
63
1 236
13
30
1 259
38
70
1 257
11
12
'''

        result = '''38753340
587915072
644474045
423479916
320130104
792930663
846814121
385120933
60306396
306773532
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())

    def test_case2(self):
        input_string = '''10
5 200
31 64 13 10 65
33 77 40 27 95
6 71
29 58 77 1 7 1
35 68 98 18 53 2
7 242
66 15 41 22 40 12 8
66 45 41 32 98 82 10
8 257
34 3 2 5 27 21 4 32
98 87 7 20 29 33 4 71
9 216
25 39 9 24 16 49 4 39 89
41 97 19 47 22 80 65 42 94
5 65
15 1 16 2 17
25 88 44 28 60
3 252
19 68 47
38 76 75
9 296
8 26 8 8 4 63 36 3 3
30 36 19 44 29 77 44 14 7
5 119
23 48 1 19 66
29 70 18 25 71
1 300
24
73
'''

        result = '''517479036
434664558
947516242
135816704
364285283
842822704
985312230
351950416
363111721
196793198
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())



    def test_case3(self):
        input_string = '''10
2 14
2 58
22 85
1 5
3
16
2 7
53 16
92 57
1 11
19
97
2 6
38 15
85 37
1 10
8
14
1 16
11
83
1 8
15
35
2 11
57 43
88 77
1 5
4
4
'''
        result = '''145422675
25
16384
2048
4096
990
65262
256
4194304
8
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())


    def test_case4(self):
        input_string = '''1
3 3
2 2 2
3 3 3
'''
        result = '''132
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


