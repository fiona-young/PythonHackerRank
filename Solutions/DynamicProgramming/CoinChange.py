
def read_input():
    number, types = get_int_list(input())
    coins = get_int_list(input())
    return number, types, coins


class Solution:
    def __init__(self):
        self.number, self.types, self.coins = read_input()
        self.coins.sort()
        self.min_coin = self.coins[0]

    def calculate(self):
        dp=[[None]*(self.number+1) for i in range((self.types+1))]
        for i in range(1, self.number+1):
            self.calculate_dp(dp, i)
        my_sum = 0
        for i in range( self.types):
            my_sum += dp[i][self.number]
        return my_sum

    def calculate_dp(self, dp: list, value):
        for i in range(self.types):
            dp[i][value]=0
            if value == self.coins[i]:
                dp[i][value]=1
            if (value - self.coins[i]) > 0:
                my_sum = 0
                for x in range(i, self.types):
                    my_sum += dp[x][value-self.coins[i]]
                dp[i][value]+=my_sum


def main():
    my_object = Solution()
    print(my_object.calculate())


def get_int_list(in_str):
    return [int(i) for i in in_str.strip().split()]


if __name__ == "__main__":
    main()
