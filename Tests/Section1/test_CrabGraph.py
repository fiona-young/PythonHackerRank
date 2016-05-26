from unittest import TestCase
import sys
import io
from Section1.CrabGraphBipartite import main


class TestCrabGraph(TestCase):
    def test_initial_case(self):
        input_string = '''4
8 2 7
1 4
2 4
3 4
5 4
5 8
5 7
5 6
6 3 8
1 2
2 3
3 4
4 5
5 6
6 1
1 4
2 5
8 2 11
1 4
1 2
3 4
3 2
2 5
4 5
2 6
5 6
6 7
6 8
7 8
50 3 24
32 46
18 23
3 38
27 32
23 36
6 17
26 28
49 45
7 22
7 10
47 11
37 22
12 50
38 47
7 15
38 9
32 42
25 29
1 23
49 19
10 28
2 36
33 41
19 45
'''

        output_string = '''6
6
8
32
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(output_string, sys.stdout.getvalue())

    def test_caseb(self):
        input_string = '''9
65 2 33
4 55
7 46
4 9
39 49
59 29
40 25
43 24
35 10
52 38
26 63
36 48
50 6
17 34
30 47
23 29
30 43
27 65
61 39
46 2
23 50
2 1
30 11
46 18
10 25
39 40
19 31
25 3
48 25
11 51
19 2
39 23
35 14
46 50
74 10 46
26 2
2 5
57 21
44 18
46 8
35 6
45 44
24 56
17 27
33 37
46 64
35 69
35 19
36 45
35 29
66 47
39 20
34 38
61 60
34 74
35 31
4 5
48 4
34 53
11 67
66 71
45 58
71 41
38 11
54 48
73 74
39 70
6 26
27 49
54 47
62 73
57 5
39 16
28 48
50 64
70 25
44 9
67 59
44 4
17 57
57 29
40 4 47
15 7
9 6
12 1
38 2
26 25
17 8
12 28
37 8
29 11
18 8
13 38
12 29
16 13
1 17
24 31
11 38
31 10
11 27
4 5
25 32
8 11
18 36
30 6
29 21
2 17
12 32
19 7
28 2
38 40
18 27
34 31
17 9
13 1
27 2
40 16
27 40
35 14
11 28
4 30
25 1
7 10
10 29
5 19
7 31
17 28
28 24
3 25
46 96 13
4 20
42 5
20 38
37 18
45 33
18 7
13 9
42 19
5 8
18 28
33 11
12 40
39 5
59 11 29
41 53
34 46
26 19
9 11
18 49
3 27
34 14
42 55
56 47
29 9
7 4
51 55
39 59
33 6
5 7
33 45
23 22
58 34
1 35
24 23
41 14
22 51
57 40
10 5
46 20
25 47
39 32
57 16
35 31
24 2 211
4 7
7 16
3 17
14 12
18 7
16 22
4 10
24 9
9 23
15 1
15 19
20 8
24 19
16 3
10 22
15 3
6 20
6 19
6 11
13 2
16 10
1 17
6 5
1 11
11 18
18 15
11 2
2 15
6 4
18 6
19 7
4 23
10 12
9 3
15 24
8 23
11 20
11 5
2 14
1 16
14 9
14 17
8 21
12 11
17 22
9 16
13 21
21 5
19 1
6 12
9 4
20 2
23 10
9 21
21 20
19 5
23 1
7 14
24 14
1 3
10 13
8 10
19 2
11 4
18 19
22 23
4 22
3 12
1 13
13 14
17 5
11 14
22 7
5 23
18 22
14 1
2 12
7 17
12 23
4 8
18 5
6 8
10 20
9 13
4 16
20 12
11 13
16 23
19 23
23 17
18 2
8 16
4 13
8 9
7 6
16 11
21 4
22 19
18 16
6 14
22 20
2 22
20 9
2 21
24 20
4 14
11 21
21 19
16 2
24 7
15 16
22 1
8 11
13 8
7 21
12 1
3 10
13 23
11 22
23 15
13 20
19 3
9 17
1 21
19 8
6 13
11 17
20 5
9 5
6 9
17 8
21 12
12 22
24 2
24 10
6 23
9 2
21 16
16 5
19 17
17 12
3 14
20 1
15 9
9 1
1 4
7 11
7 13
6 2
24 6
8 14
12 13
3 22
17 20
23 20
6 1
24 17
6 22
8 18
2 8
19 14
7 12
2 3
15 6
16 24
5 22
21 23
18 13
18 14
13 16
21 10
19 16
20 15
12 9
11 23
8 3
20 3
22 8
14 15
2 17
3 13
14 23
18 24
5 15
2 5
20 4
5 10
22 15
14 21
23 24
12 8
10 18
5 14
12 4
20 14
4 17
18 21
16 6
4 19
24 4
8 15
22 13
24 13
1 8
1 18
15 17
5 24
15 10
1 7
10 17
5 7
64 8 7
51 39
64 49
23 45
8 40
59 11
29 58
61 62
93 88 11
86 38
78 50
79 54
86 63
52 55
75 26
88 82
11 4
20 30
28 15
68 76
89 30 75
20 51
73 32
7 20
41 48
79 89
3 88
9 58
37 41
59 58
33 44
29 87
89 27
23 78
72 45
14 5
27 9
34 32
89 51
21 33
85 29
75 71
86 55
14 58
8 30
55 35
2 47
82 57
23 81
60 61
61 1
7 86
86 38
49 76
61 68
76 14
39 16
82 62
39 32
54 52
23 31
26 42
63 66
23 53
70 26
53 27
78 76
72 50
28 44
65 5
50 32
63 18
2 68
54 5
8 4
33 15
86 58
7 77
57 63
26 55
63 4
35 78
40 14
67 15
88 53
83 37
87 24
20 82
61 58
10 79
15 35
79 80
73 13
52 35
82 11
12 22
'''

        output_string = '''40
