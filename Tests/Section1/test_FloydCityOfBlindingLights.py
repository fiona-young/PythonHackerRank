from unittest import TestCase
import sys
import io
from Section1.FloydCityOfBlindingLights import main
import Section1.FloydCityOfBlindingLights2

class TestFloydCityOfBlindingLights(TestCase):
    def test_initial_case(self):
        input_string = '''4 5
1 2 5
1 4 24
2 4 6
3 4 4
3 2 7
3
1 2
3 1
1 4
'''

        output_string = '''5
-1
11
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(output_string, sys.stdout.getvalue())

    def test_initial_case2(self):
        input_string = '''4 5
1 2 5
1 4 24
2 4 6
3 4 4
3 2 7
3
1 2
3 1
1 4
'''

        output_string = '''5
-1
11
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        Section1.FloydCityOfBlindingLights2.main()
        self.assertEqual(output_string, sys.stdout.getvalue())

    def test_case4(self):
        file_input = open('test_Floyd4.in')
        expected_output = open('test_Floyd4.out')
        sys.stdin = file_input #io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(expected_output.read().strip(), sys.stdout.getvalue().strip())

    def test_case4b(self):
        file_input = open('test_Floyd4.in')
        expected_output = open('test_Floyd4.out')
        sys.stdin = file_input
        sys.stdout = io.StringIO()
        Section1.FloydCityOfBlindingLights2.main()
        self.assertEqual(expected_output.read().strip(), sys.stdout.getvalue().strip())


