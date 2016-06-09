class DisjointSet:
    def __init__(self, node_count):
        self.forest = {x: {x} for x in range(node_count)}
        self.pointer_list = [x for x in range(node_count)]

    def find(self, x):
        return self.pointer_list[x]

    def union(self, x, y):
        if self.find(x) == self.find(y):
            return
        if len(self.forest[self.find(y)]) > len(self.forest[self.find(x)]):
            x, y = y, x
        y_dest = self.find(x)
        y_origin = self.find(y)
        for y_val in self.forest[y_origin]:
            self.pointer_list[y_val] = y_dest
        self.forest[y_dest].update(self.forest[y_origin])
        self.forest[y_origin].clear()

    def max_size(self):
        max_size = 0
        for trees in self.forest.values():
            max_size = max(max_size, len(trees))
        return max_size


class ConnectedCell:
    def __init__(self):
        self.dict_ones = self.read_input()
        self.disjoint_set = DisjointSet(len(self.dict_ones))

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
        for (i_row, j_row), index in self.dict_ones.items():
            self.add_edges(i_row, j_row, index)
        return self.disjoint_set.max_size()

    def add_edges(self, i_row, j_row, index):
        possible_connections = {'cell_down': (i_row + 1, j_row),
                                'cell_right': (i_row, j_row + 1),
                                'cell_right_down': (i_row + 1, j_row + 1),
                                'cell_left_down': (i_row - 1, j_row + 1)}
        for check_connection in possible_connections.values():
            if check_connection in self.dict_ones:
                self.disjoint_set.union(index, self.dict_ones[check_connection])


def main():
    my_obj = ConnectedCell()
    print(my_obj.calculate())


def get_int_list(in_str):
    return [int(i) for i in in_str.strip().split()]


if __name__ == "__main__":
    main()
