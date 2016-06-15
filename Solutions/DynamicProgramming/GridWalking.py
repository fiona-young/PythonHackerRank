import collections
def read_input():
    dimension_count, steps = get_int_list(input())
    initial_position = get_int_list(input())
    grid_dimensions = get_int_list(input())
    return dimension_count, steps, initial_position, grid_dimensions


class Solution:
    def __init__(self):
        self.dimension_count, self.steps, self.initial_position, grid_dimensions = read_input()
        self.initial_position = tuple(self.initial_position)
        self.grid_dimensions = grid_dimensions
        self.graph = self.create_graph()

    def get_cells(self,current_dimension=0, origin_string='' ):
        return_val = []
        if current_dimension == self.dimension_count:
            return [tuple(get_int_list(origin_string))]
        else:
            for i in range(1,self.grid_dimensions[current_dimension]+1):
                return_val.extend(self.get_cells(current_dimension+1,'%s %s'%(origin_string,i)))
        return return_val

    def create_graph(self):
        graph = []
        for i in range(self.dimension_count):
            graph_dimens = {}
            for grid in range(1, self.grid_dimensions[i]+1):
                graph_dimens[grid]=[]
                for b in [-1, 1]:
                    new_pos = grid+b
                    if 0 < new_pos <= self.grid_dimensions[i]:
                        graph_dimens[grid].append(new_pos)
            graph.append(graph_dimens)
        return graph

    def calculate(self):
        return self.grid_walk()

    def grid_walk(self):
        mod_val = 1000000007
        position = []
        for i in range(self.dimension_count):
            position.append({self.initial_position[i]:1})

        for step in range(self.steps):
            last_position = position
            position = []
            for i in range(self.dimension_count):
                position.append(collections.defaultdict(int))
                for origin, value in last_position[i].items():
                    if self.dimension_count > 1:
                        position[i][origin]=last_position[i][origin]
                    for destination in self.graph[i][origin]:
                        position[i][destination]=(position[i][destination]+value)%mod_val
        routes = 0
        for per_dimension in position:
            for value in per_dimension.values():
                routes = (routes+ value)%mod_val
        return routes

    def lazy_load(self, origin):
        self.graph[origin]=[]
        for i in range(self.dimension_count):
            for b in [-1, 1]:
                new_pos = origin[i]+b
                if 0 < new_pos <= self.grid_dimensions[i]:
                    grid = list(origin)
                    grid[i]=new_pos
                    dest = tuple(grid)
                    self.graph[origin].append(dest)

    def get_adj_list(self, origin):
        if origin not in self.graph:
            self.lazy_load(origin)
        return self.graph[origin]

def main():
    cases = int(input())
    for i in range(cases):
        my_object = Solution()
        print(my_object.calculate())


def get_int_list(in_str):
    return [int(i) for i in in_str.strip().split()]


if __name__ == "__main__":
   # main()
    input_string = '''1
10 7
20 58 12 14 5 5 48 18 39 11
22 86 55 63 42 53 63 100 55 16
'''

    import sys
    import io
    sys.stdin = io.StringIO(input_string)
    import cProfile
    cProfile.run("main()")
   # main()
