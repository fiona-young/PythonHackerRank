def read_input():
    _, _ = get_int_list(input())
    y_array = get_int_list(input())
    x_array = get_int_list(input())
    return x_array, y_array


class Solution:
    X, Y = 'X', 'Y'
    def __init__(self):
        self.y_array, self.x_array = read_input()
        self.array = [(y, self.Y) for y in self.y_array]
        self.array.extend([(x, self.X) for x in self.x_array])
        self.array.sort(reverse=True)

    def calculate(self):
        paid = 0
        strips={self.X:1, self.Y:1}
        for cost, direction in self.array:
            paid += cost*strips[direction]
            strips[self.other(direction)] +=1
        return paid

    def other(self, direction):
        if direction == self.X:
            return self.Y
        else:
            return self.X

def main():
    cases = int(input())
    for i in range(cases):
        my_object = Solution()
        print(my_object.calculate()%1000000007)


def get_int_list(in_str):
    return [int(i) for i in in_str.strip().split()]


if __name__ == "__main__":
    main()