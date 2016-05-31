import array

class SherlockAndArray:
    success, fail = 'YES', 'NO'
    def __init__(self, my_array :array.array):
        self.my_array = my_array

    def calculate(self):
        left = 0
        right = sum(self.my_array)
        if left == right:
            return SherlockAndArray.success
        for val in self.my_array:
            right -= val
            if left == right:
                return SherlockAndArray.success
            left += val
        return SherlockAndArray.fail



def main():
    cases = int(input())
    for _ in range(cases):
        _ = input()
        my_obj = SherlockAndArray(array.array('I',get_int_list(input())))
        print(my_obj.calculate())


def get_int_list(in_str):
    return [int(i) for i in in_str.strip().split()]


if __name__ == "__main__":
    main()
