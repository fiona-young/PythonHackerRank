import collections
import math


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
        self.mod_val = 1000000007
        self.fact = {}

    def create_graph(self):
        graph = []
        for i in range(self.dimension_count):
            graph_dimens = {}
            for grid in range(1, self.grid_dimensions[i] + 1):
                graph_dimens[grid] = []
                for b in [-1, 1]:
                    new_pos = grid + b
                    if 0 < new_pos <= self.grid_dimensions[i]:
                        graph_dimens[grid].append(new_pos)
            graph.append(graph_dimens)
        return graph

    def calculate(self):
        return self.grid_walk()

    def grid_walk(self):
        combined_positions = None
        for i in range(self.dimension_count):
            position = self.get_1d_paths_array(i)
            position_array =[]
            for j in range(self.steps+1):
                position_array.append(sum(position[j].values()))
            combined_positions = self.combine_positions(position_array, combined_positions)
        return combined_positions[self.steps] % self.mod_val

    def combine_positions(self, position, combined_positions):
        if combined_positions is None:
            combined_positions = position
        else:
            combined_positions_old = combined_positions
            combined_positions = [None] * (self.steps+1)
            combined_positions[0] = 1
            for path_len in range(1, self.steps + 1):
                sum = 0
                for len1 in range(0, path_len + 1):
                    sum += position[len1] * combined_positions_old[path_len - len1] * self.get_choose(path_len, len1)
                combined_positions[path_len] = sum % self.mod_val
        return combined_positions

    def get_choose(self, n, k):

        return self.get_factorial(n) // (self.get_factorial(k) * (self.get_factorial(n - k)))

    def get_factorial(self,val):
        if val not in self.fact:
            self.fact[val]=math.factorial(val)
        return self.fact[val]

    def get_1d_paths_array(self, index):
        position = []
        position.append({self.initial_position[index]: 1})
        for step in range(self.steps):
            position.append(collections.defaultdict(int))
            for origin, value in position[step].items():
                for destination in self.graph[index][origin]:
                    position[step + 1][destination] = (position[step + 1][destination] + value) % self.mod_val
        return position

def main():
    cases = int(input())
    for i in range(cases):
        my_object = Solution()
        print(my_object.calculate())


def get_int_list(in_str):
    return [int(i) for i in in_str.strip().split()]


if __name__ == "__main__":
    main()