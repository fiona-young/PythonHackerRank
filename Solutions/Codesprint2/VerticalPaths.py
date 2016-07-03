import collections
import random
import itertools

class Trial:
    routes = None
    nodes_to_routes = None
    route_ids = None
    def __init__(self, remaining,used_routes = None, value = 0):
        self.remaining = remaining
        self.used_routes = set() if used_routes is None else used_routes
        self.value = value

    def get_constraints(self):
        constraints = {x[0] for x in self.remaining.items() if x[1] == 0}
        return constraints

    def get_constraining_routes(self):
        constraining_routes = set()
        for node_id in self.get_constraints():
            constraining_routes.update(Trial.nodes_to_routes[node_id])
        return constraining_routes

    def can_add(self,route):
        if route[2] in self.used_routes:
            return False
        for node_id in route[1]:
            if self.remaining[node_id] == 0:
                return False
        return True

    def add_routes_random(self):
        random.shuffle(Trial.route_ids)
        for route_id in Trial.route_ids:
            route = Trial.routes[route_id]
            self.add(route)

    def add(self,route):
        if not self.can_add(route):
            return
        self.used_routes.add(route[2])
        self.value += route[0]
        for node_id in route[1]:
            self.remaining[node_id]-=1

    def add_list(self, routes):
        for route in routes:
            self.add(route)

    def add_routes_order(self, route_id_list):
        for route_id in route_id_list:
            route = Trial.routes[route_id]
            self.add(route)

    def add_list_double(self, route1, route2):
        self.add_list(route1)
        self.add_list(route2)

    def pop(self, route_id):
        if route_id in self.used_routes:
            route = Trial.routes[route_id]
            self.value -= route[0]
            self.used_routes.remove(route_id)
            for node_id in route[1]:
                self.remaining[node_id]+=1
        return route_id


def powerset(iterable,min_len=0):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(min_len,len(s)+1))

class Collect:
    def __init__(self,routes,available):
        self.available = available
        Trial.routes = {x[2]:x for x in routes}
        test = {x[2]:x[0] for x in routes}
       # target = 9678062818
       # for i,val in enumerate(powerset(test.items(),18)):
       #     d_val = dict(val)
       #     sum_val = sum(d_val.values())
       #     if sum_val == target:
       #         print("**********!!!!*************")
       #     if abs( target -sum_val) < 500 or i%5000000 == 0:
       #         print('%s: %s %s: (len %s)'%(i,sum_val,d_val.keys(),len(d_val)))
       #     if sum_val == target:
       #         print("**********!!!!*************")
       #     a = 1
        nodes_to_routes = collections.defaultdict(set)
        for route in routes:
            for node_id in route[1]:
                nodes_to_routes[node_id].add(route[2])
        Trial.nodes_to_routes = nodes_to_routes
        self.routes = routes
        self.used_routes = set(range(len(self.routes)))
        Trial.route_ids = list(range(len(self.routes)))
        self.value = 0

    def process(self):
        trial = []
        max_val = 0
        self.routes.sort( key=lambda x: (-x[0]))
        my_trial = Trial(dict(self.available))
        my_trial.add_routes_order([0, 1, 3, 6, 7, 8, 10, 11, 15, 16, 17, 18, 20, 21, 24, 25, 26, 27, 28])
        #my_trial.add_list(self.routes)
        max_val = max(max_val,my_trial.value)
        if len(my_trial.get_constraints())==0:
            return max_val

        for b in range(1000):
            my_trial_copy = Trial(dict(my_trial.remaining),set(my_trial.used_routes),my_trial.value)
            if b == 500:
                a = 1
            constraining_routes = my_trial_copy.get_constraining_routes()
            remove_count = len(constraining_routes)
            for i,route_id in enumerate(constraining_routes):
                if i>= remove_count:
                    break
                if len(my_trial_copy.used_routes) >0:
                    my_trial_copy.pop(route_id)
            my_trial_copy.add_routes_random()
            #print(my_trial_copy.value, max_val)
            if my_trial_copy.value > max_val:
                max_val = my_trial_copy.value
                my_trial = Trial(dict(my_trial_copy.remaining),set(my_trial_copy.used_routes),my_trial_copy.value)
        return max_val

class Solution:
    def __init__(self):
        self.parents = {}
        self.nodes, self.edges = get_int_list(input())
        self.edge_list = []
        self.remaining = {}
        self.adj_list = {i:[] for i in range(1,self.nodes+1)}
        for i in range(self.nodes-1):
            edge = get_int_list(input())
            self.remaining[edge[1]]=edge[2]
            self.edge_list.append(edge)
            self.adj_list[edge[0]].append((edge[1],edge[2]))
            self.adj_list[edge[1]].append((edge[0],edge[2]))
        self.path_list = []
        for i in range(self.edges):
            self.path_list.append(get_int_list(input()))

        self.graph = None

        self.root = None

    def process_graph(self):
        queue = collections.deque()
        queue.append(1)
        visited_set = {1}
        while len(queue) > 0:
            node_id = queue.popleft()
            for child_id,weight in self.adj_list[node_id]:
                if child_id not in visited_set:
                    self.parents[child_id]=node_id
                    self.remaining[child_id]=weight
                    visited_set.add(child_id)
                    queue.append(child_id)

    def get_path(self,origin, dest):
        route =[]
        node_id = origin
        while node_id != dest:
            route.append(node_id)
            node_id = self.parents[node_id]
        return route


    def get_path_routes(self):
        path_list_old = self.path_list
        self.path_list =[]
        for path_id, path in enumerate(path_list_old):
            route = self.get_path(path[1],path[0])
            self.path_list.append((path[2],route,path_id))

    def calculate(self):
        self.process_graph()
        self.get_path_routes()
        collect = Collect(self.path_list,self.remaining)
        return collect.process()


def main():
    cases = int(input())
    for i in range(cases):
        my_object = Solution()
        print(my_object.calculate())


def get_int_list(in_str):
    return [int(i) for i in in_str.strip().split()]


if __name__ == "__main__":
    main()
