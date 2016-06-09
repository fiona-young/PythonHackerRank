
def read_input():
    size = int(input())
    array = get_int_list(input())
    return size, array


class Solution:
    def __init__(self):
        self.size, self.array = read_input()
        self.dp_ending_here = None
        self.dp = None

    def calculate(self):
        max_sum=None
        max_neg = None
        for val in self.array:
            if val >= 0:
                max_sum = val if max_sum is None else max_sum+val
            else:
                max_neg = val if max_neg is None else max(max_neg, val)
            self.add_dp(val)
        if max_sum is None:
            max_sum = max_neg
        return "%s %s"%(self.dp, max_sum)

    def add_dp(self , val):
        if self.dp_ending_here is None:
            self.dp_ending_here = val
        else:
            self.dp_ending_here = max(val, val+self.dp_ending_here)
        if self.dp is None:
            self.dp = val
        else:
            self.dp = max(self.dp, self.dp_ending_here)



def main():
    cases = int(input())
    for i in range(cases):
        my_object = Solution()
        print(my_object.calculate())


def get_int_list(in_str):
    return [int(i) for i in in_str.strip().split()]


if __name__ == "__main__":
    main()
