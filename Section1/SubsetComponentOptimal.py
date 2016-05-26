from math import log2
class Graph:
    nodes = 64

    def __init__(self, num):
        self.dec = num
        node_set = set(pos_list_from_binary(self.dec))
        self.on_set = node_set if len(node_set) > 1 else set()
        self.graph_num = 0 if len(self.on_set) == 0 else num

class GraphList:
    def __init__(self, d: list):
        self.node_count = len(d)
        self.combinations = 2 ** self.node_count
        self.d = d
        self.my_list = []
        self.clashes = set()
        for num in self.d:
            self.my_list.append(Graph(num))
        for graph_x in self.my_list:
            for graph_y in self.my_list:
                if(graph_x.graph_num != 0) and (graph_y.graph_num != 0) and ((graph_x.graph_num | graph_y.graph_num)==(graph_x.graph_num ^ graph_y.graph_num)):
                    self.clashes.add(frozenset({graph_x.graph_num,graph_y.graph_num}))



    def calculate(self):
        if len(self.clashes) >0:
            count = self.count_with_clashes()
        else:
            count = self.count_without_clashes()
        print(count)

    def count_without_clashes(self):
        dp ={0:0}
        count = 0
        for combo in range(self.combinations):
            if combo == 0:
                count += Graph.nodes
            else:
                index = int(log2(combo))
                most_significant_bit = 2** index
                dp_index = combo - most_significant_bit
                dp_value = dp[dp_index]
                my_number = dp_value | self.my_list[index].graph_num
                dp[combo]=my_number
                count+= get_groups(pos_list_from_binary(my_number))
        return count


    def count_with_clashes(self):
        count = 0
        for combo in range(self.combinations):
            if combo == 0:
                count += Graph.nodes
            else:
                combo_list = pos_list_from_binary(combo)
                my_number = self.my_list[combo_list[0]].graph_num

                disjoint_sets_list = []
                for key in combo_list[1:]:
                    loop_graph = self.my_list[key]
                    loop_number = loop_graph.graph_num
                    if{my_number, loop_number} in self.clashes:
                        disjoint_sets_list.append(loop_graph)
                    else:
                        my_number = my_number | loop_number
                if len(disjoint_sets_list) > 0:
                    singles = get_singles(pos_list_from_binary(my_number))
                    sets = 1 if singles < Graph.nodes else 0
                    for disjoint in disjoint_sets_list:
                        sets += 1
                        singles -= len(disjoint.on_set)
                    count += singles + sets
                else:
                    count += get_groups(pos_list_from_binary(my_number))
        return count


def pos_list_from_binary(num):
    bin_str = '{:b}'.format(num)[-64:]
    my_list = []
    for i, my_char in enumerate(bin_str):
        if my_char == "1":
            my_list.append(len(bin_str) - 1 - i)
    return my_list


def get_singles(my_set):
    return Graph.nodes - len(my_set)

def get_groups(my_set):
    singles = get_singles(my_set)
    if singles == Graph.nodes:
        return Graph.nodes
    else:
        return singles + 1


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
