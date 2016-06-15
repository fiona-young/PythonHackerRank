


class Solution:
    def __init__(self):
        self.size = int(input())
        self.array1 = get_int_list(input())
        self.array2 = get_int_list(input())

    def calculate(self):
        return 3


def main():
    my_object = Solution()
    print(my_object.calculate())


def get_int_list(in_str):
    return [int(i) for i in in_str.strip().split()]


if __name__ == "__main__":
    main()
