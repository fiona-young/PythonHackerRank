def read_input():
    flower_count, people_count = get_int_list(input())
    costs = get_int_list(input())
    return flower_count, people_count, costs


class Solution:
    def __init__(self):
        self.flower_count, self.people_count, self.costs = read_input()
        self.costs.sort(reverse=True)

    def calculate(self):
        paid = 0
        turn = -1
        for i, cost in enumerate(self.costs):
            if i % self.people_count == 0:
                turn += 1
            paid += (turn + 1) * cost
        return paid


def main():
    my_object = Solution()
    print(my_object.calculate())


def get_int_list(in_str):
    return [int(i) for i in in_str.strip().split()]


if __name__ == "__main__":
    main()