52
35
19
41
24
14
21
77
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(output_string, sys.stdout.getvalue())

    def test_case1(self):
        input_string = '''10
50 46 367
13 17
41 5
46 26
46 14
24 6
48 14
50 42
28 48
24 2
5 11
17 34
17 47
11 29
33 49
29 8
25 43
16 50
15 46
6 45
46 22
41 19
27 49
26 4
25 7
42 43
15 42
47 33
18 15
42 38
1 37
8 20
15 26
36 49
23 9
25 15
2 16
21 27
28 19
26 24
47 42
22 25
12 30
9 43
35 34
42 41
45 42
44 19
9 28
3 20
43 7
31 33
10 4
14 26
11 2
38 9
5 25
20 1
15 13
40 44
48 22
36 20
15 39
29 44
26 45
33 29
5 32
48 3
46 12
41 15
41 34
18 47
8 38
33 28
19 6
33 7
2 6
36 27
42 6
7 10
14 35
22 32
28 23
45 49
21 49
46 36
43 39
10 46
3 7
29 48
49 46
22 11
5 22
37 18
26 19
32 28
1 11
21 2
20 21
8 14
17 24
48 11
40 33
24 42
50 27
7 12
32 47
26 11
37 3
19 3
28 16
41 23
44 6
41 1
23 33
49 30
35 39
12 5
29 37
29 50
28 49
25 1
21 34
10 11
16 5
28 46
32 50
40 14
32 17
39 13
3 8
35 15
13 35
32 29
18 28
45 10
5 47
46 32
39 47
21 48
7 21
35 3
49 26
14 31
15 3
27 26
26 48
12 14
47 38
46 31
6 9
43 29
39 3
13 40
30 34
9 37
7 26
35 26
14 34
10 29
5 34
34 32
20 24
17 27
15 2
21 39
47 15
25 42
19 34
32 18
6 16
27 32
46 7
35 9
21 38
24 47
34 42
24 7
16 12
18 4
30 16
49 50
35 4
4 11
20 23
6 15
49 29
44 49
34 22
38 35
10 20
17 46
21 42
6 33
37 35
19 25
5 6
38 7
50 31
40 38
10 8
9 36
47 49
2 49
8 7
43 27
46 13
40 12
17 50
42 13
37 13
17 6
44 13
48 5
8 36
10 3
13 14
6 32
50 25
8 35
48 18
6 3
25 11
29 15
39 5
25 28
31 41
43 10
3 21
50 26
20 22
3 24
31 7
36 17
22 49
8 5
28 3
18 36
40 39
25 45
36 47
39 32
18 38
27 19
19 21
21 24
14 3
14 23
25 20
46 38
3 46
15 30
36 34
29 42
17 45
5 29
16 35
33 12
38 19
24 32
8 48
43 31
49 25
1 16
47 9
30 24
46 1
37 23
25 10
31 3
44 36
36 19
50 47
45 8
5 31
26 34
17 19
40 5
37 27
44 47
17 37
31 28
15 43
10 21
12 17
50 34
7 48
23 26
27 38
20 47
2 30
30 6
37 47
31 37
4 43
20 38
30 8
13 41
46 6
16 31
41 28
41 27
15 14
44 24
28 45
45 18
37 28
45 7
46 37
50 2
40 29
42 17
13 4
43 8
40 36
19 39
24 8
40 18
5 10
21 9
47 16
23 4
4 45
33 43
2 32
15 32
1 9
31 20
42 28
15 10
34 45
16 4
42 3
15 7
34 6
35 7
4 38
45 37
27 16
38 15
29 2
2 5
27 29
40 31
48 17
24 28
18 13
48 43
28 38
34 44
34 4
26 8
40 9
25 41
11 38
48 30
1 12
32 26
5 45
26 37
44 14
7 11
7 36
25 33
34 8
22 39
36 39
25 32
50 5 8
15 50
37 43
20 27
47 50
4 37
28 5
17 47
40 44
50 5 24
4 50
46 16
26 44
3 18
8 38
4 25
15 35
17 33
46 8
6 11
23 27
27 46
25 30
41 22
18 9
45 41
47 45
43 21
19 18
29 15
27 24
31 10
34 22
46 15
50 3 76
49 32
28 18
44 47
45 35
48 20
37 9
47 48
37 34
41 39
12 41
20 9
22 50
39 31
14 27
11 12
34 31
4 29
24 3
7 45
44 3
36 25
43 38
40 18
10 6
2 30
35 27
37 22
25 24
33 44
44 6
18 44
35 39
34 49
26 9
1 34
1 33
32 25
7 37
38 40
12 42
40 10
10 36
3 29
1 22
30 19
42 24
13 17
44 2
34 43
32 50
13 1
26 31
49 35
5 19
16 45
48 23
21 43
17 32
34 41
30 40
41 23
36 14
40 48
37 23
32 8
32 22
33 24
4 12
3 6
47 16
11 31
2 10
43 25
27 42
40 49
9 45
50 3 23
27 14
30 6
18 48
42 4
37 10
3 33
28 14
49 40
33 9
33 46
6 49
48 24
42 29
17 50
10 38
20 36
44 30
14 22
48 32
8 39
26 22
44 10
43 35
50 9 22
28 2
45 28
1 7
33 49
11 5
40 37
7 39
4 2
27 20
48 12
16 17
21 45
32 47
2 1
8 2
9 26
14 45
22 27
11 17
39 32
34 21
26 10
50 19 5
24 30
39 42
15 17
1 15
50 30
50 2 121
28 17
29 41
48 43
15 43
28 46
46 3
20 7
15 23
41 35
24 30
13 18
23 31
46 13
5 29
32 43
31 18
6 11
35 38
41 32
33 42
23 18
34 11
45 25
33 1
6 17
23 4
29 30
19 45
21 44
22 4
3 38
19 2
38 14
36 7
10 19
47 23
37 49
45 47
15 3
26 18
19 9
39 24
46 12
6 4
1 13
35 7
10 45
39 5
48 27
13 34
2 10
25 27
28 40
43 40
10 36
2 11
28 42
11 32
21 18
27 5
44 17
49 18
19 22
28 24
17 42
35 43
39 16
34 30
43 45
4 40
1 39
48 33
44 24
4 8
2 41
33 2
36 48
35 48
6 34
46 45
16 33
45 31
21 24
37 4
46 19
45 6
10 48
44 43
41 1
28 35
5 20
17 43
11 14
31 25
28 27
42 20
24 12
37 13
33 49
8 12
27 38
22 37
38 31
45 38
31 1
3 44
40 50
3 39
19 5
3 45
24 19
23 34
13 23
35 30
25 5
36 43
8 7
33 17
25 3
47 46
8 3
50 38 11
20 22
4 38
28 16
20 26
4 24
30 28
10 44
40 34
12 42
36 11
16 2
50 32 6
16 1
48 45
50 46
38 15
9 18
37 48
'''

        output_string = '''50
13
33
48
32
29
8
50
18
11
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(output_string, sys.stdout.getvalue())

    def test_case2(self):
        input_string = '''1
