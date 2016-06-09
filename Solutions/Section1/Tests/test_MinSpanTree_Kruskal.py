import io
import sys
from unittest import TestCase

from Solutions.Section1.MinSpanTree_Kruskal import main


class TestMinSpanTreePrism(TestCase):
    def test_initial_case(self):
        input_string = '''4 6
1 2 5
1 3 3
4 1 6
2 4 7
3 2 4
3 4 5
1
'''

        result = '''12
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())
