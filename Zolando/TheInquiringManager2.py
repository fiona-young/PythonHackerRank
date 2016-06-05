import collections
Order = collections.namedtuple('Order', 'time price')

def read_input():
    events = int(input())
    orders = []
    managers = []
    for i in range(events):
        query = get_int_list(input())
        if len(query)==2:
            managers.append(query[1])
            orders.append(Order(query[1],None))
        else:
            orders.append(Order(query[2],query[1]))
    return orders, managers


class Solution:
    def __init__(self):
        self.orders, self.managers = read_input()
        self.orders.sort(key=lambda x: x.time)
        self.lookup = {}
        for i, order in enumerate(self.orders):
            self.lookup[order.time]=i
        a = 1
    def add_to_cost(self,cost, price):
        if price is not None:
            if cost is None:
                cost = price
            else:
                cost =max(cost,price)
        return cost

    def made_in_range(self, time_start, time_end):
        index = self.lookup[time_end]
        i = index
        cost = None
        while i < len(self.orders) and  self.orders[i].time <= time_end:
            cost = self.add_to_cost(cost, self.orders[i].price)
            i+=1
        i = index-1
        while i >= 0 and  self.orders[i].time >= time_start:
            cost = self.add_to_cost(cost, self.orders[i].price)
            i-=1
        if cost is None:
            cost = -1
        return cost

    def calculate(self):
        for time_end in self.managers:
            time_start = max(0, time_end-59)
            print(self.made_in_range(time_start,time_end))

def main():
    my_object = Solution()
    my_object.calculate()


def get_int_list(in_str):
    return [int(i) for i in in_str.strip().split()]


if __name__ == "__main__":
    main()
