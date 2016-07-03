import math
import collections

Case = collections.namedtuple('Case', 'faces colours')

fact = {}


def get_choose_k_max_to_1(n, k_max):
    combos = 1
    k_max = min(n, k_max)
    for k in range(1, k_max + 1):
        combos *= choose(n, k)
    return combos


def get_choose_cat_from_slots(slots, categories):
    return choose(slots + categories - 1, slots)


def get_factorial(val):
    if val not in fact:
        fact[val] = math.factorial(val)
    return fact[val]


def choose(n, k):
    return get_factorial(n) // (get_factorial(k) * get_factorial(n - k))


class Node:
    colours = None
    faces = None

    def __init__(self, node_id):
        self.id = node_id
        self.parent = None
        self.children = []
        self.combos = 0
        self.processed = False
        self.combo_dict = {}

    def __str__(self):
        return str(self.id)

    @property
    def child_count(self):
        return len(self.children)

    def walk(self, print_str=''):
        for node in self.children:
            print_str += node.walk()
        print_str += '%s ' % self.id
        return print_str

    def count_beautiful(self):
        root = self
        while root.processed == False:
            my_node = root
            for child in self.children:
                if child.processed == False:
                    my_node = child
                    break
            my_node.process()
        print(self.walk(''))

    def get_compatible_cases(self, available_faces, available_colours):
        combos = 0
        for colours in range(1, available_colours + 1):
            for face in available_faces:
                combos += self.combo_dict[Case(face, colours)]
        return combos

    def process(self):
        for faces in Node.faces:
            for colours in range(1, Node.colours + 1):
                self.combo_dict[Case(faces, colours)] = get_choose_cat_from_slots(faces, colours)
        for child in self.children:
            for case in self.combo_dict.keys():
                available_faces = Node.faces.difference({case.faces})
                available_colours = Node.colours - case.colours
                self.combo_dict[case] *= child.get_compatible_cases(available_faces, available_colours)
        self.processed = True


class Solution:
    def __init__(self):
        self.nodes, self.colours, self.types = get_int_list(input())
        self.face_list = get_int_list(input())
        Node.colours = self.colours
        Node.faces = set(self.face_list)
        if self.nodes > 1:
            self.parent = get_int_list(input())
        self.leaves = None
        self.graph = {}
        self.root = None

    def build_graph(self):
        self.graph = {i: Node(i) for i in range(1, self.nodes + 1)}
        self.root = self.graph[1]
        self.leaves = set(self.graph.keys())
        for child_id, parent_id in enumerate(self.parent, 2):
            self.graph[parent_id].children.append(self.graph[child_id])
            self.graph[child_id].parent = self.graph[parent_id]
            if parent_id in self.leaves:
                self.leaves.remove(parent_id)

    def calculate(self):
        self.build_graph()
        return self.root.count_beautiful()


def main():
    my_object = Solution()
    print(my_object.calculate())


def get_int_list(in_str):
    return [int(i) for i in in_str.strip().split()]


if __name__ == "__main__":
    main()
