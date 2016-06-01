def read_input():
    size, swaps = get_int_list(input())
    array = get_int_list(input())
    return size, swaps, array


class Solution:
    def __init__(self):
        self.size, self.swaps, self.array = read_input()
        self.sorted_array = [[x, i]for i, x in enumerate(self.array)]
        self.sorted_array.sort(reverse=True)
        self.sort_lookup = {x[1][0]: x[0] for x in enumerate(self.sorted_array)}

    def calculate(self):
        array_pointer = 0
        move_pointer = 0
        swaps_remaining = self.swaps
        while swaps_remaining > 0 and array_pointer < self.size and move_pointer < self.size:
            sorted_target = self.sorted_array[move_pointer]
            if sorted_target[1]==array_pointer:
                array_pointer += 1
                move_pointer += 1
                continue
            if sorted_target[1] < array_pointer:
                move_pointer += 1
                continue
            if sorted_target[0] < self.array[array_pointer]:
                array_pointer += 1
                continue
            old_index, new_index, old_value, new_value = array_pointer, sorted_target[1], self.array[array_pointer],sorted_target[0]
            self.sorted_array[self.sort_lookup[old_value]][1]= new_index
            self.sorted_array[self.sort_lookup[new_value]][1]= old_index
            self.array[old_index], self.array[new_index] = self.array[new_index], self.array[
                old_index]

            array_pointer += 1
            move_pointer += 1
            swaps_remaining -= 1
        return " ".join([str(x) for x in self.array])


def main():
    my_object = Solution()
    print(my_object.calculate())


def get_int_list(in_str):
    return [int(i) for i in in_str.strip().split()]


if __name__ == "__main__":
    main()
