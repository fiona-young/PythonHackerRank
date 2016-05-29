import array

class Fenwick:
    def __init__(self, size):
        self.size = size
        self.array = array.array('l', [0] * (size+1))
        self.bare_array = array.array('l', [0] * size)

    def update(self, key, value):
        last_value = self.bare_array[key]
        difference = value - last_value
        self.bare_array[key] = value
        tree_key = key + 1
        while tree_key < self.size+1:
            self.array[tree_key] += difference
            tree_key += tree_key & -tree_key

    def query(self, key):
        tree_key = min(key + 1,self.size)
        sum = 0
        while tree_key > 0:
            sum += self.array[tree_key]
            tree_key -= tree_key & -tree_key
        return sum

class FenwickRangeFinder:
    def __init__(self, size):
        self.fenwick = Fenwick(size)

    def add(self, node_id):
        self.fenwick.update( node_id, 1)

    def remove(self, node_id):
        self.fenwick.update( node_id, 0)

    def range_count(self, min_val, max_val):
        count_fen = self.fenwick.query(max_val)-self.fenwick.query(min_val-1)
        return count_fen
