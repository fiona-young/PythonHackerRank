import random
import collections

SplitSet = collections.namedtuple('SplitSet', 'smaller larger')
Query = collections.namedtuple('Query','l r')

class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.tree_size = 1
        self.parent = None
        self.left = None
        self.right = None

    def get_tree_walk_str(self):
        result = []
        self.get_tree_walk(result)
        return " ".join(str(a) for a in result)

    def __str__(self):
        return self.get_tree_walk_str()
        return '%s s:%s prio:%s' % (self.value, self.tree_size, self.priority)

    def split(self):
        my_node = self.parent
        root_smaller = self.left
        root_larger = self.right

        is_left_child = self.is_left_child
        while my_node is not None:
            my_node.update_single()
            if is_left_child:
                root_larger = my_node.join(root_larger, my_node.right)
            else:
                root_smaller = my_node.join(my_node.left, root_smaller)
            is_left_child = my_node.is_left_child
            my_node.update_single()
            my_node = my_node.parent
        self.set_parent(root_smaller, None)
        self.set_parent(root_larger, None)
        self.parent = None
        self.right = None
        self.left = None
        self.update_single()
        return SplitSet(root_smaller, root_larger)

    def join(self, smaller, larger):
        root = self
        root.left = smaller
        root.set_parent(smaller, root)
        root.right = larger
        root.set_parent(larger, root)
        root.update_single()
        if (root.size_right > 0 and root.priority > root.right.priority) or (
                root.size_left > 0 and root.priority > root.left.priority):
            root = root.rebalance()
        return root

    def is_root(self):
        return self.parent is None

    @property
    def is_left_child(self):
        if self.is_root():
            return None
        return self == self.parent.left

    def get_node_at_position(self, position):
        my_node = self
        current_size = 0
        while my_node is not None:
            if position <= my_node.size_left + current_size:
                my_node = my_node.left
            else:
                current_size += my_node.size_left + 1
                if current_size == position:
                    return my_node
                else:
                    my_node = my_node.right

    def get_tree_walk(self, result: list):
        assert(self.tree_size == 1+self.size_right+self.size_left)
        if self.left is not None:
            self.left.get_tree_walk(result)
        result.append(self.value)
        if self.right is not None:
            self.right.get_tree_walk(result)

    def add(self, add_node):
        tree_node = self
        while tree_node is not None:
            if add_node.value < tree_node.value:
                if tree_node.left is None:
                    tree_node.set_left(add_node)
                    break
                else:
                    tree_node = tree_node.left
            else:
                if tree_node.right is None:
                    tree_node.set_right(add_node)
                    break
                else:
                    tree_node = tree_node.right
        add_node.update()

    def set_left(self, add_node):
        if add_node is not None:
            add_node.parent = self
        self.left = add_node

    def set_right(self, add_node):
        if add_node is not None:
            add_node.parent = self
        self.right = add_node

    def update(self):
        my_node = self
        while my_node is not None:
            my_node = my_node.check_heap()
            my_node.tree_size = 1 + my_node.size_right + my_node.size_left
            my_node = my_node.parent

    def update_single(self):
        self.tree_size = 1 + self.size_right + self.size_left

    def check_heap(self):
        if self.parent is None or self.parent.priority < self.priority:
            return self
        else:
            bottom_node = self.parent
            if self is self.parent.right:
                self.parent.rotate_left(self)
            else:
                self.parent.rotate_right(self)
            return bottom_node

    def rebalance(self):
        my_node = self
        while (my_node.size_right > 0 and my_node.priority > my_node.right.priority) or (
          my_node.size_left > 0 and my_node.priority > my_node.left.priority):
                if my_node.size_left == 0 or (my_node.size_right != 0 and my_node.left.priority > my_node.right.priority):
                    my_node.rotate_left(my_node.right)
                else:
                    my_node.rotate_right(my_node.left)
        my_node.update()
        return my_node.get_root()


    def get_root(self):
        my_node = self
        while not my_node.is_root():
            my_node = my_node.parent
        return my_node

    def rotate_left(self, u):
        w = self
        parent = w.parent
        b = u.left
        self.set_parent(w, u)
        u.left = w

        self.set_parent(b, w)
        w.right = b

        u.parent = parent
        if parent is not None:
            if parent.right is w:
                parent.right = u
            else:
                parent.left = u
        w.update_single()
        u.update_single()

    def rotate_right(self, w):
        u = self
        parent = u.parent
        b = w.right

        self.set_parent(u, w)
        w.right = u

        self.set_parent(b, u)
        u.left = b

        w.parent = parent
        if parent is not None:
            if parent.right is u:
                parent.right = w
            else:
                parent.left = w
        u.update_single()
        w.update_single()

    @staticmethod
    def set_parent(child, parent):
        if child is not None:
            child.parent = parent

    @property
    def size_right(self):
        return 0 if self.right is None else self.right.tree_size

    @property
    def size_left(self):
        return 0 if self.left is None else self.left.tree_size


class Treap:
    def __init__(self):
        self.root = None

    def __str__(self):
        if self.root is None:
            return 'empty'
        else:
            return self.root.get_tree_walk_str()

    @staticmethod
    def build_from_range(min_val, max_val):
        my_treap = Treap()
        random_list = list(range(min_val, max_val + 1))
        random.shuffle(random_list)
        for priority, value in enumerate(random_list, 1):
            my_node = Node(value, priority)
            my_treap.add(my_node)
        return my_treap

    def get_node_at_position(self, position: int):
        if self.root is None:
            return None
        else:
            return self.root.get_node_at_position(position)

    def add(self, my_node):
        if self.root is None:
            self.root = my_node
        else:
            self.root.add(my_node)

    def move_to_front(self, val_low, val_high):
        if val_low == 1:
            return
        low_node = self.get_node_at_position(val_low - 1)
        high_node = self.get_node_at_position(val_high)
        low_split_set = low_node.split()
        high_split_set = high_node.split()
        new_front = high_node.join(high_split_set.smaller, low_split_set.smaller)
        self.root = low_node.join(new_front, high_split_set.larger)


def read_input():
    n_boxes = int(input())
    initial_position = get_int_list()
    n_queries = int(input())
    queries =[]
    for i in range(n_queries):
        queries.append(Query(*get_int_list()))
    return n_boxes, initial_position, n_queries, queries

class Shelf:
    def __init__(self,min_val,max_val):
        self.treap = Treap.build_from_range(min_val,max_val)


    def move_to_front(self, query: Query):
        self.treap.move_to_front(query.l,query.r)

    def __str__(self):
        return str(self.treap)

    def print_result(self):
        print(str(self))

class Solution:
    def __init__(self):
        self.n_boxes, self.initial_position, self.n_queries, self.queries = read_input()
        self.locations = dict(zip(range(1,self.n_boxes+1),self.initial_position))
        self.start = 1
        self.gaps = []
        self.shelf = Shelf(1,self.n_boxes)

    def calculate(self):
        for query in self.queries:
            self.shelf.move_to_front(query)
        self.shelf.print_result()



def main():
    my_object = Solution()
    my_object.calculate()


def get_int_list():
    return [int(i) for i in input().strip().split()]


if __name__ == "__main__":
    main()
