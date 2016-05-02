from unittest import TestCase
import sys
import io
from Section1.CountStrings import main, CountStrings

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
        input_string = '''37
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
        sys.stdout = io.StringIO()

        main()
        self.assertEqual(result, sys.stdout.getvalue())

    def test_case3(self):
        self.maxDiff = None
        input_string = '''50
((((b*)((b(a|a))a))(((a*)|a)a))((aa)((((((b*)*)(b|((b|(aa))|b)))(a|b))|(b*))*))) 937477085
((((b*)((a*)*))b)|(b|(((a*)*)|((((a(b|a))|a)*)|(((a|(b|(b*)))*)*))))) 927612903
(((a(ba))(((((b|((ab)*))((b*)*))*)*)|((a|b)(((a|((ab)a))*)|b))))*) 150122847
((((b(aa))|a)|(b|b))(((b((a|b)|(b|b)))*)|((((((a*)*)*)|((aa)(a(((b*)*)*))))(a|(a*)))*))) 359512184
((a|((((((b*)|a)|(a|a))*)|(((b(bb))a)|(aa)))|(a((a((a*)|a))|(a*)))))|(((b|((aa)*))(b*))|(a|b))) 472713774
((((a|((a*)|(a(b(a|b)))))|((((b|b)*)|((((((bb)|(b*))*)|a)((a((a|a)a))*))*))*))|a)*) 253207673
(((((a|a)|b)(((b(b|b))*)*))|(a*))(((((ba)(aa))b)((((a*)|a)(((a*)*)((b*)*)))((aa)|a)))*)) 150517568
(a|(((((((b(b|a))|b)((a(((b|(a|a))*)*))*))a)|(((((a*)*)|b)(b|b))*))*)*)) 144522536
((((((((((b(b|a))*)|a)|((((ab)*)*)|(((a|(b*))|((a*)|b))*)))*)|a)*)*)*)((a|a)*)) 16764525
((((((((ab)*)*)*)(a*))|b)*)|((((aa)|(b*))*)(((a*)*)|(a((b|a)|a))))) 873524567
(((((b|b)(((((b*)|b)a)|((ba)*))*))*)*)(((a*)((aa)|((ba)((aa)a))))((b|b)|(((b*)(a|a))a)))) 655035326
(a((((((((a*)*)*)*)|(((((((((b(a|(bb)))*)|((b|a)*))*)*)*)b)*)*))|((b|((a|a)a))*))*)*)) 765326718
(((((((((b|a)*)|a)|((b|b)*))|((ba)*))*)((a(bb))*))|(((((b*)|b)*)*)((((bb)((a|b)|a))*)*)))*) 460686764
(((((((((((a|b)((aa)*))|((a|b)a))*)*)*)*)|b)(((b|((ba)*))*)*))*)*) 64945487
((b|b)((((((((b*)|a)*)*)*)*)|(((((((a|a)*)*)|((((a*)b)*)*))((b|a)*))((b(a*))*))*))(bb))) 931489115
((((((a*)|b)|a)a)((((((ab)|a)*)*)*)*))|(((((ba)(b*))*)|(ba))|b)) 287860000
((((a*)|a)((((b*)(ba))*)*))((((((((((a|b)*)b)*)*)(ba))((((a|b)a)|b)(b*)))*)*)*)) 787689127
(((b|(((((b*)*)*)(bb))|(a|a)))*)((aa)((((a(a|b))|(ab))*)*))) 870305001
(((b*)(b|a))|(((((b|a)|((((a*)|b)(a*))*))*)|((((bb)|(b|(a|((a*)b))))*)*))*)) 143195512
(((a|a)|(((a*)*)*))((((((aa)|a)((a|a)|(b|b)))*)*)|(((b*)b)*))) 404259632
((b((((((b*)|(ab))(bb))|a)|(a(a|a)))|(((b|(a|b))*)|b)))|((((a*)((ba)|a))|(a(a|b)))*)) 489692378
(((((((b*)*)*)|(a|(b*)))*)|((((a|a)*)(ab))*))((a((ba)|((a*)a)))*)) 649785906
((((((b|b)*)*)(a(((((((ab)|b)|(a|a))|(((bb)a)(b*)))|(b|b))*)*)))*)|(((((b*)|(ab))*)(b|b))*)) 2992735
((((b|(b*))a)(a|b))|(((b*)((b|a)|(a|b)))((b*)|((a(a*))(b*))))) 338346093
((a|a)|((b|(((((((b|b)b)|b)|(((ba)|b)|b))*)|((a((bb)*))*))|((a*)*)))*)) 775056795
(((((((b*)|((((b|a)a)|a)a))|(a(((b*)*)*)))(b|b))|b)a)((a(b*))a)) 396342014
(a(((((((((a|a)*)*)b)*)b)(((b|((((b|b)|b)*)*))|b)*))|((aa)|(b|b)))*)) 266222408
((((((b|b)*)|((b*)|a))(a|(a|a)))*)(((((ab)a)|(ab))*)((a|(((b|b)*)*))((ba)|b)))) 599529155
((((b|((b(b*))b))*)*)((((a((b*)|a))|(a|a))(ab))|((((b((((b(b(a|a)))*)|(aa))*))*)*)b))) 456651795
((((a|((ab)*))((a|(b*))b))(((((a*)*)*)|(a|b))*))|(b((b*)*))) 390387709
(((((b|a)*)*)(((ba)*)|((a(b((((a|b)|b)*)*)))((a((((b*)*)a)*))b))))|((a((a*)|a))*)) 356228372
(((((a*)|(bb))|(((((((ba)|a)(((((aa)*)*)|((ba)|((bb)*)))|((a|b)*)))*)*)*)|((b|a)*)))*)*) 245277884
((b|(b*))((((((bb)*)(((b*)*)b))(a|a))|(b((((ba)|b)|(a*))|(ab))))|(a*))) 296528781
((a|a)|(((b|(((a(((b|a)b)|(a|a)))|((a(ab))*))*))|b)(((b((b*)|((a(a|a))b)))(((bb)a)a))*))) 961415140
((a|(b|b))|(((aa)(((a|(ba))|a)|a))|(((((aa)a)|(aa))(b(a(aa))))*))) 859310841
((((a|(b((((ab)|((a*)*))*)*)))*)((b((aa)|(a|(a|b))))|(b*)))*) 63762112
((((((((b|a)(((bb)a)*))*)*)*)*)*)(((b|((a(b|a))a))|(ba))|a)) 212220436
((((((((((((bb)|a)|a)*)*)*)*)b)|((b*)b))|(((a|b)*)*))(b(b*)))((a(((bb)*)a))*)) 107230152
((((((((((a|a)b)*)|(a|(((a(((ba)a)*))*)*)))|a)*)*)|a)*)(((((a*)*)*)|b)*)) 959112712
(((b(b|((b*)*)))|(((ba)((b|a)|((((b*)b)|b)*)))((b(bb))*)))((a|b)|a)) 346030097
(((((((((a|((((b*)((a*)a))*)*))|(a*))*)*)(b*))*)*)*)|(((aa)((b|a)|(((a|(b*))*)*)))*)) 71061649
(((((((b|(b*))*)*)(ba))*)|(((((ba)*)|a)|((a|(b|(ba)))*))*))|(((a|(b*))*)a)) 68728259
(((a(b((a|a)b)))((((a|a)*)*)a))((a(((a(((a|(ab))((b*)a))*))*)|(a|a)))(((ab)*)|((b*)*)))) 202029502
((((a((a|((bb)((a|b)|(b*))))(a(a|b))))((a|(a*))(b|b)))*)(((((ba)(a*))|b)|(a|a))*)) 52861121
(((((a|a)*)|((a|((a(b|a))*))*))|(((a((aa)a))*)*))(((bb)b)b)) 822514996
(((b(((((b*)*)*)*)|a))((b*)|((((aa)|b)|(bb))*)))|((b(a*))|(((b(b*))|a)|(((a*)|(b*))(a|a))))) 100598389
((((a|((a*)*))((b((a|(a*))*))|(((a*)(((b|a)b)(bb)))*)))|((((b|a)*)*)((a|((bb)*))|b)))*) 709163926
(((((a*)*)(((a|a)(a(a(a*))))|(b*)))((((a|a)|a)*)*))((a*)*)) 849876230
(a(((((((ba)|(b|a))a)|a)|((b*)(((((((((((a((a|a)|a))a)(b|a))|a)|a)*)*)(b|a))*)*)*)))*)*)) 257164627
((((a|a)*)(((((((b|(a|b))|b)|b)*)b)(a*))|(((a|(((b*)*)*))*)b)))*) 368046388
'''

        result = '''971722885
