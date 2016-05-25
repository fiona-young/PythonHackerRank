class Graph:
    nodes = 64

    def __init__(self, num, connected_sets=None):
        self.dec = num
        self.bin = bin(num)
        self.connected_sets = {}
        self.index = 0
        if connected_sets is None:
            self.add_connected_set(pos_list_from_binary(num))
        else:
            for key, value in connected_sets.items():
                self.connected_sets[key] = set(value)

    def append_set(self, connected_set):
        self.connected_sets[self.index] = connected_set
        self.index += 1

    def add_connected_set(self, connected_set):
        if len(connected_set) > 1:
            self.append_set(set(connected_set))

    def count_nodes_degree_0(self):
        count = Graph.nodes
        for connected_set in self.connected_sets.values():
            count -= len(connected_set)
        return count

    def get_connected_set_count(self):
        connected_groups = len(self.connected_sets)
        connected_groups += self.count_nodes_degree_0()
        return connected_groups

    def add(self, other):
        if len(other.connected_sets) == 0:
            return
        if len(self.connected_sets) == 0:
            for key, value in other.connected_sets.items():
                self.connected_sets[key] = set(value)
            return
        else:
            for i_other, set_other in other.connected_sets.items():
                set_target = None
                for i_this, set_this in self.connected_sets.items():
                    if set_target is None:
                        set_target = i_other
                    else:
                        self.connected_sets[set_target].update(set_this)
                        del (self.connected_sets[i_this])
                    self.connected_sets[set_target].update(set_other)
                if set_target is None:
                    self.append_set(set(set_other))


class GraphList:
    def __init__(self, d: list):
        self.node_count = len(d)
        self.combinations = 2 ** self.node_count
        self.d = d
        self.my_list = []
        for num in self.d:
            self.my_list.append(Graph(num))

    def calculate(self):
        count = 0
        for combo in range(self.combinations):
            if combo == 0:
                count += Graph.nodes
            else:
                combo_list = pos_list_from_binary(combo)
                set_graph = Graph(self.my_list[combo_list[0]].dec, self.my_list[combo_list[0]].connected_sets)
                for list_id in combo_list[1:]:
                    set_graph.add(self.my_list[list_id])
                count += set_graph.get_connected_set_count()
        print(count)


def pos_list_from_binary(num):
    bin_str = '{:b}'.format(num)[-64:]
    my_list = []
    for i, my_char in enumerate(bin_str):
        if my_char == "1":
            my_list.append(len(bin_str) - 1 - i)
    return my_list


def unique_pairs(n):
    return (n * (n - 1)) // 2


def main():
    ignore = input()
    d = get_int_list(input())
    my_obj = GraphList(d)
    my_obj.calculate()


def get_int_list(in_str):
    return [int(i) for i in in_str.strip().split()]


if __name__ == "__main__":
    main()
