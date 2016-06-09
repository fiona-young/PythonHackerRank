def read_input():
    size = int(input())
    array = get_int_list(input())
    return size, array


class Solution:
    def __init__(self):
        self.bonus = 4
        self.size, self.array = read_input()
        self.array.sort()

    def calculate(self):
        paid = 0
        included = -3
        for toy in self.array:
            if toy > included:
                paid += 1
                included = toy + self.bonus
        return paid


def main():
    my_object = Solution()
    print(my_object.calculate())


def get_int_list(in_str):
    return [int(i) for i in in_str.strip().split()]


if __name__ == "__main__":
    main()
