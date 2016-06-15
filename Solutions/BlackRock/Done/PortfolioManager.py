import collections

class Node:
    def __init__(self,node_id,value, parent,depth):
        self.id = node_id
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None
        self.depth = depth
        self.child_max = 0
        self.my_max = 0
        self.leaf = True

    def __str__(self):
        return '%s max %s child max %s'%(self.value, self.my_max, self.child_max)

    def set_max_not_related(self):
        self.my_max =  max(self.children_max(),self.value + self.children_children_max())
        self.child_max = self.children_max()

    def get_max_not_related(self):
        return max(self.my_max, self.child_max)

    def children_max(self):
        my_max = 0
        if self.left is not None:
            my_max += self.left.my_max
        if self.right is not None:
            my_max += self.right.my_max
        return my_max

    def children_children_max(self):
        child_max = 0
        if self.left is not None:
            child_max += self.left.child_max
        if self.right is not None:
            child_max += self.right.child_max
        return child_max

    def walk_str(self):
        str_val = ''
        if self.left is not None:
            str_val = self.left.walk_str()
        str_val += ' %s'%str(self.value)
        if self.right is not None:
            str_val += self.right.walk_str()
        return str_val

    def get_parent_id(self):
        if self.parent is None:
            return None
        else:
            return self.parent.id

    def children_value(self):
        value = 0
        if self.left is not None:
            value += self.left.value
        if self.right is not None:
            value += self.right.value
        return value if value >self.value else 0

    def get_child_id(self):
        if self.left is not None:
            return self.left.id
        if self.right is not None:
            return self.right.id
        return 0

    def not_related(self,id_set:set):
        return len(id_set.intersection(self.get_related_set()))==0

    def get_related_set(self):
        return_set = set()
        if self.parent is not None:
            return_set.add(self.parent.id)
        if self.left is not None:
            return_set.add(self.left.id)
        if self.right is not None:
            return_set.add(self.right.id)
        return return_set

class Tree:
    def __init__(self,size, tree_list: collections.deque):
        self.node_id=1
        build_list = collections.deque()
        self.root = Node(self.node_id,int(tree_list.popleft()), None,0)
        build_list.append(self.root)
        self.node_id+=1
        self.node_dict={1:self.root}
        while len(build_list) > 0 and len(tree_list)>0:# and node_id <= size:
            for i in range(len(build_list)):
                my_node = build_list.popleft()
                for is_left in [True, False]:
                    if len(tree_list)==0:
                        continue
                    else:
                        self.add_node(my_node, tree_list.popleft(),build_list,is_left)
        depth_list=self.get_depth_list()
        for depth, node in depth_list :
            node.set_max_not_related()

    def add_node(self,my_node,value,build_list,left = True):
        try:
            value=int(value)
        except ValueError:
            return
        if value != '#':
            child_node = Node(self.node_id,int(value),my_node,my_node.depth+1)
            self.node_dict[self.node_id]=child_node
            self.node_id+=1
            if left :
                my_node.left = child_node
            else:
                my_node.right= child_node
            my_node.leaf = False
            build_list.append(child_node)

    def get_depth_list(self):
        val = []
        for node in self.node_dict.values():
            val.append((node.depth, node))
        val.sort(reverse=True, key=lambda x: x[0])
        return val

    def get_max_not_related(self):
        return self.root.get_max_not_related()


class Solution:
    def __init__(self):
        self.size = int(input())
        self.build_tree = None
        if self.size>0:
            self.tree_list = collections.deque(input().strip().split())
            self.build_tree = Tree(self.size,self.tree_list)


    def calculate(self):
        if self.size == 0:
            return 0
        return self.build_tree.get_max_not_related()

    def get_individual_value(self, data_list,added_set):

        total_value = 0
        for value, id, node in data_list:
            if node.not_related(added_set):
                total_value += value
                added_set.add(id)
        return total_value

def main():
    my_object = Solution()
    print(my_object.calculate())


def get_int_list(in_str):
    return [int(i) for i in in_str.strip().split()]


if __name__ == "__main__":
    main()
