import collections

Edge = collections.namedtuple('Edge', 'node1 node2 weight')
Adj = collections.namedtuple('Adj', 'to weight')

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


class MinimumPenaltyPath:
    def __init__(self, node_count, edge_list: list):
        self.node_count = node_count
        self.edge_list = edge_list
        self.node_dict = {i: collections.defaultdict(list) for i in range(node_count)}
        for node1, node2, weight in edge_list:
            self.node_dict[node1][node2].append(Adj(node2, weight))

    def breadth_first_search(self, origin, destination, bit_mask=None):
        node_list = [Node(i) for i in range(self.node_count)]
        node_list[origin].distance = 0
        node_list[origin].visited = True
        queue = collections.deque()
        queue.append(node_list[origin])
        while len(queue) > 0:
            current_node = queue.popleft()
            for to_node, edge_list in self.node_dict[current_node.id].items():
                if not node_list[to_node].visited:
                    can_use, weight = self.process_adj(edge_list, bit_mask)
                    if can_use:
                        node_list[to_node].update(current_node.distance | weight, current_node.id)
                        if to_node == destination:
                            return True, node_list[to_node].distance
                        queue.append(node_list[to_node])
        return False, None

    def process_adj(self, edge_list, bit_mask):
        weight_pass = []
        for to, weight in edge_list:
            Node.compare += 1
            if bit_mask == None or ((weight | bit_mask) == bit_mask):
                weight_pass.append(weight)
        if len(weight_pass) == 0:
            return False, None
        else:
            return True, min(weight_pass)

    def calculate(self, origin, destination):
        path_existed, path_weight = self.breadth_first_search(origin, destination)
        if not path_existed:
            return -1
        best_weight = path_weight
        mask_len = path_weight.bit_length()
        last_mask = '1' * mask_len
        for i in range(mask_len):
            try_mask = last_mask[:i] + '0' + last_mask[i + 1:]
            masked_path_exists, masked_path_weight = self.breadth_first_search(origin, destination, int(try_mask, 2))
            if masked_path_exists:
                best_weight = masked_path_weight
                last_mask = try_mask
        return best_weight


def main():
    in_str = input()
    edge_list = []
    nodes, edges = get_int_list(in_str)
    for i in range(edges):
        node1, node2, weight = get_int_list(input())
        edge_list.append(Edge(node1 - 1, node2 - 1, weight))
        edge_list.append(Edge(node2 - 1, node1 - 1, weight))
    Node.compare = 0
    my_object = MinimumPenaltyPath(nodes, edge_list)
    origin, destination = get_int_list(input())
    print(my_object.calculate(origin - 1, destination - 1))
    #print(Node.compare)

def get_int_list(in_str):
    return [int(i) for i in in_str.strip().split()]


if __name__ == "__main__":
    main()
