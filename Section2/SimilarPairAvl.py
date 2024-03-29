class BinaryNode:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.right = None
        self.left = None
        self.tree_size = 0
        self.height = 0

    def update(self):
        my_node = self
        while True:
            if abs(my_node.height_left - my_node.height_right) > 1:
                my_node.rotate()
            my_node.update_single()
            if my_node.parent is None:
                break
            my_node = my_node.parent
        return my_node

    def update_single(self):
        self.tree_size = self.tree_size_left + self.tree_size_right + 1
        self.height = max(self.height_right, self.height_left) + 1

    def rotate(self):
        while abs(self.height_left - self.height_right) > 1:
            if self.height_left > (1 + self.height_right):
                if self.left.height_left >= self.left.height_right:
                    self.rotate_right()
                else:
                    self.left.rotate_left()
                    self.rotate_right()
            elif self.height_right > (1 + self.height_left):
                if self.right.height_right >= self.right.height_left:
                    self.rotate_left()
                else:
                    self.right.rotate_right()
                    self.rotate_left()

    def rotate_right(self):
        parent = self.parent
        y = self
        x = self.left
        b = x.right
        if parent is not None:
            if y is parent.right:
                parent.right = x
            elif y is parent.left: #stop null error
                parent.left = x
        y.left = b
        if b is not None:
            b.parent = y
        x.parent = parent
        x.right = y
        y.parent = x
        x.update_single()
        y.update_single()


    def rotate_left(self):
        parent = self.parent
        x = self
        y = self.right
        b = y.left
        if parent is not None:
            if x is parent.right:
                parent.right = y
            elif x is parent.left: #stop null error
                parent.left = y
        x.right = b
        if b is not None:
            b.parent = x
        y.parent = parent
        x.parent = y
        y.left = x
        x.update_single()
        y.update_single()



    def walk(self, result=None):
        if result is None:
            result = []
        if self.left is not None:
            self.left.walk(result)
        result.append(self.value)
        if self.right is not None:
            self.right.walk(result)
        return result

    def get_max_node(self):
        my_node = self
        while my_node.right is not None:
            my_node = my_node.right
        return my_node

    def delete(self, value):
        delete_node = self.find_node(value, True)
        update_node = None
        if delete_node is None:
            return self
        if delete_node.left is None and delete_node.right is None:
            if delete_node.parent is None:
                return None
            if delete_node is delete_node.parent.right:
                delete_node.parent.right = None
            else:
                delete_node.parent.left = None
            return delete_node.parent.update()
        if delete_node.left is None:
            promoted_node = delete_node.right
        elif delete_node.right is None:
            promoted_node = delete_node.left
        else:
            promoted_node = delete_node.left.get_max_node()
            if promoted_node.parent is not delete_node:
                if promoted_node.left is not None:
                    promoted_node.left.parent = promoted_node.parent
                update_node = promoted_node.parent
                promoted_node.parent.right = promoted_node.left
                promoted_node.left = None
        delete_node.swap_nodes(promoted_node)
        if update_node is None:
            return promoted_node.update()
        else:
            return update_node.update()

    def swap_nodes(self, target):
        if self.parent is not None:
            if self is self.parent.right:
                self.parent.right = target
            else:
                self.parent.left = target
        target.parent = self.parent
        if self.right is not None and self.right is not target:
            self.right.parent = target
            target.right = self.right
        if self.left is not None and self.left is not target:
            self.left.parent = target
            target.left = self.left

    def find_node(self, search_val, exact=True):
        this_node = self
        while True:
            if search_val < this_node.value:
                if this_node.left is None:
                    return None if exact else this_node
                this_node = this_node.left
            elif search_val > this_node.value:
                if this_node.right is None:
                    return None if exact else this_node
                this_node = this_node.right
            else:
                return this_node

    @property
    def tree_size_left(self):
        return 0 if self.left is None else self.left.tree_size

    @property
    def tree_size_right(self):
        return 0 if self.right is None else self.right.tree_size

    @property
    def height_left(self):
        return -1 if self.left is None else self.left.height

    @property
    def height_right(self):
        return -1 if self.right is None else self.right.height

    def add(self, my_node):
        this_node = self
        while True:
            if my_node < this_node:
                if this_node.left is None:
                    this_node.left = my_node
                    my_node.parent = this_node
                    return my_node.update()
                else:
                    this_node = this_node.left
            else:
                if this_node.right is None:
                    this_node.right = my_node
                    my_node.parent = this_node
                    return my_node.update()
                else:
                    this_node = this_node.right

    def get_rank(self, search_val, include_exact=False):
        this_node = self
        rank = 0
        while this_node is not None:
            if search_val < this_node.value:
                this_node = this_node.left
            elif search_val > this_node.value:
                rank += 1 + this_node.tree_size_left
                this_node = this_node.right
            else:
                rank += this_node.tree_size_left
                if include_exact:
                    rank += 1
                break
        return rank

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

    def __str__(self):
        return str(self.value)


class RangeFinder:
    def __init__(self):
        self.root_node = None

    def add(self, node_id):
        my_node = BinaryNode(node_id)
        if self.root_node is None:
            self.root_node = my_node
            self.root_node.update()
        else:
            self.root_node = self.root_node.add(my_node)

    def remove(self, node_id):
        if self.root_node is None:
            return
        else:
            self.root_node = self.root_node.delete(node_id)

    def range_count(self, min_val, max_val):
        if self.root_node is None:
            count = 0
        else:
            min_rank = self.root_node.get_rank(min_val, False)
            max_rank = self.root_node.get_rank(max_val, True)
            count = max_rank - min_rank
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
