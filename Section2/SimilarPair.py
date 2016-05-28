class Node:
    def __init__(self, node_id):
        self.id = node_id
        self.parent = None
        self.children = []

    def __str__(self):
        return 'id %s child_count %s' % (self.id, len(self.children))


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
        self.pointers = {i:Node(i) for i in range(1,1+nodes)}
        self.root = self.pointers[self.root_id]
        for parent_id, child_id in edge_list:
            parent = self.pointers[parent_id]
            child = self.pointers[child_id]
            parent.children.append(child)
            child.parent = parent

    def calculate(self):
        process_list = [(self.root,'')]
        pairs = 0
        while len(process_list) > 0:
            my_node, parent_str = process_list.pop()
            if parent_str != '':
                parent_list = parent_str[1:].strip().split(',')
                for i in parent_list:
                    if(abs(int(i)-my_node.id)) <= self.T:
                        pairs += 1
            for child in my_node.children:
                process_list.append((child,parent_str+','+str(my_node.id)))
        return pairs


def main():
    my_obj = Tree()
    print(my_obj.calculate())


def get_int_list(in_str):
    return [int(i) for i in in_str.strip().split()]


if __name__ == "__main__":
    main()
