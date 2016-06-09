import collections

Edge = collections.namedtuple("Edge", "node weight")


class Node:
    def __init__(self, node_id):
        self.id = node_id
        self.inserted = False
        self.adj_list = []

    def add_adj(self, node_id):
        self.adj_list.append(node_id)


class Graph:
    def __init__(self, node_count, edge_list: list):
        self.my_dict = {}
        self.origin = None
        for i in range(1, node_count + 1):
            my_node = Node(i)
            self.my_dict[i] = my_node
        for edge in edge_list:
            node1 = self.my_dict[edge[0]]
            node2 = self.my_dict[edge[1]]
            node1.add_adj(Edge(node2, edge[2]))
            node2.add_adj(Edge(node1, edge[2]))

    def calculate(self, origin):
        weight_sum = 0
        min_span_tree = {}
        frontier = {origin}
        self.my_dict[origin].inserted = True
        while len(frontier) > 0:
            next_val = None
            for node_id in frontier.copy():
                my_node = self.my_dict[node_id]
                all_added = True
                for edge in my_node.adj_list:
                    if not edge.node.inserted:
                        all_added = False
                        if next_val is None or edge.weight < next_val.weight:
                            next_val = edge
                if all_added:
                    frontier.remove(node_id)
            if next_val is not None:
                next_val.node.inserted = True
                frontier.add(next_val.node.id)
                min_span_tree[next_val.node.id]=next_val.weight
                weight_sum+=next_val.weight
        print(weight_sum)



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
