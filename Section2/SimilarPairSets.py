class RangeFinder:
    def __init__(self):
        self.range_set = set()

    def add(self, node_id):
        self.range_set.add(node_id)

    def remove(self, node_id):
        self.range_set.discard(node_id)

    def range_count(self, min_val, max_val):
        count = 0
        for i in self.range_set:
            if (i>= min_val) and (i<= max_val):
                count += 1
        return count


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
        range_finder = RangeFinder()
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
