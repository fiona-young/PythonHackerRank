import io
import sys
from unittest import TestCase

from Solutions.Section1.MinSpanTree_Prim import main


class TestMinSpanTreePrism(TestCase):
    def test_initial_case(self):
        input_string = '''5 6
1 2 3
1 3 4
4 2 6
5 2 2
2 3 5
3 5 7
1
'''

        result = '''15
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())
