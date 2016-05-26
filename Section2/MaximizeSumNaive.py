import array

class MaximizeSum:
    def __init__(self):
        _, self.mod = get_int_list(input())
        str_input = input()
        self.values = []
        self.running_max = 0
        for val in str_input.strip().split():
            val_int = int(val)%self.mod
            self.running_max = max(self.running_max, val_int)
            self.values.append(val_int)

    def calculate(self):
        old_list = self.values
        i_val = 1
        while len(old_list)>1:
            new_list = []
            for i in range(len(old_list)-1):
                val = (old_list[i]+self.values[i+i_val])%self.mod
                if val > self.running_max:
                    self.running_max = val
                new_list.append(val)
            old_list = new_list
            i_val += 1
        return self.running_max



def main():
    cases = int(input())
    for _ in range(cases):
        my_obj = MaximizeSum()
        print(my_obj.calculate())


def get_int_list(in_str):
    return [int(i) for i in in_str.strip().split()]


if __name__ == "__main__":
    main()
