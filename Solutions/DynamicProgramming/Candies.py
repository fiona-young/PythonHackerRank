def read_input():
    size = int(input())
    array = []
    for i in range(size):
        array.append(int(input()))
    return size, array

class Solution:
    def __init__(self):
        self.size, self.array = read_input()

    def calculate(self):
        if self.size == 1:
            return 1
        i = 1
        sweets =[]
        last_i_set = 0
        last_diff = direction(self.array[i-1],self.array[i])
        while i < self.size:
            this_diff =  direction(self.array[i-1],self.array[i])
            if this_diff != last_diff:
                sweets = self.change_direction(last_diff, last_i_set,i-1,sweets)
                last_i_set = i-1
            i+=1
            last_diff = this_diff
        sweets = self.change_direction(last_diff, last_i_set,self.size-1,sweets)
        return sum(sweets)

    def change_direction(self, last_diff, first_i, last_i, sweets:list):
        length = last_i-first_i+1
        if last_diff == 1:
            sweet_list =[length-x for x in range(length)]
        elif last_diff ==0:
            sweet_list=[1]*length
        else:
            sweet_list=[x+1 for x in range(length)]
        if len(sweets)==0:
            sweets=sweet_list
        else:
            sweets[len(sweets)-1]=max( sweets[len(sweets)-1], sweet_list[0])
            sweets.extend(sweet_list[1:])
        a = 1
        return sweets

def direction(val1, val2):
    diff = (val1-val2)
    if diff == 0:
        return diff
    return int(diff/abs(diff))

def main():
    my_object = Solution()
    print(my_object.calculate())


def get_int_list(in_str):
    return [int(i) for i in in_str.strip().split()]


if __name__ == "__main__":
    main()
