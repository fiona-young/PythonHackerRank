from unittest import TestCase
import sys
import io
from GreedyChallenges.SherlockAndMiniMax import main

class TestSolution(TestCase):
    def test_initial_case(self):
        input_string = '''3
5 8 14
4 9
'''

        result = '''4
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())

    def test_case2(self):
        input_string = '''5
38 50 60 30 48
23 69
'''

        result = '''69
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())


    def test_case3(self):
        input_string = '''100
635179944 592614358 645156538 601132234 72927588 782907998 26680576 571904512 253411364 368495632 668408894 715988190 473032290 221000496 166917988 579752154 157507364 169860230 693307354 154889188 598650762 721921752 691564182 40331570 680814954 699857994 283203518 248907756 42917082 510182506 103334006 659157584 68613710 41025968 514681540 388857390 732578568 312342822 544403214 414550896 401504698 342138612 578598706 455969120 673917170 671475360 622813896 327454610 742037798 192108990 115056746 453856008 67302432 568454084 178080688 624229470 47759236 7828940 554075052 636698586 56519734 254355714 149844386 684772334 714305610 572611200 740611006 350803732 625347950 27623254 429722502 772950450 508854614 18633596 529333176 635794634 102605328 122897004 595455366 105384508 220658676 370461750 782829740 371224392 595323626 302478768 448101966 213876262 477578452 724776600 623913570 456079206 284937928 441662568 21517112 446207966 467159802 620366990 178426646 130044896
64214888 789945206
'''

        result = '''493216533
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())

    def test_case4(self):
        input_string = '''5
12 10 50 24 40
9 16
'''

        result = '''16
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(result, sys.stdout.getvalue())

    def test_case5(self):
        input_string = '''67
7518 4798 5528 3806 7798 3396 6294 790 6724 3582 2336 4372 4746 7328 6822 1996 2004 5098 7376 7118 3478 2416 5310 3082 3288 2582 824 2832 4818 3508 1134 6640 5834 4068 3622 192 940 2564 5026 4708 4504 4828 2332 3948 5948 5676 2196 4206 7766 3710 4938 5688 3650 5824 4360 3786 6712 2856 5768 1826 2452 5874 964 1988 10 3226 2956
6449 7347
'''

        result = '''6467
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


