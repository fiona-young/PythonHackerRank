
def read_input():
    size = int(input())
    array1 = get_int_list()
    array2 = get_int_list()
    return size, array1, array2


class Solution:
    def __init__(self):
        self.size, self.array1, self.array2 = read_input()

    def calculate(self):
        return 3


def main():
    my_object = Solution()
    print(my_object.calculate())


def get_int_list():
    return [int(i) for i in input().strip().split()]


if __name__ == "__main__":
    main()
