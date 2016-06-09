class Node():
    def __init__(self, node_id, parent, weight):
        self.id = node_id
        self.parent = parent
        self.weight = weight
        self.children = []
        self.total_weight = weight

    def __str__(self):
        return 'id %s weight %s child_count %s' % (self.id, self.total_weight, len(self.children))

    def build_tree(self, graph: dict, added_set: set):
        my_node = self
        while my_node is not None:
            added_set.add(my_node.id)
            if len(graph[my_node.id]['adj']) > 0:
                child_id = graph[my_node.id]['adj'].pop()
                if child_id not in added_set:
                    child = Node(child_id, my_node, graph[child_id]['weight'])
                    graph[child_id]['adj'].remove(my_node.id)
                    my_node.children.append(child)
                    my_node = child
            else:
                if my_node.parent is not None:
                    my_node.parent.total_weight += my_node.total_weight
                my_node = my_node.parent

    def get_min_weight_diff(self):
        process_list = [self]
        total_tree_weight = self.total_weight
        min_weight_diff = self.total_weight
        while len(process_list) > 0:
            my_node = process_list.pop()
            for child in my_node.children:
                process_list.append(child)
                child_tree_weight = child.total_weight
                remaining_tree_weight = total_tree_weight - child.total_weight
                difference = abs(remaining_tree_weight - child_tree_weight)
                if difference < min_weight_diff:
                    min_weight_diff = difference
        return min_weight_diff


class Tree:
    def __init__(self, graph):
        root_id = self.get_root(graph)
        self.root = Node(root_id, None,graph[root_id]['weight'])
        self.root.build_tree(graph, set())

    def get_min_weight_diff(self):
        return self.root.get_min_weight_diff()

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
        graph = {i: {'weight': weight, 'adj': set()} for i, weight in enumerate(weight_list, 1)}
        for node1, node2 in edge_list:
            graph[node1]['adj'].add(node2)
            graph[node2]['adj'].add(node1)
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
