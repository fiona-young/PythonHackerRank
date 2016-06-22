from unittest import TestCase
import random

from ExampleDataStructures.Treap import Treap, Node


class TestSolution(TestCase):
    def testBuildTreap(self):
        min_val = 1
        max_val = 10
        test_subject = Treap.build_from_range(min_val,max_val)
        for i in range(min_val,max_val+1):
            self.assertEqual(i,test_subject.get_node_at_position(i).value)
        test_subject.move_to_front(5,8)
        self.assertEqual('5 6 7 8 1 2 3 4 9 10',str(test_subject))
        test_subject.move_to_front(10, 10)
        self.assertEqual('10 5 6 7 8 1 2 3 4 9',str(test_subject))
        test_subject.move_to_front(1, 5)
        self.assertEqual('10 5 6 7 8 1 2 3 4 9',str(test_subject))
        test_subject.move_to_front(2, 9)
        self.assertEqual('5 6 7 8 1 2 3 4 10 9',str(test_subject))

    def testExtractNode(self):
        min_val = 1
        max_val = 10
        test_subject = Treap()
        random_list = list(range(min_val, max_val + 1))
        random.shuffle(random_list)
        node_list=[]
        for value, priority in enumerate(random_list, 1):
            my_node = Node(value, priority)
            node_list.append(my_node)
            test_subject.add(my_node)
        test_subject.extract_node(node_list[3])
        self.assertEqual('1 2 3 5 6 7 8 9 10',str(test_subject))
        self.assertEqual(1,node_list[3].tree_size)
        node_list[3].value = 25
        test_subject.add(node_list[3])
        self.assertEqual('1 2 3 5 6 7 8 9 10 25',str(test_subject))
        a = 1


   # def testJoinTreap(self):
       # test_subject1 = Treap.build_from_range(1,5)
        #test_subject2 = Treap.build_from_range(6,10)
        #test_subject1.join(test_subject2)


 #   def test_case1(self):
 #       file_input = open('GridChallenge.in')
 #       expected_output = open('GridChallenge.out')
 #       sys.stdin = file_input
 #       sys.stdout = io.StringIO()
 #       main()
 #       self.assertEqual(expected_output.read().strip(), sys.stdout.getvalue().strip())


