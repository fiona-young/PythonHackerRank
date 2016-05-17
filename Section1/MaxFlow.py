import collections
Edge = collections.namedtuple("Edge", "node capacity")
class MaxFlow:
    def __init__(self, node_count, source, sink, capacity):
        self.node_count = node_count
        self.source = source
        self.sink = sink
        self.capacity = capacity
        self.flow = [[0]*self.node_count for _ in range(self.node_count)]

    def calculate(self):
        residual = self.get_residual()
        a = 1

    def get_residual(self):
        residual = collections.defaultdict(list)
        for (n1, n2), capacity in self.capacity.items():
            if (capacity - self.flow[n1][n2]) > 0:
                residual[n1].append(Edge(n2,capacity - self.flow[n1][n2]))
            if self.flow[n1][n2]>0:
                residual[n2].append(Edge(n1,self.flow[n1][n2]))
        return residual


def get_adj_dict(edges):
    adj_dict={}
    for n1, n2, capacity in edges:
        adj_dict[n1,n2]= capacity
    return adj_dict