50 4 29
25 18
8 49
3 26
35 20
41 5
8 1
15 43
7 11
44 11
12 22
8 42
30 4
28 36
2 43
27 23
37 5
15 50
20 42
11 36
34 8
31 22
17 28
21 15
6 5
15 29
1 34
42 14
18 42
8 30
50 4 4
24 14
45 41
44 6
50 10
'''

        output_string = '''35
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(output_string, sys.stdout.getvalue())

    def test_case3(self):
        input_string = '''4
54 2 167
52 54
29 30
51 19
18 21
9 53
50 17
8 20
48 28
16 50
35 27
41 54
8 14
17 20
14 9
52 18
50 39
19 5
20 26
12 47
12 27
11 33
49 19
7 26
5 48
24 51
7 25
34 8
9 29
23 34
34 42
54 27
37 49
17 6
34 41
40 11
11 31
51 1
33 43
11 42
41 29
3 43
36 24
52 23
11 1
32 10
26 30
36 14
34 22
36 38
51 45
20 15
35 3
13 51
12 48
47 46
39 46
39 24
24 15
53 29
34 37
18 14
33 20
53 47
44 23
5 24
10 6
1 12
44 30
36 1
39 20
14 48
28 10
26 28
24 52
51 41
42 19
41 13
46 2
19 11
19 21
44 9
53 19
28 1
36 54
18 38
45 13
13 7
5 38
8 1
16 20
20 12
51 6
41 16
39 11
53 6
22 38
30 11
28 29
10 7
39 10
20 13
18 1
32 5
31 40
2 34
35 22
8 47
39 31
29 32
9 23
50 51
27 20
47 41
13 40
39 17
32 36
33 50
20 53
19 38
15 6
6 45
37 54
39 35
21 41
35 13
50 25
30 34
2 48
33 24
6 46
9 18
11 46
43 8
21 30
16 28
28 50
54 5
20 43
9 32
2 14
24 17
49 3
32 15
42 35
24 30
33 35
48 26
11 54
33 39
22 7
41 14
22 9
26 21
27 6
31 24
17 27
48 33
44 39
54 16
54 17
17 45
54 6
33 25
40 5
42 21
34 1
13 2
41 40 0
15 77 0
6 2 10
5 1
3 5
3 2
4 1
4 6
4 2
3 6
1 2
5 6
6 1
'''

        output_string = '''53
0
0
6
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(output_string, sys.stdout.getvalue())

    def test_case4(self):
        input_string = '''1
50 16 15
43 4
15 7
20 8
35 12
26 19
45 17
23 37
20 3
1 33
48 3
37 1
7 6
6 20
35 43
49 37
'''

        output_string = '''20
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(output_string, sys.stdout.getvalue())