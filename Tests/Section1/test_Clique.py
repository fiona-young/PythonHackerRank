from unittest import TestCase
import sys
import io
from Section1.Clique import main, get_result
from math import ceil


class TestEvenTree(TestCase):
    def test_initial_case(self):
        input_string = '''5
5 10
3 2
4 6
5 7
19 166
'''

        result = '''5
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
            self.assertEqual(expected_clique, max_clique,"%s %s %s"%(i,nodes,edges))

def get_int_list(in_str):
    return [int(i) for i in in_str.strip().split()]
