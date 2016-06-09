import array

class IceCreamParlor:
    def __init__(self, money, cost_array :array.array):
        self.cost_array = [(val, i) for i, val in enumerate(cost_array,1)]
        self.cost_array.sort()

        self.money = money

    def calculate(self):
        i_left = 0
        i_right = len(self.cost_array)-1
        while i_left != i_right:
            my_sum =  self.cost_array[i_left][0]+ self.cost_array[i_right][0]
            if my_sum == self.money:
                return sorted([self.cost_array[i_left][1],self.cost_array[i_right][1]])
            elif my_sum > self.money:
                i_right -=1
            else:
                i_left += 1
        return (0,0)



def main():
    cases = int(input())
    for _ in range(cases):
        money = int(input())
        _ = input()
        my_obj = IceCreamParlor(money, array.array('I',get_int_list(input())))
        result = my_obj.calculate()
        print(str(result[0])+' '+str(result[1]))


def get_int_list(in_str):
    return [int(i) for i in in_str.strip().split()]


if __name__ == "__main__":
    main()
