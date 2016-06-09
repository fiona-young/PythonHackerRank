import io
import sys
from unittest import TestCase

from Solutions.Section2 import main


class TestSimilarPair(TestCase):
    def test_initial_case(self):
        input_string = '''5 2
3 2
3 1
1 4
1 5
'''

        result = '''4
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())

    def test_case_file1(self):
        file_input = open('test_SimilarPair.in')
        sys.stdin = file_input
        sys.stdout = io.StringIO()
        main()
        self.assertEqual("4991754395", sys.stdout.getvalue().strip())

    def test_case_file2(self):
        file_input = open('test_SimilarPair2.in')
        sys.stdin = file_input
        sys.stdout = io.StringIO()
        main()
        self.assertEqual("642387", sys.stdout.getvalue().strip())

    def test_smallish_case(self):
        input_string = '''100 5
1 90
90 64
90 63
90 68
1 52
52 13
13 79
79 78
78 46
46 72
72 83
83 66
66 57
57 53
53 28
28 36
36 23
53 74
74 5
5 54
5 99
5 50
74 11
11 7
74 31
53 87
87 59
87 44
44 4
4 15
15 19
19 71
71 51
15 61
4 56
56 49
44 55
44 67
67 77
87 41
41 60
60 100
57 39
39 10
10 14
14 96
96 22
22 12
10 98
98 95
95 73
73 94
94 81
95 21
98 43
43 16
16 18
18 45
45 26
26 62
43 69
43 27
27 85
85 2
85 6
85 58
58 88
58 84
39 89
46 65
65 40
40 76
76 86
86 35
86 3
76 17
17 70
70 97
17 33
17 38
40 34
65 48
48 9
46 37
37 47
37 8
78 32
32 80
32 20
20 91
32 24
24 29
29 92
29 82
32 93
78 25
79 42
52 30
30 75
'''

        result = '''103
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())
