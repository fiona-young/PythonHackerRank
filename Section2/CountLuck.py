import collections

DfsRecord = collections.namedtuple('DfsRecord', 'time type id')


def read_input():
    available = '.'
    origin = 'M'
    destination = '*'
    dict_available_points = {}
    rows, _ = get_int_list(input())
    index = 0
    origin_location = None
    destination_location = None
    for i_rows in range(rows):
        for i_cols, val in enumerate(input()):
            if val == origin:
                origin_location = index
            if val == destination:
                destination_location = index
            if val in (available, origin, destination):
                dict_available_points[i_rows, i_cols] = index
                index += 1

    return dict_available_points, origin_location, destination_location


class BfsNode:
    def __init__(self, node_id):
        self.id = node_id
        self.parent = None
        self.visited = False
        self.distance = None

    def visit(self, distance, parent):
        self.distance = distance
        self.parent = parent
        self.visited = True


class CountLuck:
    def __init__(self):
        dict_available_points, self.origin, self.destination = read_input()
        self.turns = int(input())
        self.graph = self.build_graph(dict_available_points)

    def build_graph(self, dict_available_points):
        graph = {x: [] for x in range(len(dict_available_points))}
        for (i_row, j_row), index in dict_available_points.items():
            add_edges = self.get_edges(dict_available_points, i_row, j_row, index)
            for node1, node2 in add_edges:
                graph[node1].append(node2)
                graph[node2].append(node1)
        return graph

    def calculate(self):
        path_list = self.bfs_search(self.origin, self.destination)
        required_decisions = self.path_decisions(path_list)
        if self.turns == required_decisions:
            return "Impressed"
        else:
            return "Oops!"

    def path_decisions(self, path_list):
        decisions = 0
        if len(self.graph[path_list[0]]) > 1:  # first step have all choices
            decisions += 1
        for node_id in path_list[1:-1]:
            if len(self.graph[node_id]) > 2:  # subsequent steps do not retrace steps
                decisions += 1
        return decisions

    def bfs_search(self, origin, destination):
        bfs_queue = collections.deque()
        bfs_nodes = {node_id: BfsNode(node_id) for node_id in self.graph.keys()}
        bfs_queue.append(origin)
        bfs_nodes[origin].visit(0, None)
        while len(bfs_queue) > 0:
            current_node = bfs_queue.popleft()
            for next_node in self.graph[current_node]:
                if not bfs_nodes[next_node].visited:
                    bfs_queue.append(next_node)
                    bfs_nodes[next_node].visit(bfs_nodes[origin].distance + 1, current_node)
                    if next_node == destination:
                        bfs_queue.clear()
                        break
        bfs_path = collections.deque()
        current_node = bfs_nodes[destination]
        while current_node.parent is not None:
            bfs_path.appendleft(current_node.id)
            current_node = bfs_nodes[current_node.parent]
        bfs_path.appendleft(current_node.id)
        return list(bfs_path)

    def get_edges(self, dict_ones, i_row, i_col, index):
        edges = []
        possible_connections = {'cell_down': (i_row + 1, i_col),
                                'cell_right': (i_row, i_col + 1)}
        for check_connection in possible_connections.values():
            if check_connection in dict_ones:
                edges.append((index, dict_ones[check_connection]))
        return edges


def main():
    cases = int(input())
    for i in range(cases):
        my_obj = CountLuck()
        print(my_obj.calculate())


def get_int_list(in_str):
    return [int(i) for i in in_str.strip().split()]


if __name__ == "__main__":
    main()
