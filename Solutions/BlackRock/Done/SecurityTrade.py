class Portfolio:
    def __init__(self,name,order):
        self.id = name
        self.order = order
        self.proportional_allocation = None
        self.allocation = None
        self.min_trade_size = None
        self.increment = None

    def update(self, total_order, available_units,min_trade_size, increment):
        self.min_trade_size = min_trade_size
        self.increment = increment
        self.proportional_allocation = (self.order/total_order)*available_units
        if self.proportional_allocation < min_trade_size:
            if self.proportional_allocation > min_trade_size/2.:
                self.allocation = self.allocate_min_trade_size(min_trade_size)
            else:
                self.allocation = 0
        else:
            if self.proportional_allocation >= self.order:
                self.allocation = self.allocate_value(self.order)
            else:
                self.allocation = self.allocate_value(self.proportional_allocation)

    def allocate_value(self, value):
        n = int((value - self.min_trade_size)//self.increment)
        allocate = self.min_trade_size + n * self.increment
        if self.can_trade_amount(self.order - allocate):
            return allocate
        else:
            return 0

    def can_trade_amount(self,value):
        return value == 0 or ((value - self.min_trade_size)%self.increment == 0) and value >= self.min_trade_size

    def allocate_min_trade_size(self, min_trade_size):
        if self.can_trade_amount(self.order - min_trade_size):
            return min_trade_size
        else:
            return 0


class Solution:
    def __init__(self):
        self.portfolios = int(input())
        self.min_trade_size, self.increment, self.available_units = get_int_list(input())
        self.portfolio_dict = {}
        self.portfolio_sort = []
        self.total_order = 0
        for i in range(self.portfolios):
            arr = input().strip().split()
            name = arr[0]
            order = int(arr[1])
            self.portfolio_dict[name]=Portfolio(name,order)
            self.portfolio_sort.append((order,name))
            self.total_order += order
        self.portfolio_sort.sort()


    def calculate(self):
        for order,name in self.portfolio_sort:
            my_portfolio = self.portfolio_dict[name]
            my_portfolio.update(self.total_order, self.available_units, self.min_trade_size, self.increment)
            self.total_order -= my_portfolio.order
            self.available_units -= my_portfolio.allocation
        for order,name in sorted(self.portfolio_sort, key=lambda x:x[1]):
            print("%s %s"%(name,self.portfolio_dict[name].allocation))


def main():
    my_object = Solution()
    my_object.calculate()


def get_int_list(in_str):
    return [int(i) for i in in_str.strip().split()]


if __name__ == "__main__":
    main()
