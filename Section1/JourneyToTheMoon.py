class Graph:
    def __init__(self, node_count, edge_list: list):
        self.node_count = node_count
        self.node_groups = {x: {x} for x in range(node_count)}
        self.node_lookups = {x: x for x in range(node_count)}
        for node1, node2 in edge_list:
            new_set_id = self.node_lookups[node1]
            old_set_id = self.node_lookups[node2]
            if old_set_id == new_set_id:
                continue
            self.node_groups[new_set_id].update(self.node_groups[old_set_id])
            for move_node in self.node_groups[old_set_id]:
                self.node_lookups[move_node] = new_set_id
            del (self.node_groups[old_set_id])

    def calculate(self):
        print(self.unique_pairs_in_sets())

    def unique_pairs_in_sets(self):
        total = unique_pairs(self.node_count)
        for node_group in self.node_groups.values():
            total -= unique_pairs(len(node_group))
        return total


def unique_pairs(n):
    return (n * (n - 1)) // 2


def main():
    edge_list = []
    in_str = input()
    nodes, edges = get_int_list(in_str)
    for j in range(edges):
        node1, node2 = get_int_list(input())
        edge_list.append([node1, node2])
    my_obj = Graph(nodes, edge_list)
    my_obj.calculate()


def get_int_list(in_str):
    return [int(i) for i in in_str.strip().split()]


if __name__ == "__main__":
    main()
