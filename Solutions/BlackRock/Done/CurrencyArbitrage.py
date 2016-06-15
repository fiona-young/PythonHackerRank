import collections
Exchange = collections.namedtuple('Exchange','USD_EUR EUR_GBP GBP_USD')
def read_input():
    exchange = Exchange(*[float(i) for i in input().strip().split()])
    return exchange


class Solution:
    def __init__(self):
        self.exchange = read_input()

    def calculate(self):
        purse = 100000.
        profit = int(purse/self.exchange.USD_EUR/self.exchange.EUR_GBP/self.exchange.GBP_USD - purse)
        return max(0,profit)


def main():
    cases = int(input())
    for i in range(cases):
        my_object = Solution()
        print(my_object.calculate())


def get_int_list(in_str):
    return [int(i) for i in in_str.strip().split()]


if __name__ == "__main__":
    main()
