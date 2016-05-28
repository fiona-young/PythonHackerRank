class Pairs:
    def __init__(self, pairs_set, diff):
        self.diff = diff
        self.pairs_set = pairs_set

    def calculate(self):
        pair = 0
        for i in self.pairs_set:
            if i + self.diff in self.pairs_set:
                pair += 1
        return pair

def main():
    _, diff = get_int_list(input())
    pairs_list = {int(i) for i in input().strip().split()}
    my_obj = Pairs(pairs_list, diff)
    print(my_obj.calculate())


def get_int_list(in_str):
    return [int(i) for i in in_str.strip().split()]


if __name__ == "__main__":
    main()
