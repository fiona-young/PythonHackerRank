import collections


class Solution:
    def __init__(self):
        self.size =  get_int_list(input())
        self.array1 = collections.deque(get_int_list(input()))
        self.array2 = collections.deque(get_int_list(input()))
        self.array3 = collections.deque(get_int_list(input()))

    def calculate(self):
        height1 = sum(self.array1)
        height2 = sum(self.array2)
        height3 = sum(self.array3)
        while height1 != height2 or height2!= height3:
            if len(self.array1)==0 or len(self.array2)==0 or len(self.array3)==0:
                return 0
            next1 = height1 - self.array1[0]
            next2 = height2 - self.array2[0]
            next3 = height3 - self.array3[0]
            if next1 >= next2 and next1 >= next3:
                self.array1.popleft()
                height1 = next1
            elif  next2 >= next1 and next2 >= next3:
                self.array2.popleft()
                height2 = next2
            else:
                self.array3.popleft()
                height3 = next3
        return height1



def main():
    my_object = Solution()
    print(my_object.calculate())


def get_int_list(in_str):
    return [int(i) for i in in_str.strip().split()]


if __name__ == "__main__":
    main()
