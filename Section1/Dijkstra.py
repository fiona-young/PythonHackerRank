import collections

Edge = collections.namedtuple("Edge","node weight")

class Node:
    def __init__(self, node_id):
        self.id = node_id
        self.weight = None
        self.visited = False

    def __lt__(self,other):
        if other.weight == self.weight or self.weight is None:
            return False
        if other.weight is None:
            return True
        else:
            return self.weight < other.weight

    def set_origin(self):
        self.weight = 0
        self.visited = True

    def relax(self, new_weight):
        if self.weight is None or new_weight < self.weight:
            self.weight = new_weight

    def __str__(self):
        return "%s %s %s"%(self.id,self.weight, self.visited)

    def get_weight(self):
        if self.weight is None:
            return -1
        else:
            return self.weight

class Dijkstra:
    def __init__(self,node_count, edge_list: list):
        self.adj = {}
        self.my_list = {}
        for i in range(1,node_count+1):
            my_node = Node(i)
            self.adj[i]=[]
            self.my_list[i]=my_node
        for edge in edge_list:
            self.adj[edge[0]].append(Edge(edge[1],edge[2]))
            self.adj[edge[1]].append(Edge(edge[0],edge[2]))

    def get_min(self, unvisited_set):
        current = None
        for node_id in unvisited_set:
            if current is None:
                current = node_id
            elif self.my_list[node_id] < self.my_list[current]:
                current = node_id
        return current

    def calculate(self, origin):
        self.my_list[origin].weight = 0
        unvisited_set=set(self.adj)
        while len(unvisited_set) > 0:
            current_node_id = self.get_min(unvisited_set)
            if self.my_list[current_node_id].weight is None:
                break
            for edge in self.adj[current_node_id]:
                if not self.my_list[edge.node].visited:
                    self.my_list[edge.node].relax(self.my_list[current_node_id].weight + edge.weight)
            self.my_list[current_node_id].visited = True
            unvisited_set.discard(current_node_id)
        result = ""
        for node_id in sorted(self.my_list):
            if node_id != origin:
                result+=str(self.my_list[node_id].get_weight())+" "
        print(result.strip())


def main():
    case_str = input().strip()
    cases = int(case_str)
    for i in range(cases):
        in_str = input()
        edge_list = []
        nodes, edges = get_int_list(in_str)
        for i in range(edges):
            edge_str = input()
            edge_list.append(get_int_list(edge_str))
        origin = int(input().strip())
        my_obj = Dijkstra(nodes, edge_list)
        my_obj.calculate(origin)


def get_int_list(in_str):
    return [int(i) for i in in_str.strip().split()]

if __name__ == "__main__":
    main()