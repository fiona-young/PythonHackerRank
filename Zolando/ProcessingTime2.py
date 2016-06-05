
def read_input():
    n_product, n_employees = get_int_list()
    employee_process_time = get_int_list()

    return n_product, n_employees, employee_process_time
class Nodes:
    def __init__(self, node_id, work_len):
        self.start_time = 0
        self.end_time = 0
        self.node_id = node_id
        self.work_len = work_len

    @property
    def projected_next_end(self):
        return self.end_time + self.work_len

    def __lt__(self, other):
        return self.projected_next_end < other.projected_next_end

class Heap:
    def __init__(self, process_time_list):
        self.heap = []
        for i, work_len in enumerate(process_time_list):
            self.add(Nodes(i,work_len))

    def add(self, item):
        index = len(self.heap)
        self.heap.append(item)
        self.bubble_up(index)

    def bubble_up(self, index):
        parent_index =self.parent(index)
        while parent_index >= 0:
            if self.heap[index]<self.heap[parent_index]:
                self.heap[index],self.heap[parent_index]=self.heap[parent_index],self.heap[index]
                index = parent_index
                parent_index = self.parent(index)
            else:
                break

    def bubble_down(self, index):
        while True:
            child_left = self.child_left(index)
            child_right = self.child_right(index)
            if child_left >= len(self.heap):
                return
            if child_right >= len(self.heap):
                min_child_index = child_left
            elif self.heap[child_right]<self.heap[child_left]:
                min_child_index = child_right
            else:
                min_child_index = child_left
            if self.heap[min_child_index] < self.heap[index]:
                self.heap[index],self.heap[min_child_index]=self.heap[min_child_index],self.heap[index]
                index = min_child_index
            else:
                return

    def pop(self):
        my_node = self.heap[0]
        self.heap[0]=self.heap[len(self.heap)-1]
        self.heap.pop()
        self.bubble_down(0)
        return my_node

    def parent(self, index):
        return (index-1)//2

    def child_left(self, index):
        return ((index+1)*2)-1

    def child_right(self, index):
        return ((index+1)*2)

    def make_products(self, products):
        length = 0
        for i in range(products):
            my_node = self.pop()
            my_node.end_time = my_node.projected_next_end
            length = max(length,my_node.end_time)
            self.add(my_node)
        return length

class Solution:
    def __init__(self):
        self.n_product, self.n_employees, self.employee_process_time = read_input()
        self.heap = Heap(self.employee_process_time)

    def calculate(self):
        return self.heap.make_products(self.n_product)

def main():
    my_object = Solution()
    print(my_object.calculate())


def get_int_list():
    return [int(i) for i in input().strip().split()]


if __name__ == "__main__":
    main()
