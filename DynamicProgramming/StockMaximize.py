def read_input():
    size = int(input())
    array = get_int_list(input())
    return size, array


class Solution:
    BUY, SELL, STICK = 1,2,3
    def __init__(self):
        self.size, self.prices = read_input()
        self.dp=[None]*self.size

    def calculate(self):
        last_max = 0
        for i in range(0,self.size):
            i_key=self.size-i-1
            price = self.prices[i_key]
            diff =price-self.prices[i_key-1]
            if i_key != 0 and diff > 0 and price > last_max :
                last_max = price
                self.dp[i_key]=self.SELL
            elif price < last_max:
                self.dp[i_key]=self.BUY
            else:
                self.dp[i_key]=self.STICK
        shares = 0
        profit = 0
        for i, action in enumerate(self.dp):
            if action == self.BUY:
                shares += 1
                profit -= self.prices[i]
            elif action == self.SELL:
                profit += self.prices[i]*shares
                shares = 0
        return profit




def main():
    cases = int(input())
    for i in range(cases):
        my_object = Solution()
        print(my_object.calculate())


def get_int_list(in_str):
    return [int(i) for i in in_str.strip().split()]


if __name__ == "__main__":
    main()
