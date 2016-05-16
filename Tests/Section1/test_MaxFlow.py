from unittest import TestCase
import sys
from Section1.MaxFlow import MaxFlow, get_adj_matrix
from collections import namedtuple

Edge = namedtuple('Edge','n1 n2 cap')
class TestMaxFlow(TestCase):
    def test_initial_case(self):
        adj_list = [Edge(0,1,3),Edge(0,2,3),Edge(1,3,3),Edge(1,2,2),Edge(2,4,2),Edge(3,5,2),Edge(3,4,4),Edge(4,5,3)]
        node_count = 6
        adj_matrix = get_adj_matrix(node_count, adj_list)
        source = 0
        sink = 5
        #test_subject =

        output_string = '''6
6
8
32
'''
        self.assertEqual(output_string, sys.stdout.getvalue())

