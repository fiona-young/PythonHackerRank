import io
import random
import sys
from unittest import TestCase

from Solutions.Zolando.GiveMeTheOther import main


class TestSolution(TestCase):
    def test_initial_case(self):
        input_string = '''6
1 2 3 4 5 6
3
4 5
3 4
2 3
'''

        result = '''2 4 1 5 3 6
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())

    def test_case1(self):
        input_string = '''6
1 2 3 4 5 6
4
4 5
3 4
2 3
1 3
'''

        result = '''2 4 1 5 3 6
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())

    def test_case2(self):
        f = open('test_GiveMeTheOther1.in','w')
        max_val = 200000
        f.write('%s\n'%max_val)
        f.write(" ".join([str(a) for a in range(1,max_val+1)])+"\n")
        query = 200000
        f.write('%s\n'%query)
        for i in range(query):
            f.write(" ".join([str(a) for a in sorted([random.randint(1,max_val),random.randint(1,max_val)])])+"\n")

        input_string = '''6
1 2 3 4 5 6
5
4 5
3 4
2 3
1 3
4 6
'''

        result = '''5 3 6 2 4 1
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()

        self.assertEqual(result, sys.stdout.getvalue())



    def test_file1(self):
        file_input = open('test_GiveMeTheOther1.in')
        sys.stdin = file_input
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(''.strip(), sys.stdout.getvalue().strip())


