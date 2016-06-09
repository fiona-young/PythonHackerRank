import collections

Edge = collections.namedtuple("Edge", "node1 node2 weight")
class MinimumPenaltyPath:
    def __init__(self, node_count, edge_list: list):
        self.node_count = node_count
        self.edge_list = edge_list
        self.node_list = {}
        for i in range(node_count):
            self.node_list[i] ={"distance":None, "predecessor":None}

    def calculate(self, origin, destination):
        self.node_list[origin]['distance']=0
        for i in range(self.node_count-1):
            for node1, node2, weight in self.edge_list:
                if self.node_list[node1]['distance'] is not None:
                    if self.node_list[node2]['distance'] is None or (
                                self.node_list[node1]['distance'] | weight) < self.node_list[node2]['distance']:
                        self.node_list[node2]['distance']=weight|self.node_list[node1]['distance']
                        self.node_list[node2]['predecessor']=node1

        for node1, node2, weight in self.edge_list:
            if self.node_list[node1]['distance'] is not None and self.node_list[node2]['distance'] is None:
                if (self.node_list[node1]['distance'] | weight) < self.node_list[node2]['distance']:
                    print ("Graph contains -ve weight cycle")
        return self.node_list[destination]['distance']


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
