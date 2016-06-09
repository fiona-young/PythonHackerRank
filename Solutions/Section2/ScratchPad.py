import array
import collections


class Fenwick:
    def __init__(self, size):
        self.size = size
        self.array = array.array('l', [0] * (size + 1))
        self.bare_array = array.array('l', [0] * size)

    def update(self, key, value):
        last_value = self.bare_array[key]
        difference = value - last_value
        self.bare_array[key] = value
        tree_key = key + 1
        while tree_key < self.size + 1:
            self.array[tree_key] += difference
            tree_key += tree_key & -tree_key

    def query(self, key):
        tree_key = min(key + 1, self.size)
        sum = 0
        while tree_key > 0:
            sum += self.array[tree_key]
            tree_key -= tree_key & -tree_key
        return sum


class FenwickRangeFinder:
    def __init__(self, size):
        self.fenwick = Fenwick(size)

    def add(self, node_id):
        self.fenwick.update(node_id, 1)

    def remove(self, node_id):
        self.fenwick.update(node_id, 0)

    def range_count(self, min_val, max_val):
        count_fen = self.fenwick.query(max_val) - self.fenwick.query(min_val - 1)
        return count_fen


class BfsNode:
    def __init__(self, node_id):
        self.id = node_id
        self.parent = None
        self.distance = None
        self.visited = False

    def visit(self, parent, distance):
        self.parent = parent
        self.distance = distance
        self.visited = True


class CountPairs:
    def __init__(self, first_list:list, second_list:list):
        self.source = max(max(first_list),max(second_list))+1
        self.sink = self.source + 1
        self.node_list = first_list + second_list
        self.node_list.extend([self.source, self.sink])
        self.capacity = {x: {} for x in self.node_list}
        self.flow = {x: {} for x in self.node_list}
        self.residual = {x: set() for x in self.node_list}
        for to_node in first_list:
            self.add_edge(self.source,to_node)
        for from_node in second_list:
            self.add_edge(from_node, self.sink)
        a = 1

    def add_edge(self,from_node, to_node):
        if to_node not in self.capacity[from_node]:
            self.capacity[from_node][to_node]=1
            self.flow[from_node][to_node]=0
            self.residual[from_node].add(to_node)
            a = 1

    def bfs(self):
        node_list = {node_id:BfsNode(node_id) for node_id in self.node_list}
        my_queue = collections.deque()
        node_list[self.source].distance = 0
        node_list[self.source].visited = True
        my_queue.append(node_list[self.source])
        while len(my_queue) > 0:
            my_node = my_queue.popleft()
            for next_node_id in self.residual[my_node.id]:
                if not node_list[next_node_id].visited:
                    node_list[next_node_id].visit(my_node.id, node_list[my_node.id].distance + 1)
                    if next_node_id == self.sink:
                        my_queue.clear()
                        break
                    my_queue.append(node_list[next_node_id])
        my_node = node_list[self.sink]
        if my_node.parent is None:
            return []
        path = collections.deque()
        path.appendleft(my_node.id)
        while my_node.parent is not None:
            my_node = node_list[my_node.parent]
            path.appendleft(my_node.id)
        return list(path)

    def add_path(self, path):
        for i in range(len(path)-1):
            from_node = path[i]
            to_node = path[i + 1]
            if to_node in self.flow[from_node]:
                self.flow[from_node][to_node]=1
            else:
                self.flow[to_node][from_node]=0
            self.residual[from_node].remove(to_node)
            self.residual[to_node].add(from_node)


    def calculate_pairs(self):
        while True:
            path = self.bfs()
            if len(path) == 0:
                return sum(self.flow[self.source].values())
            self.add_path(path)
        a = 1

