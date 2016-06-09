from unittest import TestCase

from Solutions.Section2 import FenwickRangeFinder, Fenwick, CountPairs


class TestScratchPad(TestCase):
    def test_fenwick_range(self):
        test_subject = FenwickRangeFinder(20)
        for i in [13, 3, 14, 18, 1, 9, 7, 10, 4, 2, 11, 15, 12, 8]:
            test_subject.add(i)
        self.assertEquals(3, test_subject.range_count(2, 5))
        self.assertEquals(4, test_subject.range_count(2, 7))
        self.assertEquals(5, test_subject.range_count(0, 7))
        self.assertEquals(14, test_subject.range_count(0, 20))

    def test_fenwick_tree2(self):
        test_subject = Fenwick(11)
        for key, value in enumerate([3, 2, -1, 6, 5, 4, -3, 3, 7, 2, 3]):
            test_subject.update(key, value)
        for key, expected_value in enumerate([3, 5, 4, 10, 15, 19, 16, 19, 26, 28, 31]):
            self.assertEquals(expected_value, test_subject.query(key))
        test_subject.update(3, 10)
        for key, expected_value in enumerate([3, 5, 4, 14, 19, 23, 20, 23, 30, 32, 35]):
            self.assertEquals(expected_value, test_subject.query(key))

    def test_get_pairs(self):
        graph_in = {128: {78}, 129: {2}, 130: {68}, 131: {88, 1, 17}, 132: {50, 76}, 133: {99}, 134: {59}, 135: {11},
                    136: {30}, 137: {30}, 142: {5}, 143: {11}, 145: {45}, 146: {24, 73, 99}, 147: {90, 38},
                    148: {92, 37}, 150: {26}, 152: {81}, 153: {80, 32}, 154: {41, 95}, 155: {81}, 156: {22},
                    158: {8, 69}, 160: {95}, 162: {80}, 164: {90}, 165: {62}, 167: {46}, 168: {19}, 170: {8, 22},
                    171: {82}, 172: {9}, 174: {67, 37, 92, 85}, 176: {0, 75}, 177: {99}, 180: {95}, 181: {26, 3},
                    182: {20}, 183: {82, 61}, 185: {80}, 186: {48}, 187: {24, 73, 99}, 188: {0, 88}, 189: {26},
                    190: {9}, 193: {93}, 195: {42}, 196: {62}, 197: {83}, 198: {88, 17, 75}, 199: {62}, 101: {11},
                    103: {31}, 104: {96, 92, 85}, 105: {5}, 106: {98, 2, 29}, 108: {86, 94}, 109: {9}, 111: {47},
                    112: {0}, 113: {60}, 114: {88, 1}, 116: {81}, 117: {18, 34}, 119: {11}, 122: {18, 28}, 123: {47},
                    124: {71}, 125: {53}, 126: {56, 43}, 127: {56, 43}}

        a = range(250)
        b = range(250)
        c = [(i, j) for i in a for j in b]
        d = [(e, f) for e in c for f in c]
        g = 1

    def test_count_pairs(self):
        test_subject = CountPairs(list(range(1,7)),list(range(7,13)))
        for from_node, to_node in [(1,7),(1,8),(2,7),(3,9),(3,10),(3,11),(4,12),(5,12),(6,12)]:
            test_subject.add_edge(from_node, to_node)
        self.assertEquals(4,test_subject.calculate_pairs())
        self.assertEquals(4,test_subject.calculate_pairs())
        test_subject.add_edge(5, 9)
        self.assertEquals(5,test_subject.calculate_pairs())