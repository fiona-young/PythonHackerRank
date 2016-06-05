import collections
WarehouseCombined = collections.namedtuple('WarehouseCombined','set stock')
def read_input():
    n_warehouses,n_orders, n_products = get_int_list()
    warehouse_stock = []
    for i in range(n_warehouses):
        if n_products > 0:
            warehouse_stock.append(get_int_list())
        else:
            warehouse_stock.append([])
    orders = []
    for i in range(n_orders):
        if n_products > 0:
            orders.append(get_int_list())
        else:
            orders.append([])
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

    def hopeful_warehouse_count(self,order):
        order_dict = {i:count for i,count in enumerate(order) if count > 0}
        order_set = set(order_dict)
        optimised_warehouse = []
        for warehouse in self.warehouse_stock:
            warehouse_dict = {i:count for i,count in enumerate(warehouse) if count > 0}
            if len(order_set.intersection(set(warehouse_dict))) > 0 :
                weight = self.get_weight_from_order(order, warehouse_dict)
                optimised_warehouse.append((weight, warehouse_dict))
        order_remaining = order.copy()
        warehouses_used = 0
        while len(optimised_warehouse) >0:
            warehouses_used += 1
            optimised_warehouse.sort(key=lambda x:x[0], reverse= True)
            for i,count in optimised_warehouse[0][1].items():
                order_remaining[i]=max(0, order_remaining[i]-count)
            if sum(order_remaining) == 0:
                return warehouses_used
            order_remaining_set = {i for i,count in enumerate(order_remaining) if count > 0}
            old_optimised_warehouse = optimised_warehouse[1:]
            optimised_warehouse = []
            for _, warehouse_dict in old_optimised_warehouse:
                if len(order_remaining_set.intersection(set(warehouse_dict))) > 0 :
                    weight = self.get_weight_from_order(order_remaining, warehouse_dict)
                    optimised_warehouse.append((weight, warehouse_dict))
        return -1


    def get_weight_from_order(self, order_remaining, warehouse_dict):
        weight = 0
        for i, count in warehouse_dict.items():
            if order_remaining[i]>0:
                weight_item = count/order_remaining[i]
                weight += weight_item
        return weight

    def calculate(self):
        for order in self.orders:
            print(self.hopeful_warehouse_count(order))


def main():
    my_object = Solution()
    my_object.calculate()


def get_int_list():
    return [int(i) for i in input().strip().split()]


if __name__ == "__main__":
    main()
