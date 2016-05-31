class MaximizeSum:
    def __init__(self):
        _, self.mod = get_int_list(input())
        str_input = input()
        self.values = []
        self.cum_sums = []
        self.running_max = 0
        for i,val in enumerate(str_input.strip().split()):
            val_int = int(val)%self.mod
            self.values.append(val_int)

    def calculate(self):
        cum_sums = []
        cum_val = 0
        for i, val in enumerate(self.values):
            cum_val = (cum_val + val)%self.mod
            cum_sums.append((cum_val,i))
        cum_sums.sort()
        min_val = self.mod
        for i in range(len(cum_sums) -1):
            value_this, index_this = cum_sums[i]
            value_next, index_next = cum_sums[i+1]
            if index_this > index_next:
                this_min = value_next - value_this
                min_val = min(this_min, min_val)
        result = max(cum_sums[len(cum_sums)-1][0],self.mod - min_val)
        return result



def main():
    cases = int(input())
    for _ in range(cases):
        my_obj = MaximizeSum()
        print(my_obj.calculate())


def get_int_list(in_str):
    return [int(i) for i in in_str.strip().split()]


if __name__ == "__main__":
    main()
