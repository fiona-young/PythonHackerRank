from collections import namedtuple, defaultdict

Priority = namedtuple('Priority','priority node')
class Graph:
    def __init__(self, node_count, max_feet, edge_list: list):
        self.node_count = node_count * 2 + 2
        adj_dict = defaultdict(set)
        for node1, node2 in edge_list:
            adj_dict[node1].add(node2)
            adj_dict[node2].add(node1)
        self.capacity = [[0]*self.node_count for i in range(self.node_count)]
        source = 2*node_count
        sink = source+1
        for node in range(node_count):
            bi_front = node * 2
            bi_back = node * 2 + 1
            self.capacity[source][bi_front]=min(len(adj_dict[node]),max_feet)
            self.capacity[bi_back][sink]= 1
        for node1, adj_set in adj_dict.items():
            for node2 in adj_set:
                self.capacity[node1*2][node2*2+1]=1
                self.capacity[node1*2+1][node2*2]=1

        a = 1


    def calculate(self):
        flow = [[0]*self.node_count for i in range(self.node_count)]
        print(1)


def main():
    cases = int(input())
    for i in range(cases):
        edge_list = []
        in_str = input()
        nodes,max_feet, edges = get_int_list(in_str)
        for j in range(edges):
            node1, node2 = get_int_list(input())
            edge_list.append([node1-1, node2-1])
        my_obj = Graph(nodes,max_feet,  edge_list)
        my_obj.calculate()


def get_int_list(in_str):
    return [int(i) for i in in_str.strip().split()]


if __name__ == "__main__":
    main()
