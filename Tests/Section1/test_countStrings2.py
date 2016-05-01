from unittest import TestCase
import sys
import io
from Section1.CountStrings2 import main, CountStrings


class TestCountStrings(TestCase):
    def test_initial_case(self):
        input_string = '''4
        ((ab)|(ba)) 2
        ((a|b)*) 5
((ab)(ba)) 2
((a*)(b(a*))) 100
'''

        result = '''2
32
0
100
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()

        main()
        self.assertEqual(result, sys.stdout.getvalue())

    def test_case1(self):
        input_string = '''3
        ((a*)*) 100
       (((aa)b)|((a)b)) 3
       (((aa)b)|((ba)b)) 3
'''

        result = '''1
1
2
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()

        main()
        self.assertEqual(result, sys.stdout.getvalue())


    def test_case2(self):
        input_string = '''7
((a*)|a) 1
((((ab)|a)*)|(((aa)|(bb))*)) 1
((((ab)|a)*)|(((aa)|(bb))*)) 3
((((ab)|a)*)|(((aa)|(bb))*)) 4
((((ab)|a)*)|(((aa)|(bb))*)) 5
((((ab)|b)*)|(((aa)|(bb))*)) 6
((((ab)|b)*)|(((aa)|(bb))*)) 7
((((ab)|b)*)|(((aa)|(bb))*)) 8
((((ab)|b)*)|(((aa)|(bb))*)) 9
((((ab)|a)*)|(((aa)|(bb))*)) 10
(((ab)*)((ba)*)) 13
((((((((((((((((ba)b)b)a)b)b)a)a)a)a)b)b)a)a)b)a) 17
(((ab)*)((ba)*)) 12
(((((((((((ba)b)b)a)b)b)a)a)a)a)(((ab)*)((ba)*))) 14
((((ab)*)((ba)*))*) 15
(((((((((((ba)b)b)a)b)b)a)a)a)a)(((ab)*)((ba)*))) 15
((((((ab)*)((ba)*))*)*)*) 11
(((((((((((ba)b)b)a)b)b)a)a)a)a)(((ab)*)((ba)*))) 13
((((ab)*)|((ba)*))*) 14
(((((((((((ba)b)b)a)b)b)a)a)a)a)(((ab)*)((ba)*))) 14
((((ab)|(ba))*)|(((aa)|(bb))*)) 14
(((((ab)|(ba))*)|(((aa)|(bb))*))*) 10
(((((ab)|(ba))*)|(((aa)|(bb))*))*) 15
((a(b(bb)))*) 12
((b((a(aa))*))b) 14
((b((a(a(aa)))*))b) 13
(b(a(a(a(a(a(a(a(ab))))))))) 10
(b(a(a(a(a(a(a(a(ab))))))))) 9
(b(a(a(a(a(a(a(a(ab))))))))) 11
(a*) 10
(a(a*)) 4
(b(a(a(a(a(a(a(a(ab))))))))) 10
((ab)|((a*)(b*))) 2
(((a(ba))((ba)*))|((a|b)*)) 15
(((a(ba))((ba)*))|((a|b)*)) 16
(((a(ba))((ba)*))|(((ab)|(ba))*)) 16
(a(((b|(a(ba)))*)b)) 18
'''

        result = '''1
1
3
8
8
20
21
49
55
120
0
1
7
0
0
3
0
2
128
0
256
1024
0
1
1
0
1
0
0
1
1
1
3
32768
65536
256
277
'''
        sys.stdin = io.StringIO(input_string)
        #sys.stdout = io.StringIO()

        main()
        self.assertEqual(result, sys.stdout.getvalue())

    def test_case1_internal(self):
        input_str = "(a)"
        my_class = CountStrings(input_str)
        self.assertEqual(0,my_class.calculate(0))
        self.assertEqual(1,my_class.calculate(1))
        self.assertEqual(0,my_class.calculate(2))

    def test_case2_internal(self):
        input_str = "((a|b)*)"
        my_class = CountStrings(input_str)
        self.assertEqual(2,my_class.calculate(1))
        self.assertEqual(4,my_class.calculate(2))
        self.assertEqual(8,my_class.calculate(3))

    def test_case0_line1(self):
        input_str= "((ab)|(ba))"
        my_class = CountStrings(input_str)
        self.assertEqual(0,my_class.calculate(1))
        self.assertEqual(2,my_class.calculate(2))
        self.assertEqual(0,my_class.calculate(3))

    def test_case0_line2(self):
        input_str= "(a*)"
        my_class = CountStrings(input_str)
        self.assertEqual(1,my_class.calculate(1))
        self.assertEqual(1,my_class.calculate(2))
        self.assertEqual(1,my_class.calculate(3))






