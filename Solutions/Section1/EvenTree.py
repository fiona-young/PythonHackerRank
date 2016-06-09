class Tree:
    def __init__(self, root, adj_dict):
        self.root = root
        self.added = {root}
        self.tree = self.depth_search(root, set(), adj_dict)
        self.breaks = 0

    def depth_search(self, current_node, added_set, adj_dict):
        result = {current_node:{}}
        added_set.add(current_node)
        for next_node in adj_dict[current_node].difference(added_set):
            result[current_node].update(self.depth_search(next_node, added_set, adj_dict))
        return result

    def get_breaks(self):
        self.walk(self.tree[self.root])
        return self.breaks

    def walk(self, my_tree):
        count_outer = 0
        for key, value in my_tree.items():
            count = 1
            if value != {}:
                count += self.walk(value)
            if count % 2 == 0:
                self.breaks += 1
                count = 0
            count_outer += count
        return count_outer


class Forest:
    def __init__(self, node_count, edge_list: list):
        adj_dict = {}
        for i_node in range(1, node_count + 1):
            adj_dict[i_node] = set()
        for node1, node2 in edge_list:
            adj_dict[node1].add(node2)
            adj_dict[node2].add(node1)
        self.tree = Tree(edge_list[0][0], adj_dict)

    def calculate(self):
        print(self.tree.get_breaks())


def main():
    edge_list = []
    in_str = input()
    nodes, edges = get_int_list(in_str)
    for i in range(edges):
        edge_str = input()
        edge_list.append(get_int_list(edge_str))
    my_obj = Forest(nodes, edge_list)
    my_obj.calculate()


def get_int_list(in_str):
    return [int(i) for i in in_str.strip().split()]


if __name__ == "__main__":
    main()