992234032
4718730
486357608
141092500
873705910
713870975
721850737
294222231
948473105
437600740
794356302
527158721
115404564
977150281
388567604
387595705
194824320
894280556
847776352
131339469
117159835
599878374
92682099
920903659
792684024
273141846
472919272
767600333
883824742
133595680
136080480
296528783
664488648
30864164
23904499
127608347
629123032
746788713
4
42478196
333029944
785494390
357144475
228359184
322942292
524149263
56430959
45523423
63137616
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()

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
        self.assertEqual(1024,my_class.calculate(10))
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
        self.assertEqual(1,my_class.calculate(0))
        self.assertEqual(1,my_class.calculate(1))
        self.assertEqual(1,my_class.calculate(2))
        self.assertEqual(1,my_class.calculate(3))

    def test_case1_line2(self):
        input_str= "((((((ab)b)*)*)*)|(((aa)|((a(a|(b*)))b))|(((b|a)(b|b))(((b|b)*)(a|(ba))))))"
        my_class = CountStrings(input_str)
        self.assertEqual(3,my_class.calculate(423422303))

    def test_case1_line5(self):
        input_str= "((((a|a)*)(((((((b|(a|b))|b)|b)*)b)(a*))|(((a|(((b*)*)*))*)b)))*)"
        my_class = CountStrings(input_str)
        self.assertEqual(63137616,my_class.calculate(368046388))







