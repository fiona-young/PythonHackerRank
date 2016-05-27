
class MissingNumbers:
    def __init__(self, short_list: list, full_list: list):
        self.short_list = sorted(short_list)
        self.full_list = sorted(full_list)
        self.missing_list = []

    def get_last(self):
        if len(self.missing_list)==0:
            return -5
        else:
            return self.missing_list[len(self.missing_list)-1]

    def calculate(self):
        short_index = 0
        full_index = 0
        while full_index < len(self.full_list):
            if (short_index == len(self.short_list)) or (self.short_list[short_index] != self.full_list[full_index]):
                if self.get_last()!=self.full_list[full_index]:
                    self.missing_list.append(self.full_list[full_index])
                full_index += 1
            else:
                full_index += 1
                short_index += 1
        return self.missing_list


def main():
    _ = input()
    short_list = get_int_list(input())
    _ = input()
    long_list = get_int_list(input())
    my_obj = MissingNumbers(short_list, long_list)
    print(" ".join([str(x) for x in my_obj.calculate()]))


def get_int_list(in_str):
    return [int(i) for i in in_str.strip().split()]


if __name__ == "__main__":
    main()
