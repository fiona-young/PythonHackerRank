from unittest import TestCase
import sys
import io
import Section1.CountStrings


class TestCountStrings(TestCase):
    def test_initial_case(self):
        input_string = '''4
        ((a*)(b(a*))) 100
        ((ab)|(ba)) 2
        ((a|b)*) 5
((ab)(ba)) 2
'''

        result = '''2
32
100
'''
        sys.stdin = io.StringIO(input_string)
        #sys.stdout = io.StringIO()

        Section1.CountStrings.main()
        #self.assertEqual(result, sys.stdout.getvalue())

