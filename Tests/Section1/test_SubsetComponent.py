from unittest import TestCase
import sys
import io
import random
from Section1.SubsetComponentOptimal import main, GraphList


class TestSubsetComponent(TestCase):
    def test_initial_case(self):
        input_string = '''3
2 5 9
'''

        output_string = '''504
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(output_string, sys.stdout.getvalue())

    def test_worst_case(self):
        input_string = "20\n"
        input_string += "6612356234408173895 11075084782551501238 10839803116412655060 8540753727330998555 " \
                        "8634091438471196446 9592623732176006849 15365594866269118968 17219609215056047183 " \
                        "8363082181738449528 7767531377331086564 3377648750862034419 17501226938370097042 " \
                        "14954784957969854559 10476395877747407629 14798296609853256460 2181497071944590932 " \
                        "14540235675123941203 5153965387048937874 9436794614954476193 17046257361822060628"

        output_string = '''1190015
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(output_string, sys.stdout.getvalue())

    def test_worst_case1(self):
        input_string = "20\n"
        input_string += "13064769702345019347 17645604135140084697 14573023922744149389 9725327617823295938 " \
                        "13706030454256814013 1061768711999361577 13628786686351584901 15849292096118399700 " \
                        "16874439716125349329 2526794377617770837 10579495580343725574 12284449878999589071 " \
                        "14544871209768210805 11034875607935546714 14772754046804214000 12899444798559069517 " \
                        "15466126417063826708 1385341090865279291 17661415554894177718 4377492544227287154"

        output_string = '''1243695
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(output_string, sys.stdout.getvalue())

    def test_clash_case(self):
        input_string = "10\n"
        input_string += "3 24 288 384 3072 12288 49152 196608 5153965387048937874 1721960921505604718"

        output_string = '''34180
'''
        sys.stdin = io.StringIO(input_string)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(output_string, sys.stdout.getvalue())

    def test_second_case(self):
        input_list = [6612356234408173895, 11075084782551501238, 10839803116412655060, 8540753727330998555,
                      8634091438471196446, 9592623732176006849, 15365594866269118968, 17219609215056047183,
                      8363082181738449528, 7767531377331086564, 3377648750862034419, 17501226938370097042,
                      14954784957969854559, 10476395877747407629, 14798296609853256460, 2181497071944590932,
                      14540235675123941203, 5153965387048937874, 9436794614954476193, 17046257361822060628]
        input_list = [random.randrange(0, 2 ** 64) for i in range(20)]
        print(" ".join([str(i) for i in [random.randrange(0, 2 ** 64) for i in range(20)]]))
        my_graph = GraphList(input_list)
        my_graph.calculate()

    def test_third_case(self):
        input_list = [2 ** 1 + 2 ** 0, 2 ** 3 + 2 ** 4, 2 ** 5 + 2 ** 8, 2 ** 8 + 2 ** 7,
                      2 ** 10 + 2 ** 11, 2 ** 12 + 2 ** 13, 2 ** 14 + 2 ** 15, 2 ** 16 + 2 ** 17]
        # input_list = '3 24 288 384 3072 12288 49152 196608'
        my_graph = GraphList(input_list)
        my_graph.calculate()
