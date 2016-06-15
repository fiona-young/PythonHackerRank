import io
import sys
from unittest import TestCase

from Solutions.DynamicProgramming.GridWalking import main


class TestSolution(TestCase):
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
        input_string = '''1
10 137
5 95 50 53 29 27 45 28 4 4
33 95 80 74 51 61 80 94 22 5
2 255
16 8
27 45
3 207
7 10 12
85 43 29
3 109
18 16 3
59 37 54
4 134
3 81 15 13
34 91 68 69
1 247
41
89
10 191
2 18 23 76 4 5 30 3 7 46
4 64 54 87 53 76 58 37 15 61
9 128
15 57 13 44 3 16 1 43 12
51 57 95 100 40 29 1 48 60
6 135
13 16 5 15 72 44
40 16 5 50 86 44
8 101
3 40 45 75 33 11 18 4
39 50 68 93 44 30 83 42
'''

        result = '''407114837
500098891
139698901
806371494
949533515
230125296
417754335
581357927
503661751
644851148
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())


    def test_case3(self):
        input_string = '''10
10 35
20 58 12 14 5 5 48 18 39 11
22 86 55 63 42 53 63 100 55 16
2 265
62 77
91 92
8 138
29 9 25 31 51 8 58 4
60 72 88 91 71 66 70 62
2 213
1 34
1 39
5 190
24 1 62 13 67
33 5 80 13 70
1 57
1
45
10 215
43 12 76 56 52 65 90 18 6 21
66 27 84 70 53 94 90 32 65 49
8 114
7 6 10 9 61 23 23 11
34 50 56 69 61 24 72 78
6 82
51 11 1 65 42 40
62 24 1 76 43 60
10 245
69 17 60 26 2 36 32 21 21 3
70 52 84 34 5 82 67 68 93 3
'''
        input_string = '''1
10 8
20 58 12 14 5 5 48 18 39 11
22 86 55 63 42 53 63 100 55 16
2 265
62 77
91 92
8 138
29 9 25 31 51 8 58 4
60 72 88 91 71 66 70 62
2 213
1 34
1 39
5 190
24 1 62 13 67
33 5 80 13 70
1 57
1
45
10 215
43 12 76 56 52 65 90 18 6 21
66 27 84 70 53 94 90 32 65 49
8 114
7 6 10 9 61 23 23 11
34 50 56 69 61 24 72 78
6 82
51 11 1 65 42 40
62 24 1 76 43 60
10 245
69 17 60 26 2 36 32 21 21 3
70 52 84 34 5 82 67 68 93 3
'''
        result = '''131423402
349816159
570595546
367855350
534020185
104059731
989250436
483098783
101475790
726431319
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


