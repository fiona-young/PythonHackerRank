import collections

Edge = collections.namedtuple("Edge", "node1 node2 weight")
class MinimumPenaltyPath:
    def __init__(self, node_count, edge_list: list):
        self.node_count = node_count
        self.edge_list = edge_list


    def calculate(self, origin, destination):
        return 1


def main():
    in_str = input()
    edge_list = []
    nodes, edges = get_int_list(in_str)
    for i in range(edges):
        node1, node2, weight = get_int_list(input())
        edge_list.append(Edge(node1-1, node2-1, weight))
        edge_list.append(Edge(node2-1, node1-1, weight))
    my_object = MinimumPenaltyPath(nodes, edge_list)
    origin, destination = get_int_list(input())
    print (my_object.calculate(origin-1, destination-1))



def get_int_list(in_str):
    return [int(i) for i in in_str.strip().split()]


if __name__ == "__main__":
    main()
