from unittest import TestCase
import sys
import io
from Section1.Clique import main, get_result
from math import ceil
'''14 13 117 49 1108
19 18 196 46 998
23 22 237 51 1240
16 15 290 41 784
16 15 392 34 539
21 20 541 45 961
19 18 637 39 718
18 17 638 41 791
13 12 784 28 359
17 16 1135 42 826
19 18 1261 43 872
12 11 1269 26 307
5 6 1284 20 160
18 17 1285 44 911
5 6 1420 30 360
10 9 1516 48 1024
6 7 1537 42 735
22 21 1559 47 1051
13 12 1599 30 412
6 7 1791 18 135
10 9 1917 39 676
12 11 1937 51 1182
12 11 1956 36 589
10 9 2087 21 196
21 20 2109 43 878
12 11 2578 39 691
5 6 2732 10 40
5 6 2759 20 160
15 14 2978 36 601
5 6 3062 10 40
14 13 3076 33 502
5 6 3108 10 40
20 19 3225 46 1001
17 16 3360 40 749
21 20 3377 49 1140
11 10 3679 37 616
18 17 3714 45 952
12 11 3773 37 622
5 6 3808 10 40
10 11 3983 20 180
17 16 4141 36 607
15 14 4701 37 635
14 13 4709 48 1063
22 21 4916 48 1097
10 9 4986 32 455'''

class TestClique(TestCase):
    def test_initial_case(self):
        input_string = '''7
20 160
49 1108
5 10
3 2
4 6
5 7
19 166
'''

        result = '''5
14
5
2
4
3
14
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())

    def test_case4(self):
        file_input = open('test_Clique1.in')
        expected_output = open('test_Clique1.out')
        sys.stdin = file_input #io.StringIO(input_string)
        sys.stdout = io.StringIO()
        cases = int(input())
        for i in range(cases):
            expected_clique = int(expected_output.readline().strip())
            in_str = input()
            nodes, edges = get_int_list(in_str)
            max_clique = get_result(nodes, edges)
            #if expected_clique != max_clique:
             #   print("%s %s %s %s %s"%(expected_clique, max_clique,i,nodes,edges))
            self.assertEqual(expected_clique, max_clique,"%s %s %s"%(i,nodes,edges))

def get_int_list(in_str):
    return [int(i) for i in in_str.strip().split()]
