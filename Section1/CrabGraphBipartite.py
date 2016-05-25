import collections

class Graph:
    def __init__(self, node_count, max_feet, edge_list: list):
        self.node_count = node_count * 2 + 2
        adj_dict = collections.defaultdict(set)
        for node1, node2 in edge_list:
            adj_dict[node1].add(node2)
            adj_dict[node2].add(node1)
        self.source = 2*node_count
        self.sink = self.source+1
        self.capacity = {}
        for node in range(node_count):
            bi_front = node * 2
            bi_back = node * 2 + 1
            self.capacity[self.source,bi_front]=min(len(adj_dict[node]),max_feet)
            self.capacity[bi_back,self.sink]= 1
        for node1, adj_set in adj_dict.items():
            for node2 in adj_set:
                self.capacity[node1*2,node2*2+1]=1
                self.capacity[node2*2,node1*2+1]=1

    def calculate(self):
        maxFlow = MaxFlow(self.node_count,self.source, self.sink,self.capacity)
        print(maxFlow.calculate())

Edge = collections.namedtuple("Edge", "node capacity")


class MaxFlow:
    def __init__(self, node_count, source, sink, capacity: dict):
        self.node_count = node_count
        self.source = source
        self.sink = sink
        self.capacity = capacity
        self.flow = {keys:0 for keys in self.capacity.keys()}

    def calculate(self):
        while True:
            residual = self.get_residual()
            shortest_path, flow = self.breadth_first_search(residual)
            if len(shortest_path) == 0:
                break
            self.add_flow(shortest_path, flow)
        return sum([flow for (n1, n2), flow in self.flow.items() if n1 == self.source])

    def add_flow(self, shortest_path, flow):
        for i in range(len(shortest_path) - 1):
            from_node = shortest_path[i]
            to_node = shortest_path[i + 1]
            if (from_node, to_node) in self.capacity:
                self.flow[from_node, to_node] += flow
            else:
                self.flow[to_node, from_node] -= flow

    def get_residual(self):
        residual = {i: [] for i in range(self.node_count)}

        for (n1, n2), capacity in self.capacity.items():
            if (capacity - self.flow[n1, n2]) > 0:
                residual[n1].append(Edge(n2, capacity - self.flow[n1, n2]))
            if self.flow[n1, n2] > 0:
                residual[n2].append(Edge(n1, self.flow[n1, n2]))
        return residual

    def breadth_first_search(self, graph: dict):
        node_dict = {node_id: Node(node_id) for node_id in graph.keys()}
        queue = collections.deque()
        queue.append(node_dict[self.source])
        node_dict[self.source].length = 0
        while len(queue) > 0:
            current_node = queue.popleft()
            current_node.visited = True
            for adj_node_id, capacity in graph[current_node.node_id]:
                adj_node = node_dict[adj_node_id]
                if not adj_node.visited:
                    adj_node.update(current_node.node_id, capacity, current_node.length + 1)
                    queue.append(adj_node)
                    if adj_node_id == self.sink:
                        queue.clear()
                        break
        my_node = node_dict[self.sink]
        if not my_node.visited:
            return [], None
        weight = my_node.weight
        path = []
        while my_node.parent is not None:
            path.append(my_node.node_id)
            weight = min(weight, my_node.weight)
            my_node = node_dict[my_node.parent]
        path.append(self.source)
        path.reverse()
        return path, weight


class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.length = None
        self.weight = None
        self.visited = False
        self.parent = None

    def update(self, parent_id, weight, length):
        self.parent = parent_id
        self.weight = weight
        self.length = length
        self.visited = True

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
