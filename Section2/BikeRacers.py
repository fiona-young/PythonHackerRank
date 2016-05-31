import collections

Coord = collections.namedtuple('Coord', 'x y')
Edge = collections.namedtuple('Edge', 'node distance')


def read_input():
    riders, bikes, max_participants = get_int_list(input())
    rider_list, bike_list = {}, {}
    for i in range(riders):
        rider_list[i] = Coord(*get_int_list(input()))
    for i in range(bikes):
        bike_list[i + riders] = Coord(*get_int_list(input()))
    return max_participants, rider_list, bike_list


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
    def __init__(self, first_list: list, second_list: list):
        self.source = max(max(first_list), max(second_list)) + 1
        self.sink = self.source + 1
        self.node_list = first_list + second_list
        self.node_list.extend([self.source, self.sink])
        self.capacity = {x: {} for x in self.node_list}
        self.flow = {x: {} for x in self.node_list}
        self.residual = {x: set() for x in self.node_list}
        for to_node in first_list:
            self.add_edge(self.source, to_node)
        for from_node in second_list:
            self.add_edge(from_node, self.sink)

    def add_edge(self, from_node, to_node):
        if to_node not in self.capacity[from_node]:
            self.capacity[from_node][to_node] = 1
            self.flow[from_node][to_node] = 0
            self.residual[from_node].add(to_node)

    def bfs(self):
        node_list = {node_id: BfsNode(node_id) for node_id in self.node_list}
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
        for i in range(len(path) - 1):
            from_node = path[i]
            to_node = path[i + 1]
            if to_node in self.flow[from_node]:
                self.flow[from_node][to_node] = 1
            else:
                self.flow[to_node][from_node] = 0
            self.residual[from_node].remove(to_node)
            self.residual[to_node].add(from_node)

    def calculate_pairs(self):
        while True:
            path = self.bfs()
            if len(path) == 0:
                return sum(self.flow[self.source].values())
            self.add_path(path)


class BikeRacer:
    def __init__(self):
        self.max_participants, self.riders_list, self.bike_list = read_input()
        self.distances = self.calculate_distances()
        self.count_pairs = CountPairs(list(self.riders_list.keys()), list(self.bike_list.keys()))

    def calculate_distances(self):
        distances = []
        for i_rider, rider in self.riders_list.items():
            for i_bike, bike in self.bike_list.items():
                distance = (rider.x - bike.x) ** 2 + (rider.y - bike.y) ** 2
                distances.append((distance, i_rider, i_bike))
        return sorted(distances)

    def calculate(self):
        bike_d = collections.defaultdict(set)
        i_pointer = 0
        distance = 0
        while len(bike_d) < self.max_participants or self.count_pairs.calculate_pairs() < self.max_participants:
            distance, rider, bike = self.distances[i_pointer]
            self.count_pairs.add_edge(rider, bike)
            bike_d[bike].add(rider)
            i_pointer += 1
        return distance


def main():
    my_obj = BikeRacer()
    print(my_obj.calculate())


def get_int_list(in_str):
    return [int(i) for i in in_str.strip().split()]


if __name__ == "__main__":
    main()
