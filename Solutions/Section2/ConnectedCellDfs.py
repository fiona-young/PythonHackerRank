import collections

DfsRecord = collections.namedtuple('DfsRecord', 'time type id')


class DfsList:
    VISIT, LEAVE = 'visit', 'leave'

    def __init__(self):
        self.time = 0
        self.dfs_list = []
        self.last_parent_time = None
        self.tree_sizes = []
        self.tree_max = 0

    def add(self, node_id, visit_type):
        self.dfs_list.append(DfsRecord(self.time, visit_type, node_id))
        self.time += 1

    def visit(self, node_id):
        self.add(node_id, DfsList.VISIT)

    def leave(self, node_id):
        self.add(node_id, DfsList.LEAVE)

    def visit_root(self, node_id):
        self.last_parent_time = self.time
        self.visit(node_id)

    def leave_root(self, node_id):
        self.leave(node_id)
        tree_size = (self.time - self.last_parent_time)//2
        self.tree_sizes.append(tree_size)
        self.tree_max = max(self.tree_max, tree_size)

    def get_biggest_tree_size(self):
        return self.tree_max


class ConnectedCell:
    def __init__(self):
        dict_ones = self.read_input()
        self.graph = self.build_graph(dict_ones)

    def build_graph(self, dict_ones):
        graph = {x: [] for x in range(len(dict_ones))}
        for (i_row, j_row), index in dict_ones.items():
            add_edges = self.get_edges(dict_ones, i_row, j_row, index)
            for node1, node2 in add_edges:
                graph[node1].append(node2)
                graph[node2].append(node1)
        return graph

    def read_input(self):
        dict_ones = {}
        rows = int(input())
        _ = int(input())
        index = 0
        for i_rows in range(rows):
            for j_rows, val in enumerate(get_int_list(input())):
                if val == 1:
                    dict_ones[i_rows, j_rows] = index
                    index += 1
        return dict_ones

    def calculate(self):
        dfs_list = self.dfs_search()
        return dfs_list.get_biggest_tree_size()

    def dfs_search(self):
        unvisited_set = set(self.graph.keys())
        dfs_list = DfsList()
        while len(unvisited_set) > 0:
            root_node = unvisited_set.pop()
            dfs_list.visit_root(root_node)
            self.dfs_visit_children(unvisited_set, dfs_list, root_node)
            dfs_list.leave_root(root_node)
        return dfs_list

    def dfs_visit_children(self, unvisited_set :set, dfs_list: DfsList, parent_node: int):
        for child_node in self.graph[parent_node]:
            if child_node in unvisited_set:
                unvisited_set.discard(child_node)
                dfs_list.visit(child_node)
                self.dfs_visit_children(unvisited_set, dfs_list, child_node)
                dfs_list.leave(child_node)

    def get_edges(self, dict_ones, i_row, j_row, index):
        edges = []
        possible_connections = {'cell_down': (i_row + 1, j_row),
                                'cell_right': (i_row, j_row + 1),
                                'cell_right_down': (i_row + 1, j_row + 1),
                                'cell_left_down': (i_row - 1, j_row + 1)}
        for check_connection in possible_connections.values():
            if check_connection in dict_ones:
                edges.append((index, dict_ones[check_connection]))
        return edges


def main():
    my_obj = ConnectedCell()
    print(my_obj.calculate())


def get_int_list(in_str):
    return [int(i) for i in in_str.strip().split()]


if __name__ == "__main__":
    main()
