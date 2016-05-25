from collections import namedtuple, defaultdict

Priority = namedtuple('Priority','priority node')
class Graph:
    def __init__(self, node_count, max_feet, edge_list: list):
        self.extracted = set()
        self.adj_matrix=[[0]*node_count for i in range(node_count)]
        for node1, node2 in edge_list:
            self.adj_matrix[node1][node2] += 1
            self.adj_matrix[node2][node1] += 1
        self.node_count = node_count
        self.max_feet = max_feet


    def degree_count(self, degree_list):
        result = defaultdict(list)
        for node, degree_count in enumerate(degree_list):
            if degree_count > 0:
                result[degree_count].append(node)
        return result

    def degree_list(self):
        return [sum(a) for a in self.adj_matrix]

    def adj_dict(self):
        adj_dict = defaultdict(list)
        for node1, my_list in enumerate(self.adj_matrix):
            for node2, link in  enumerate(my_list):
                if link >= 1:
                    adj_dict[node1].append(node2)
        return adj_dict


    def calculate(self):
        while True :
            degree_list = self.degree_list()
            if sum(degree_list) == 0:
                break
            degree_count = self.degree_count(degree_list)
            if 1 in degree_count:
                self.extract_crab_degree1(self.get_next_degree1_head(degree_count, degree_list), degree_list)
            else:
                self.break_links(degree_count[min(degree_count)][0])
        print(len(self.extracted))

    def get_next_degree1_head(self, degree_count, degree_list):
        WEIGHT_MAX_FEET, WEIGHT_LINE, WEIGHT_ABOVE3, WEIGHT3 = 1, 2, 3, 4
        adj_dict = self.adj_dict()
        leaf_nodes = degree_count[1]
        head_set = {adj_dict[leaf][0] for leaf in leaf_nodes}
        priority_list = []
        for possible_head in head_set:
            degree = degree_list[possible_head]
            degree_of_ones=len([adj for adj in adj_dict[possible_head] if degree_list[adj]==1])
            if degree_of_ones >= self.max_feet or degree == degree_of_ones:
                weight = WEIGHT_MAX_FEET
                return possible_head
            elif degree <= 2:
                weight = WEIGHT_LINE
            elif degree == 3:
                weight = WEIGHT3
            else:
                weight = WEIGHT_ABOVE3
            priority_list.append(Priority(weight, possible_head))
        priority_list.sort()
        return priority_list[0].node

    def adjacent_nodes(self, head):
        return [node for node, count in enumerate(self.adj_matrix[head])if count > 0]

    def extract_crab_degree1(self,head, degree_list):
        adj_degree =[i for i in self.adjacent_nodes(head) if degree_list[i]==1][:self.max_feet]
        for foot in adj_degree:
            self.extract_single(foot)
        self.extract_single(head)

    def break_links(self, break_head):
        possible_nodes = self.adjacent_nodes(break_head)
        for break_tail in possible_nodes[1:]:
            self.adj_matrix[break_head][break_tail] = 0
            self.adj_matrix[break_tail][break_head] = 0
        a = 1

    def extract_crab_pair(self, head, degree_list):
        possible_nodes = self.adjacent_nodes(head)
        extract_node = possible_nodes[0]
        for possible_node in possible_nodes[1:]:
            if degree_list[possible_node] > degree_list[extract_node]:
                extract_node = possible_node
        self.extract_link(head, extract_node)

    def extract_link(self,head, extract_node):
        self.extract_single(head)
        self.extract_single(extract_node)

    def extract_single(self,node):
        self.extracted.add(node)
        for i in range(self.node_count):
            self.adj_matrix[i][node] = 0
        self.adj_matrix[node]=[0]*self.node_count

def main():
    cases = int(input())
    for i in range(cases):
        edge_list = []
        in_str = input()
        nodes,max_feet, edges = get_int_list(in_str)
        for j in range(edges):
            node1, node2 = get_int_list(input())
            edge_list.append([node1-1, node2-1])
        my_obj = Graph(nodes,max_feet,  edge_list)
        my_obj.calculate()


def get_int_list(in_str):
    return [int(i) for i in in_str.strip().split()]


if __name__ == "__main__":
    main()
