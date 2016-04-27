from unittest import TestCase
import sys
import io
import Section1.SparseArrays


class TestSparseArrays(TestCase):
    def test_initial_case(self):
        input_string = '''4
aba
baba
aba
xzxb
3
aba
xzxb
ab
'''

        result = '''2
1
0
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        Section1.SparseArrays.main()
        self.assertEqual(result, sys.stdout.getvalue())
