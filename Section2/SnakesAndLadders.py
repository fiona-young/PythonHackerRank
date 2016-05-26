import collections
Edge = collections.namedtuple("Edge", "node weight")


class Node:
    def __init__(self, node_id):
        self.id = node_id
        self.weight = None
        self.visited = False
        self.adj_list = []
        self.heap_location = None

    def update_heap(self, location):
        self.heap_location = location

    def __lt__(self, other):
        if other.weight == self.weight or self.weight is None:
            return False
        if other.weight is None:
            return True
        else:
            return self.weight < other.weight

    def set_origin(self):
        self.weight = 0
        self.visited = True

    def add_adj(self, node_id):
        self.adj_list.append(node_id)

    def __str__(self):
        return "%s %s %s" % (self.id, self.weight, self.visited)

    def get_weight(self):
        if self.weight is None:
            return -1
        else:
            return self.weight


class Graph:
    def __init__(self, node_dict):
        self.my_dict = {}
        self.min_heap = MinHeap()
        self.origin = None
        for i in node_dict:
            my_node = Node(i)
            self.my_dict[i] = my_node
            self.min_heap.add(my_node)
        for from_node, edge_list in node_dict.items():
            for to_node, weight in edge_list:
                self.my_dict[from_node].add_adj(Edge(self.my_dict[to_node],weight))
        a = 1

    def set_origin(self, origin):
        self.origin = origin
        my_node = self.my_dict[origin]
        my_node.weight = 0
        self.min_heap.bubble_up(my_node.heap_location)

    def should_continue(self):
        return len(self.min_heap) > 0 and self.min_heap.query().weight is not None

    def get_min(self):
        return self.min_heap.extract()

    def relax(self, my_node, update_weight):
        if my_node.weight is None or update_weight < my_node.weight:
            my_node.weight = update_weight
            self.min_heap.bubble_up(my_node.heap_location)

    def __str__(self):
        result = ""
        for node_id in sorted(self.my_dict):
            if node_id != self.origin:
                result += str(self.my_dict[node_id].get_weight()) + " "
        return result.strip()


class MinHeap:
    def __init__(self):
        self.min_heap = []

    def __len__(self):
        return len(self.min_heap)

    def add(self, value):
        self.min_heap.append(value)
        self.update_heap(len(self.min_heap) - 1)
        self.bubble_up(len(self.min_heap) - 1)

    def bubble_up(self, index):
        if index > 0:
            parent = self._get_parent(index)
            if self.min_heap[index] < self.min_heap[parent]:
                self._swap(index, parent)
                self.bubble_up(parent)

    def update_heap(self, location):
        self.min_heap[location].update_heap(location)

    def query(self):
        return self.min_heap[0]

    def extract(self):
        result = self.query()
        self.min_heap[0].update_heap(None)
        self.min_heap[0] = self.min_heap[len(self.min_heap) - 1]
        self.min_heap[0].update_heap(0)
        del self.min_heap[len(self.min_heap) - 1]
        self._heapify(0)
        return result

    def _heapify(self, index):
        index_left = self._get_left(index)
        index_right = self._get_right(index)
        if index_left >= len(self.min_heap):
            return
        if index_right >= len(self.min_heap):
            index_child = index_left
        else:
            index_child = index_right if self.min_heap[index_right] < self.min_heap[index_left] else index_left
        if self.min_heap[index_child] < self.min_heap[index]:
            self._swap(index, index_child)
            self._heapify(index_child)

    def _swap(self, index1, index2):
        self.min_heap[index1], self.min_heap[index2] = self.min_heap[index2], self.min_heap[index1]
        self.update_heap(index1)
        self.update_heap(index2)

    def _get_left(self, index):
        return (index + 1) * 2 - 1

    def _get_right(self, index):
        return self._get_left(index) + 1

    def _get_parent(self, index):
        return (index-1) // 2

class SnakesAndLadders:
    MAX_THROW, MAX_SQUARES = 6, 100
    def __init__(self):
        self.node_dict={i:[] for i in range(SnakesAndLadders.MAX_SQUARES)}
        snake_heads = self.read_file()
        self.add_throws(snake_heads)
        self.graph = Graph(self.node_dict)

    def add_throws(self, snake_heads: set):
        for node_from in range(SnakesAndLadders.MAX_SQUARES):
            if node_from not in snake_heads:
                for node_to in range(node_from+1,node_from+1+SnakesAndLadders.MAX_THROW):
                    if node_to < SnakesAndLadders.MAX_SQUARES:
                        self.node_dict[node_from].append((node_to,1))

    def calculate(self):
        origin = 0
        destination = SnakesAndLadders.MAX_SQUARES-1
        self.graph.set_origin(origin)
        while self.graph.should_continue():
            current_node = self.graph.get_min()
            for edge in current_node.adj_list:
                if not edge.node.visited:
                    self.graph.relax(edge.node, current_node.weight + edge.weight)
            current_node.visited = True
            if current_node.id == destination:
                return current_node.weight
        return -1



    def read_file(self):
        n_ladders = int(input())
        for _ in range(n_ladders):
            node1, node2 = [i-1 for i in get_int_list(input())]
            self.node_dict[node1].append((node2,0))
        n_snakes = int(input())
        snake_heads = set()
        for _ in range(n_snakes):
            node1, node2 = [i-1 for i in get_int_list(input())]
            self.node_dict[node1].append((node2,0))
            snake_heads.add(node1)
        return snake_heads



def main():
    cases = int(input())
    for _ in range(cases):
        my_obj = SnakesAndLadders()
        print(my_obj.calculate())


def get_int_list(in_str):
    return [int(i) for i in in_str.strip().split()]


if __name__ == "__main__":
    main()
