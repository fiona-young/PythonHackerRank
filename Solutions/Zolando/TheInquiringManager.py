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

class QueryList:
    duration = 59
    def __init__(self):
        self.data = collections.deque()
        self.time = 0
        self.max = None

    def append(self, order: Order):
        self.data.append(order)
        if self.max is None or order.price> self.max.price:
            self.max = order
        self.update_duration(order.time)
    def get_max(self, time):
        self.update_duration(time)
        if len(self.data)==0:
            return -1
        return self.max.price

    def update_duration(self, time):
        if self.time != time and time-self.duration > 0:
            self.time = time
            if len(self.data) == 0:
                self.max = None
            else:
                start = time - self.duration
                while len(self.data) > 0 and self.data[0].time < start:
                    self.data.popleft()
                if self.max.time < start:
                    self.update_max_time()

    def update_max_time(self):
        self.max = None
        for query in self.data:
            if self.max is None or query.price >= self.max.price:
                self.max = query

class Solution:
    def calculate(self):
        query_list = QueryList()
        events = int(input())
        for i in range(events):
            query = get_int_list(input())
            if len(query)==2:
                print(query_list.get_max(query[1]))
            else:
                query_list.append(Order(query[2],query[1]))
def main():
    my_object = Solution()
    my_object.calculate()


def get_int_list(in_str):
    return [int(i) for i in in_str.strip().split()]


if __name__ == "__main__":
    main()
