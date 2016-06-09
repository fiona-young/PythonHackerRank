import collections
Query = collections.namedtuple('Query','l r')

def read_input():
    n_boxes = int(input())
    initial_position = get_int_list()
    n_queries = int(input())
    queries =[]
    for i in range(n_queries):
        queries.append(Query(*get_int_list()))
    return n_boxes, initial_position, n_queries, queries

class Box:
    def __init__(self, value, previous):
        self.previous = previous
        self.next = None
        self.value = value

    def __str__(self):
        return str(self.value)
class Shelf:
    def __init__(self, initial_position: list):
        self.length = len(initial_position)
        self.head = None
        self.tail = None
        self.lookup = {}
        for position, box_id in enumerate(initial_position,1):
            my_box = Box(box_id, self.tail)
            if self.head is None:
                self.head = my_box
                self.tail = my_box
            else:
                self.tail.next = my_box
                self.tail = my_box

    def move_to_front(self, query: Query):
        if query.l == 1:
            return
        if query.l < (self.length - query.r):
            node_left =self.walk_right(self.head,query.l-1)
            node_right = self.walk_right(node_left, query.r-query.l)
        else:
            node_right = self.walk_left(self.tail, self.length - query.r)
            node_left = self.walk_left(node_right,query.r-query.l)
        if node_right.next is None:
            self.tail = node_left.previous
        else:
            node_right.next.previous = node_left.previous
        node_left.previous.next = node_right.next
        self.head.previous = node_right
        node_right.next = self.head
        node_left.previous = None
        self.head = node_left

    def walk_right(self, my_node, step):
        i = 0
        while i < step:
            my_node=my_node.next
            i+=1
        return my_node

    def walk_left(self, my_node, step):
        i = 0
        while i < step:
            my_node=my_node.previous
            i+=1
        return my_node

    def print_result(self):
        result =[]
        my_node=self.head
        while my_node is not None:
            result.append(str(my_node))
            my_node = my_node.next
        print(" ".join(result))

class Solution:
    def __init__(self):
        self.n_boxes, self.initial_position, self.n_queries, self.queries = read_input()
        self.locations = dict(zip(range(1,self.n_boxes+1),self.initial_position))
        self.start = 1
        self.gaps = []
        self.shelf = Shelf(self.initial_position)

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
