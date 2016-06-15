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
        #cells_list = self.get_cells()
        self.graph = {}#self.create_graph(cells_list)

    def get_cells(self,current_dimension=0, origin_string='' ):
        return_val = []
        if current_dimension == self.dimension_count:
            return [tuple(get_int_list(origin_string))]
        else:
            for i in range(1,self.grid_dimensions[current_dimension]+1):
                return_val.extend(self.get_cells(current_dimension+1,'%s %s'%(origin_string,i)))
        return return_val

    def create_graph(self, cells_list):
        graph = {}
        for grid_loc in cells_list:
            graph[grid_loc]=[]
            for i in range(self.dimension_count):
                for b in [-1, 1]:
                    new_pos = grid_loc[i]+b
                    if 0 < new_pos <= self.grid_dimensions[i]:
                        grid = list(grid_loc)
                        grid[i]=new_pos
                        graph[grid_loc].append(tuple(grid))
        return graph

    def calculate(self):
        return self.grid_walk()

    def grid_walk(self):
        mod_val = 1000000007
        position = {self.initial_position:1}
        for step in range(self.steps):
            last_position = position
            position = collections.defaultdict(int)
            for origin, value in last_position.items():
                for destination in self.get_adj_list(origin):
                    position[destination]=(position[destination]+value)%mod_val
        routes = 0
        for value in position.values():
            routes = (routes+ value)%mod_val
        return routes

    def get_adj_list(self, origin):
        if origin not in self.graph:
            self.graph[origin]=[]
            for i in range(self.dimension_count):
                for b in [-1, 1]:
                    new_pos = origin[i]+b
                    if 0 < new_pos <= self.grid_dimensions[i]:
                        grid = list(origin)
                        grid[i]=new_pos
                        dest = tuple(grid)
                        self.graph[origin].append(dest)
            a = 1
        return self.graph[origin]

def main():
    cases = int(input())
    for i in range(cases):
        my_object = Solution()
        print(my_object.calculate())


def get_int_list(in_str):
    return [int(i) for i in in_str.strip().split()]


if __name__ == "__main__":
    main()
    input_string = '''10
1 287
44
78
1 236
25
87
1 122
41
63
1 260
7
64
1 127
3
73
1 69
6
68
1 231
14
63
1 236
13
30
1 259
38
70
1 257
11
12
'''
    import sys
    import io
    sys.stdin = io.StringIO(input_string)
    import cProfile
    cProfile.run("main()")
   # main()
