import io
import sys
from unittest import TestCase

from Solutions.BlackRock.PerfectSeparating import main


class TestSolution(TestCase):
    def test_initial_case(self):
        input_string = '''aaa
'''

        result = '''0
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())

    def test_case1(self):
        input_string = '''bbbb
'''

        result = '''6
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())

   # def test_case2(self):
   #     input_string = 'a'*24+'b'*24

    #    result = '''4
#'''
   #     sys.stdin = io.StringIO(input_string)
   #     sys.stdout = io.StringIO()
   #     main()
   #     self.assertEqual(result, sys.stdout.getvalue())

    def test_case3(self):
        input_string = '''abbaabbabbbbaa
'''

        result = '''48
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())

    def test_case4(self):
        input_string = '''abaaaaaaaaba
'''

        result = '''0
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())

    def test_case5(self):
        input_string = '''aaaabbbbaaaa
'''

        result = '''216
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())

    def test_case6(self):
        input_string = '''aabbaabbaabb
'''

        result = '''88
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())

    def test_case7(self):
        input_string = '''aabbaa
'''

        result = '''8
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())

    def test_case8(self):
        input_string = '''abaaba
'''

        result = '''4
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())

    def test_case9(self):
        input_string = '''ababaa
'''

        result = '''4
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())

    def test_case10(self):
        input_string = '''bbaabbaaaaaaaaaaaaaaaaaaaaabbbbaaaaaaaaaaaaaaaaaaaaabbbbaaaaaaaaaaaaaaaaaabbbbbbbbbbaaaaaaaaaabbaa
'''

        result = '''273485197059007610880
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())
 #   def test_case1(self):
 #       file_input = open('GridChallenge.in')
 #       expected_output = open('GridChallenge.out')
 #       sys.stdin = file_input
 #       sys.stdout = io.StringIO()
 #       main()
 #       self.assertEqual(expected_output.read().strip(), sys.stdout.getvalue().strip())


