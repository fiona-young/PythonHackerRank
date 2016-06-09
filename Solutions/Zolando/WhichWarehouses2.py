import collections
WarehouseCombined = collections.namedtuple('WarehouseCombined','set stock')
def read_input():
    n_warehouses,n_orders, n_products = get_int_list()
    warehouse_stock = []
    for i in range(n_warehouses):
        warehouse_stock.append(get_int_list())
    orders = []
    for i in range(n_orders):
        orders.append(get_int_list())
    return n_warehouses,n_orders,n_products,warehouse_stock,orders


class Solution:
    def __init__(self):
        self.n_warehouses, self.n_orders, self.n_products, self.warehouse_stock, self.orders = read_input()
        self.total_stock = None
        for warehouse in self.warehouse_stock:
            if self.total_stock is None:
                self.total_stock = warehouse[:]
            else:
                for i, stock in enumerate(warehouse):
                    self.total_stock[i]+=stock


    def warehouse_count(self,order):
        if not self.can_do_order(order, self.total_stock):
            return -1
        warehouse_set = set(range(self.n_warehouses))
        possible_list = [WarehouseCombined(warehouse_set,self.total_stock[:])]
        number = self.n_warehouses
        while len(possible_list) > 0:
            possible_list = self.get_can_do_order_with_one_less_warehouse(order, possible_list)
            if len(possible_list) > 0:
                number -=1
        return number

    def get_can_do_order_with_one_less_warehouse(self, order, possible_list):
        new_warehouse_set =[]
        for warehouse_set in possible_list:
            for warehouse in warehouse_set.set:
                stock = [max(0,stock-self.warehouse_stock[warehouse][i]) for i, stock in enumerate(warehouse_set.stock)]
                if self.can_do_order(order,stock):
                    new_warehouse_set.append(WarehouseCombined(warehouse_set.set.difference({warehouse}), stock))
        return new_warehouse_set

    def can_do_order(self,order,stock_list):
        for i, stock in enumerate(order):
            if stock>stock_list[i]:
                return False
        return True

    def calculate(self):
        for order in self.orders:
            print(self.warehouse_count(order))


def main():
    my_object = Solution()
    my_object.calculate()


def get_int_list():
    return [int(i) for i in input().strip().split()]


if __name__ == "__main__":
    main()
