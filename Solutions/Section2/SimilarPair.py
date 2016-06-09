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

class RangeFinder:
    def __init__(self, size):
        self.fenwick = Fenwick(size)

    def add(self, node_id):
        self.fenwick.update( node_id, 1)

    def remove(self, node_id):
        self.fenwick.update( node_id, 0)

    def range_count(self, min_val, max_val):
        count_fen = self.fenwick.query(max_val)-self.fenwick.query(min_val-1)
        return count_fen

def read_input():
    nodes, T = get_int_list(input())
    edge_list = []
    for i_edges in range(nodes - 1):
        edge_list.append(get_int_list(input()))
    return nodes, T, edge_list



class Tree:

    def __init__(self):
        nodes, self.T, edge_list = read_input()
        self.root_id = edge_list[0][0]
        self.pointers = {i:TreeNode(i) for i in range(1,1+nodes)}
        self.root = self.pointers[self.root_id]
        for parent_id, child_id in edge_list:
            parent = self.pointers[parent_id]
            child = self.pointers[child_id]
            parent.children.append(child)
            child.parent = parent

    def calculate(self):
        return self.dfs_for_silly_non_recursive_python()

    def dfs_for_silly_non_recursive_python(self):
        process_list = [self.root]
        visited_set = set()
        range_finder = RangeFinder(100000)
        pairs = 0
        while len(process_list)>0 :
            my_node = process_list[len(process_list)-1]
            if my_node.paused:
                range_finder.remove(my_node.id)
                process_list.pop()
            else:
                visited_set.add(my_node.id)
                pairs += range_finder.range_count(my_node.id - self.T,my_node.id + self.T)
                for child in my_node.children:
                    if child.id not in visited_set:
                        process_list.append(child)
                        my_node.paused = True
                if my_node.paused:
                    range_finder.add(my_node.id)
                else:
                    process_list.pop()
        return pairs

class TreeNode:
    def __init__(self, node_id):
        self.id = node_id
        self.parent = None
        self.children = []
        self.paused = False

    def __str__(self):
        return '%s: %s'%(self.id, len(self.children))

def main():
    my_obj = Tree()
    print(my_obj.calculate())


def get_int_list(in_str):
    return [int(i) for i in in_str.strip().split()]


if __name__ == "__main__":
    main()
