def read_input():
    stock = dict(zip(list('ABC'), get_int_list()))
    n_orders = int(input())
    orders = []
    for i in range(n_orders):
        orders.append(set(input().strip().split(',')))
    return stock, n_orders, orders


class Solution:
    def __init__(self):
        self.stock, self.n_orders, self.orders= read_input()

    def calculate(self):
        sum_requests = {'A':0,'B':0,'C':0}
        for orders in self.orders:
            for item in orders:
                sum_requests[item]+=1
        unfufilled = 0
        for key, requested in sum_requests.items():
            unfufilled = max(unfufilled, requested-self.stock[key])

        return self.n_orders -unfufilled

def main():
    my_object = Solution()
    print(my_object.calculate())


def get_int_list():
    return [int(i) for i in input().strip().split()]


if __name__ == "__main__":
    main()
