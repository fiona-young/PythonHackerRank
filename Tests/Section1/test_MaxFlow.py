from unittest import TestCase
import sys
from Section1.MaxFlow import MaxFlow
from collections import namedtuple

Edge = namedtuple('Edge','n1 n2 cap')
class TestMaxFlow(TestCase):
    def test_initial_case(self):
        adj_dict = {(0, 1): 3, (0, 2): 3, (1, 3): 3, (1, 2): 2, (2, 4): 2, (3, 5): 2, (3, 4): 4, (4, 5): 3}
        node_count = 6
        source = 0
        sink = 5
        test_subject = MaxFlow(node_count, source, sink, adj_dict)
        self.assertEqual(5,test_subject.calculate())

