import collections

Edge = collections.namedtuple("Edge", "weight node0 node1")
NodeEdge = collections.namedtuple("NodeEdge", "node weight")


class ReallySpecialSubtree:
    def __init__(self, node_count):
        self.weight = 0
        self.forest = {}
        for i in range(1, node_count + 1):
            self.forest[i - 1] = {i}

    def add_edge(self, edge: Edge):
        combine_groups = []
        for tree_id, tree_set in self.forest.items():
            if edge.node0 in tree_set or edge.node1 in tree_set:
                combine_groups.append(tree_id)
        if len(combine_groups) == 2:
            self.forest[combine_groups[0]].update(self.forest[combine_groups[1]])
            self.weight += edge.weight
            del self.forest[combine_groups[1]]

    @property
    def connected(self):
        return len(self.forest) == 1


class Graph:
    def __init__(self, node_count, edge_list: list):
        self.min_span_tree = ReallySpecialSubtree(node_count)
        self.weight_list = []
        for edge in edge_list:
            node0 = edge[0]
            node1 = edge[1]
            weight = edge[2]
            self.weight_list.append(Edge(weight, node1, node0))
        self.weight_list.sort()

    def calculate(self, origin):
        i_weight = 0
        while not self.min_span_tree.connected:
            edge = self.weight_list[i_weight]
            self.min_span_tree.add_edge(edge)
            i_weight += 1
        print(self.min_span_tree.weight)


def main():
    in_str = input()
    edge_list = []
    nodes, edges = get_int_list(in_str)
    for i in range(edges):
        edge_str = input()
        edge_list.append(get_int_list(edge_str))
    origin = int(input().strip())
    my_obj = Graph(nodes, edge_list)
    my_obj.calculate(origin)


def get_int_list(in_str):
    return [int(i) for i in in_str.strip().split()]


if __name__ == "__main__":
    main()
