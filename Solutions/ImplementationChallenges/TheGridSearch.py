import collections

Grid = collections.namedtuple('Grid', 'rows cols data')


def read_input():
    rows, cols = get_int_list(input())
    haystack = Grid(rows, cols, [])
    for i in range(rows):
        haystack.data.append([int(i) for i in list(input().strip())])
    rows, cols = get_int_list(input())
    needle = Grid(rows, cols, [])
    for i in range(rows):
        needle.data.append([int(i) for i in list(input().strip())])
    return (haystack, needle)


class TheGridSearch:
    def __init__(self):
        self.haystack, self.needle = read_input()

    def calculate(self):
        return self.coarse()

    def fine_check(self, row_offset, col_offset):
        for irow in range(0, self.needle.rows):
            for icol in range(0, self.needle.cols):
                if self.haystack.data[irow + row_offset][icol + col_offset] != self.needle.data[irow][icol]:
                    return False
        return True

    def coarse(self):
        top_corner = self.needle.data[0][0]
        for irow in range(0, self.haystack.rows - self.needle.rows + 1):
            for icol in range(0, self.haystack.cols - self.needle.cols + 1):
                if self.haystack.data[irow][icol] == top_corner:
                    if self.fine_check(irow, icol):
                        return 'YES'
        return 'NO'


def main():
    cases = int(input())
    for i in range(cases):
        my_object = TheGridSearch()
        print(my_object.calculate())


def get_int_list(in_str):
    return [int(i) for i in in_str.strip().split()]


if __name__ == "__main__":
    main()
