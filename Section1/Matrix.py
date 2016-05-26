
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

class Matrix:
    @staticmethod
    def get_from_edges(dimension, adj_list):
        my_matrix = Matrix.get_zeros(dimension)
        my_matrix._add_edges(adj_list)
        return my_matrix

    @staticmethod
    def get_zeros(dimension):
        my_matrix = Matrix(dimension)
        my_matrix.pad_zeros()
        return my_matrix

    def copy(self):
        my_matrix = Matrix(self.dimension)
        my_matrix.matrix = []
        for i in range(self.dimension):
            my_matrix.matrix.append([])
            for j in range(self.dimension):
                my_matrix.matrix[i].append(self.matrix[i][j])
        return my_matrix

    def __init__(self, dimension):
        self.matrix = None
        self.dimension = dimension

    def __str__(self):
        my_str = ''
        for row in self.matrix:
            my_str += str(row)+"\n"
        return my_str

    def pad_zeros(self):
        self.matrix = []
        for i in range(self.dimension):
            self.matrix.append([])
            for j in range(self.dimension):
                self.matrix[i].append(0)

    def _add_edges(self, adj_list):
        if adj_list is not None:
            for from_node, edge_list in adj_list.items():
                for to_node in edge_list:
                    self.matrix[from_node][to_node]=1

    def pow(self, pow_val, mod_val = None):
        started = False
        target = pow_val
        current_pow = 1
        current_val = 0
        while pow_val > 0:
            if current_pow == 1:
                current_pow_matrix = self.copy()
            else:
                current_pow_matrix = current_pow_matrix.mat_square_mult(current_pow_matrix, mod_val)
            if pow_val % (2 * current_pow):
                current_val += current_pow
                if started:
                    result = result.mat_square_mult(current_pow_matrix, mod_val)
                else:
                    result = current_pow_matrix.copy()
                    started = True
                #print(current_pow, current_val, target)
                pow_val -= current_pow
            current_pow *= 2
        return result

    def mat_square_mult(self, other, mod_val = None):
        result = Matrix.get_zeros(self.dimension)
        for i in range(self.dimension):
            for j in range(self.dimension):
                val = 0
                for k in range(self.dimension):
                    val += self.matrix[i][k]*other.matrix[k][j]
                if mod_val is not None:
                    val %= mod_val
                result.matrix[i][j]=val

        return result
