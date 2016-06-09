import collections
Query = collections.namedtuple('Query','l r')

def read_input():
    n_boxes = int(input())
    initial_position = get_int_list()
    n_queries = int(input())
    queries =[]
    for i in range(n_queries):
        queries.append(Query(*get_int_list()))
    return n_boxes, initial_position, n_queries, queries

class Box:
    def __init__(self, value, previous):
        self.previous = previous
        self.next = None
        self.value = value

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self, initial_position: list=None, from_list=True):
        if not from_list:
            return
        self.length = len(initial_position)
        self.head = None
        self.tail = None
        for position, box_id in enumerate(initial_position,1):
            my_box = Box(box_id, self.tail)
            if self.head is None:
                self.head = my_box
                self.tail = my_box
            else:
                self.tail.next = my_box
                self.tail = my_box

    def set_list(self, head, tail, length):
        self.length = length
        self.head = head
        self.tail = tail

    def get_section(self, start, end):
        section_len = end-start+1
        node_left = self.walk_right(self.head,start-1)
        node_right = self.walk_left(self.tail,self.length-end)
        if start == 1:
            self.head = node_right.next
        else:
            try:
                node_left.previous.next = node_right.next
            except AttributeError:
                a = 1
        if end == self.length:
            self.tail = node_left.previous
        else:
            node_right.next.previous = node_left.previous
        node_left.previous = None
        node_right.next = None
        self.length -= section_len
        return_list = LinkedList(from_list= False)
        return_list.set_list(node_left,node_right, section_len)
        return return_list



    def move_to_front(self, query: Query):
        if query.l == 1:
            return
        if query.l < (self.length - query.r):
            node_left =self.walk_right(self.head,query.l-1)
            node_right = self.walk_right(node_left, query.r-query.l)
        else:
            node_right = self.walk_left(self.tail, self.length - query.r)
            node_left = self.walk_left(node_right,query.r-query.l)
        if node_right.next is None:
            self.tail = node_left.previous
        else:
            node_right.next.previous = node_left.previous
        node_left.previous.next = node_right.next
        self.head.previous = node_right
        node_right.next = self.head
        node_left.previous = None
        self.head = node_left

    def walk_right(self, my_node, step):
        i = 0
        while i < step:
            my_node=my_node.next
            i+=1
        return my_node

    def walk_left(self, my_node, step):
        i = 0
        while i < step:
            my_node=my_node.previous
            i+=1
        return my_node

    def __str__(self):
        result =[]
        my_node=self.head
        while my_node is not None:
            result.append(str(my_node))
            my_node = my_node.next
        return " ".join(result)

    def join(self, list_to_add):
        self.length += list_to_add.length
        self.tail.next = list_to_add.head
        list_to_add.head.previous = self.tail
        self.tail = list_to_add.tail
        a = 1


class Shelf:
    def __init__(self,initial_position):
        self.empty_count = 0
        self.too_long = 2
        self.total_length = len(initial_position)
        self.lists = collections.deque()
        sqrt_len = max(1,int(len(initial_position)**0.5))
        self.chunk_size = max(1,len(initial_position) // sqrt_len)
        list_chunks = [initial_position[i:i+self.chunk_size] for i in range(0, len(initial_position), self.chunk_size)]
        self.chunk_number = len(list_chunks)
        for list_section in list_chunks:
            self.lists.append(LinkedList(list_section))

    def move_to_front(self, query: Query):
        end = self.total_length
        old_length = len(self.lists)
        while self.lists[-1] is None:
            self.lists.pop()
        for i in range(1,old_length+1):
            my_list = self.lists[-1*i]
            if my_list is None:
                continue
            start = end - my_list.length+1
            if end < query.l:
                break
            if start <= query.r:
                relative_end = min(my_list.length,query.r-start+1)
                if start < query.l:
                    front_section = my_list.get_section(query.l-start+1,relative_end)
                elif relative_end == my_list.length:
                    self.empty_count+=1
                    front_section = my_list
                    self.lists[-1*i]=None
                else:
                    front_section = my_list.get_section(1,relative_end)
                self.lists.appendleft(front_section)
            if start < query.l:
                break
            end = start -1
        if self.empty_count > self.chunk_number//4 or (len(self.lists)>self.chunk_number):
            self.redo_lists()

    def __str__(self):
        print_list =[]
        for my_list in self.lists:
            if my_list is None:
                continue
            print_list.append(str(my_list))
        return " ".join(print_list)

    def print_result(self):
        print(str(self))

    def redo_lists(self):
        old_lists = self.lists
        self.lists = collections.deque()
        for my_list in old_lists:
            if my_list is not None:
                self.lists.append(my_list)
        if len(self.lists) > (self.chunk_number):
            old_lists = self.lists
            self.lists = collections.deque()
            i = 0
            while i < len(old_lists):
                first_list = old_lists[i]
                i+=1
                while i < len(old_lists) and first_list.length < self.chunk_size*2:
                    first_list.join(old_lists[i])
                    i+=1
                self.lists.append(first_list)
        self.empty_count = 0



class Solution:
    def __init__(self):
        self.n_boxes, self.initial_position, self.n_queries, self.queries = read_input()
        self.locations = dict(zip(range(1,self.n_boxes+1),self.initial_position))
        self.start = 1
        self.gaps = []
        self.shelf = Shelf(self.initial_position)

    def calculate(self):
        for query in self.queries:
            self.shelf.move_to_front(query)
        self.shelf.print_result()



def main():
    my_object = Solution()
    my_object.calculate()


def get_int_list():
    return [int(i) for i in input().strip().split()]


if __name__ == "__main__":
    main()
