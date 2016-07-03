import collections

Edge = collections.namedtuple("Edge", "weight node0 node1")
NodeEdge = collections.namedtuple("NodeEdge", "node weight")

class Node:
    compare = 0
    def __init__(self, id_var):
        self.id = id_var
        self.distance = None
        self.parent = None
        self.visited = False

    def update(self, distance, parent):
        self.distance = distance
        self.parent = parent
        self.visited = True

    def __str__(self):
        return "d %s p %s"%(self.distance,self.parent.id)

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
        self.node_count = node_count
        self.min_span_tree = ReallySpecialSubtree(node_count)
        self.weight_list = []
        for edge in edge_list:
            self.weight_list.append(Edge(edge[2], edge[1], edge[0]))
        self.weight_list.sort()
        self.node_dict = {i: {} for i in range(node_count)}

    def exclude_heavy_edges(self):
        output_edge=[]
        i_weight = 0
        while not self.min_span_tree.connected:
            edge = self.weight_list[i_weight]
            self.min_span_tree.add_edge(edge)
            output_edge.append(edge)
            i_weight += 1
        return output_edge

    def calculate(self):
        self.weight_list = self.exclude_heavy_edges()
        for edge in self.weight_list:
            self.node_dict[edge.node0-1][edge.node1-1]=2**edge.weight
            self.node_dict[edge.node1-1][edge.node0-1]=2**edge.weight
        sum = 0
        for i in range(self.node_count-1):
            nodes = self.breadth_first_search(i)
            for j in range(i, self.node_count):
                if i!=j:
                    sum+=nodes[j].distance
        print('{:b}'.format(sum))


    def breadth_first_search(self, origin):
        node_list = [Node(i) for i in range(self.node_count)]
        node_list[origin].distance = 0
        node_list[origin].visited = True
        queue = collections.deque()
        queue.append(node_list[origin])
        while len(queue) > 0:
            current_node = queue.popleft()
            for to_node, weight in self.node_dict[current_node.id].items():
                if not node_list[to_node].visited:
                    node_list[to_node].update(current_node.distance+weight,current_node)
                    queue.append(node_list[to_node])
        return node_list

def main():
    in_str = input()
    edge_list = []
    nodes, edges = get_int_list(in_str)
    for i in range(edges):
        edge_str = input()
        edge_list.append(get_int_list(edge_str))
    my_obj = Graph(nodes, edge_list)
    my_obj.calculate()


def get_int_list(in_str):
    return [int(i) for i in in_str.strip().split()]


if __name__ == "__main__":
    main()
