
def read_input():
    array_size, max_sum = get_int_list(input())
    array1 = get_int_list(input())
    array2 = get_int_list(input())
    return max_sum, array_size, array1, array2


class Solution:
    SUCCESS, FAIL = 'YES', 'NO'

    def __init__(self):
        self.max_sum, self.size, self.array1, self.array2 = read_input()
        self.array1.sort()
        self.array2.sort()

    def calculate(self):
        for i in range(self.size):
            if (self.array1[i]+self.array2[self.size - 1 - i]) < self.max_sum:
                return self.FAIL
        return self.SUCCESS


def main():
    cases = int(input())
    for i in range(cases):
        my_object = Solution()
        print(my_object.calculate())


def get_int_list(in_str):
    return [int(i) for i in in_str.strip().split()]


if __name__ == "__main__":
    main()
