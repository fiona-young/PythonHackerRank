
def read_input():
    size = int(input())
    array1 = get_int_list(input())
    array2 = get_int_list(input())
    return size, array1, array2


class BeautifulPairs:
    def __init__(self):
        self.size, self.array1, self.array2 = read_input()
        self.array1.sort()
        self.array2.sort()

    def calculate(self):
        pairs = 0
        left_over1 = 0
        left_over2 = 0
        pointer1 = 0
        pointer2 = 0
        while pointer1 < self.size and pointer2 < self.size:
            if self.array1[pointer1]==self.array2[pointer2]:
                pairs += 1
                pointer1 += 1
                pointer2 += 1
            elif self.array1[pointer1]<self.array2[pointer2]:
                left_over1 +=1
                pointer1+=1
            else:
                left_over2 +=1
                pointer2 +=1
        if pointer1 < self.size:
            left_over1 += 1
        if pointer2 < self.size:
            left_over2 += 1
        if left_over1 > 0 and left_over2 > 0:
            pairs += 1
        else:
            pairs -= 1
        return pairs

def main():
    my_object = BeautifulPairs()
    print(my_object.calculate())


def get_int_list(in_str):
    return [int(i) for i in in_str.strip().split()]


if __name__ == "__main__":
    main()
