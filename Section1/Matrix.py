
def get_binary_list(target_val):
    target = target_val
    i = 1
    row = 0
    current_val = 0

    while target_val/2 > 1:
        if target_val%(2*i):
            current_val += i
            print(row, i, current_val, target)
            target_val -= i
        i = i*2
        row += 1

get_binary_list(502014773)
get_binary_list(15)

class Matrix:
    @staticmethod
    def get_from_edges(dimension, adj_list):
        my_matrix = Matrix(dimension)
        my_matrix.pad_zeros()
        my_matrix.add_edges(adj_list)
        return my_matrix

    @staticmethod
    def copy(other):
        my_matrix = Matrix(other.dimension)
        my_matrix.matrix = []
        for i in range(my_matrix.dimension):
            my_matrix.matrix.append([])
            for j in range(other.dimension):
                my_matrix.matrix[i].append(other.matrix[i][j])
        return my_matrix

    def __init__(self, dimension):
        self.matrix = None
        self.dimension = dimension

    def pad_zeros(self):
        self.matrix = []
        for i in range(self.dimension):
            self.matrix.append([])
            for j in range(self.dimension):
                self.matrix[i].append(0)

    def add_edges(self, adj_list):
        if adj_list is not None:
            for from_node, edge_list in adj_list.items():
                for to_node in edge_list:
                    self.matrix[from_node][to_node]=1







a = Matrix(4)
b = Matrix.get_from_edges(3, {0: [1,2], 1: [1,2], 2: [1,2]})
c = Matrix.copy(b)
b = 1


