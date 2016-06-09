class Node():
    def __init__(self, node_id, graph: dict, added_set: set):
        added_set.add(node_id)
        self.id = node_id
        self.weight = graph[node_id]['weight']
        self.children = []
        self.total_weight = self.weight
        for child_id in graph[node_id]['adj']:
            if child_id not in added_set:
                child = Node(child_id, graph, added_set)
                self.total_weight += child.total_weight
                self.children.append(child)

    def get_min_weight_diff(self, min_weight_diff, total_tree_weight):
        for child in self.children:
            child_tree_weight = child.total_weight
            remaining_tree_weight = total_tree_weight - child.total_weight
            difference = abs(remaining_tree_weight - child_tree_weight)
            if difference < min_weight_diff:
                min_weight_diff = difference
            min_weight_diff = child.get_min_weight_diff(min_weight_diff, total_tree_weight)
        return min_weight_diff


class Tree:
    def __init__(self, graph):
        self.root_id = self.get_root(graph)
        self.root = Node(self.root_id, graph, set())

    def get_min_weight_diff(self):
        min_weight_diff = self.root.total_weight
        min_weight_diff = self.root.get_min_weight_diff(min_weight_diff, self.root.total_weight)
        return min_weight_diff

    def get_root(self, graph: dict):
        for i_node, data in graph.items():
            if len(data['adj']) > 1:
                return i_node
        return list(graph.keys())[0]


def read_input():
    nodes = int(input())
    node_weights = get_int_list(input())
    edge_list = []
    for i_edges in range(nodes - 1):
        edge_list.append(get_int_list(input()))
    return node_weights, edge_list


class CutTheTree:
    def __init__(self):
        weight_list, edge_list = read_input()
        graph = self.build_graph(weight_list, edge_list)
        self.tree = Tree(graph)

    def build_graph(self, weight_list, edge_list):
        graph = {i: {'weight': weight, 'adj': []} for i, weight in enumerate(weight_list, 1)}
        for node1, node2 in edge_list:
            graph[node1]['adj'].append(node2)
            graph[node2]['adj'].append(node1)
        return graph

    def calculate(self):
        return self.tree.get_min_weight_diff()


def main():
    my_obj = CutTheTree()
    print(my_obj.calculate())


def get_int_list(in_str):
    return [int(i) for i in in_str.strip().split()]


if __name__ == "__main__":
    main()
