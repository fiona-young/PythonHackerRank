
def read_input():
    grid = []
    index = int(input())
    for i in range(index):
        grid.append(list(input().strip()))
    return index, grid


class GridChallenge:
    SUCCESS, FAIL = 'YES', 'NO'
    def __init__(self):
        self.index, self.grid = read_input()
        for grid_row in self.grid:
            grid_row.sort()

    def calculate(self):
        for irow in range(self.index-1):
            for icol in range(self.index):
                if self.grid[irow][icol]>self.grid[irow+1][icol]:
                    return GridChallenge.FAIL
        return GridChallenge.SUCCESS


def main():
    cases = int(input())
    for i in range(cases):
        my_object = GridChallenge()
        print(my_object.calculate())


def get_int_list(in_str):
    return [int(i) for i in in_str.strip().split()]


if __name__ == "__main__":
    main()
