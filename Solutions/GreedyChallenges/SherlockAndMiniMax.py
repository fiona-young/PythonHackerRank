import math
import collections
Contender = collections.namedtuple('Contender','value diff')
def read_input():
    size = int(input())
    array = get_int_list(input())
    min_val, max_val = get_int_list(input())
    return size, array, min_val, max_val


class Solution:
    def __init__(self):
        self.size, self.array, self.min_val, self.max_val = read_input()
        self.array.sort()
        self.diff = []

    def calculate(self):
        if self.min_val < self.array[0]:
            self.diff.append(Contender(self.min_val,self.array[0]-self.min_val))
        if self.max_val > self.array[len(self.array)-1]:
            self.diff.append(Contender(self.max_val, self.max_val-self.array[len(self.array)-1]))
        for i in range(len(self.array)-1):
            x1 = self.array[i]
            x2 = self.array[i+1]
            min_diff =math.floor(abs(x1-x2)/2)
            self.diff.append(Contender(self.array[i]+min_diff, min_diff))
            if self.array[i] <self.min_val < self.array[i+1]:
                min_diff = min(abs(self.min_val-self.array[i]),abs(self.array[i+1]-self.min_val))
                self.diff.append(Contender(self.min_val, min_diff))
            if  self.array[i] < self.max_val < self.array[i+1]:
                min_diff = min(abs(self.max_val-self.array[i]),abs(self.array[i+1]-self.max_val))
                self.diff.append(Contender(self.max_val,min_diff))
        self.diff.sort(key=lambda x: (-x.diff,x.value))
        count = 0
        contender = self.diff[count]
        while self.min_val > contender.value or self.max_val < contender.value:
            count +=1
            contender = self.diff[count]
        return contender.value

def main():
    my_object = Solution()
    print(my_object.calculate())


def get_int_list(in_str):
    return [int(i) for i in in_str.strip().split()]


if __name__ == "__main__":
    main()
