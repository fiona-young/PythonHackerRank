from enum import Enum
from collections import namedtuple

Edge = namedtuple('Edge', 'dest char')


class Alphabet(Enum):
    a = 'a'
    b = 'b'
    e = None


def empty_edge(dest):
    return Edge(dest, Alphabet.e)


class CountStrings:
    def __init__(self, regex_string):
        RegexGraphNFA.node_count = 0
        self.regex_string = regex_string
        nfa_graph = self.translate_regex()
        translate_graph = TranslateGraph(nfa_graph)
        self.dfa_graph = translate_graph.translate()
        # self.dfa_graph = nfa_graph.collapse()

    def calculate(self, string_length):
        return self.dfa_graph.count_paths(string_length)

    def translate_regex(self, index=0):
        result_set = ResultSet()
        while index < len(self.regex_string):
            if self.regex_string[index] == '(':
                out_list, index = self.translate_regex(index + 1)
                result_set.insert(out_list)
            elif self.regex_string[index] == ')':
                result = result_set.calculate_result()
                return result, index
            elif self.regex_string[index] == '|':
                result_set.set_or()
            else:
                result_set.insert(self.regex_string[index])
            index += 1
        return result_set.calculate_result()


class ResultSet:
    def __init__(self):
        self.r1 = None
        self.r2 = None
        self.has_or = False

    def set_or(self):
        self.has_or = True

    def calculate_result(self):
        repeat = True if self.r2 == '*' else False
        if self.r2 is None:
            pass
        elif repeat:
            self.calculate_repeat()
        elif self.has_or:
            self.calculate_or()
        else:
            self.calculate_and()
        return self.r1

    def calculate_repeat(self):
        self.r1.graph_repeat()

    def calculate_or(self):
        self.r1.graph_or(self.r2)

    def calculate_and(self):
        self.r1.graph_add(self.r2)

    def insert(self, value):
        if value != '*' and isinstance(value, str):
            value = RegexGraphNFA.get_char_graph(Alphabet[value])
        if self.r1 is None:
            self.r1 = value
        else:
            self.r2 = value


class RegexGraphNFA:
    node_count = 0

    def __init__(self):
        self.edges = None
        self.head = None
        self.tail = None

    @staticmethod
    def get_char_graph(value):
        my_graph = RegexGraphNFA()
        my_graph.insert_char(value)
        return my_graph

    @classmethod
    def get_next_node_id(cls):
        node_id = cls.node_count
        cls.node_count += 1
        return node_id

    def insert_char(self, value):
        self.head = self.get_next_node_id()
        self.tail = self.get_next_node_id()
        self.edges = {self.head: [Edge(self.tail, value)],
                      self.tail: []}

    def graph_add(self, other):
        join_node = self.get_next_node_id()
        self.join(other)
        self.edges[self.tail].append(empty_edge(join_node))
        self.edges[join_node] = [empty_edge(other.head)]
        self.tail = other.tail

    def graph_repeat(self):
        new_head = self.get_next_node_id()
        new_tail = self.get_next_node_id()
        self.edges[self.tail].extend([empty_edge(self.head), empty_edge(new_tail)])
        self.edges[new_head] = [empty_edge(self.head), empty_edge(new_tail)]
        self.edges[new_tail] = []
        self.head = new_head
        self.tail = new_tail

    def graph_or(self, other):
        new_head = self.get_next_node_id()
        new_tail = self.get_next_node_id()
        self.join(other)
        self.edges[new_head] = [empty_edge(self.head), empty_edge(other.head)]
        self.edges[self.tail].append(empty_edge(new_tail))
        self.edges[other.tail].append(empty_edge(new_tail))
        self.edges[new_tail] = []
        self.head = new_head
        self.tail = new_tail

    def join(self, other):
        for node, edge in other.edges.items():
            if node in self.edges:
                self.edges[node].extend(edge)
            else:
                self.edges[node] = edge

    def get_dfa_char_node_set(self, origin, use_char):
        node_set = set()
        for my_node in origin:
            for edges in self.edges[my_node]:
                if edges.char == use_char:
                    node_set.add(edges.dest)

        return self.get_dfa_zero_node_set(node_set)

    def get_dfa_zero_node_set(self, origin):
        node_set = set(origin)
        processed = set()
        while len(node_set.difference(processed)) > 0:
            my_node = node_set.difference(processed).pop()
            for edges in self.edges[my_node]:
                if edges.char == Alphabet.e:
                    node_set.add(edges.dest)
            processed.add(my_node)
        return frozenset(node_set)


class TranslateGraph:
    language = (Alphabet.a, Alphabet.b)

    def __init__(self, nfa_graph: RegexGraphNFA):
        self.node_count = 0
        self.nfa_graph = nfa_graph
        self.trans_to = {}
        self.trans_from = {}
        self.table = {}

    def get_next_node_id(self):
        node_id = self.node_count
        self.node_count += 1
        return node_id

    def add_translate(self, nfa_ids):
        if len(nfa_ids) == 0:
            return None
        if nfa_ids not in self.trans_from:
            dfa_id = self.get_next_node_id()
            self.trans_to[dfa_id] = nfa_ids
            self.trans_from[nfa_ids] = dfa_id
            self.table[dfa_id] = dict(zip(self.language, [None] * len(self.language)))
        return self.trans_from[nfa_ids]

    def translate(self):
        self.create_translate_table()
        return self.build_dfa()

    def build_dfa(self):
        head = 0
        valid_ends = set()
        adjacency = {}
        for node, edges in self.table.items():
            adjacency[node]= []
            if self.nfa_graph.tail in self.trans_to[node]:
                valid_ends.add(node)
            for my_char, node_dest in edges.items():
                if node_dest is not None:
                    adjacency[node].append(Edge(node_dest, my_char))
        return RegexGraphDFA(head,valid_ends,adjacency)

    def create_translate_table(self):
        nfa_ids = self.nfa_graph.get_dfa_zero_node_set({self.nfa_graph.head})
        self.add_translate(nfa_ids)
        processed = set()

        while len(set(self.table).difference(processed)) > 0:
            my_node = set(self.table).difference(processed).pop()
            for char in self.language:
                next_nodes = self.nfa_graph.get_dfa_char_node_set(self.trans_to[my_node], char)
                dfa_id = self.add_translate(next_nodes)
                self.table[my_node][char] = dfa_id
            processed.add(my_node)


class RegexGraphDFA:

    def __init__(self,head, valid_ends, edges):
        self.edges = edges
        self.head = head
        self.valid_ends = valid_ends
        self.edge_matrix = self.generate_edge_matrix_numpy()
        self.edge_matrix2 = self.generate_edge_matrix()
        a = 1

    def generate_edge_matrix(self):
        edge_matrix = []
        for i in range(len(self.edges)):
            edge_matrix.append([])
            for j in range(len(self.edges)):
                edge_matrix[i].append(0)
        for node, edge_list in self.edges.items():
            for dest_node, my_char in self.edges[node]:
                edge_matrix[node][ dest_node] += 1
        return edge_matrix

    def count_paths_old(self, length):
        modulo = 1000000007

       # edge_walk2 = self.edge_matrix ** length
        #count = 0
        #for end_node in self.valid_ends:
        #   count += edge_walk[self.head,end_node]
        valid_paths = self.find_paths(length)
        count = 0
        for node in self.valid_ends.intersection(valid_paths):
            count += valid_paths[node] % 1000000007
        #a = 1
        return count

    def generate_edge_matrix_numpy(self):
        import numpy
        edge_matrix = numpy.zeros((len(self.edges), len(self.edges)),dtype = numpy.uint64)
        for node, edge_list in self.edges.items():
            for dest_node, my_char in self.edges[node]:
                edge_matrix[node, dest_node] += 1
        return numpy.matrix(edge_matrix)

    def count_paths(self, length):
        modulo = 1000000007
        #valid_paths = self.find_paths(length)
        #edge_walk2 = self.edge_matrix ** length
        length_chunk = 10000
        result = self.generate_mod_power()
        if length <= length_chunk:
            edge_walk = self.edge_matrix ** length
        else:
            full = length // length_chunk
            remaining = length % length_chunk
            edge_walk = (self.edge_matrix ** length_chunk % modulo) %modulo
            for i in range(1,full):
                edge_walk %= modulo
                edge_walk *= self.edge_matrix ** length_chunk % modulo
            edge_walk *= self.edge_matrix ** remaining % modulo
        count = 0
        for end_node in self.valid_ends:
            count += edge_walk[self.head,end_node]
            #a = 1
        return count

    #def generate_mod_power(self):

    def find_paths(self, length):
        last_state = {self.head: 1}
        current_state_set = {}
        dist = 0
        while len(last_state) > 0 and dist < length:
            current_state_set = {}
            for node, count in last_state.items():
                for edges in self.edges[node]:
                    current_state_set[edges[0]] = current_state_set.get(edges[0], 0) + count
            last_state = current_state_set
            dist += 1
        return current_state_set


def main():
    cases = int(input().strip())
    for i in range(cases):
        in_line = input().strip().split()
        my_class = CountStrings(in_line[0])
        print(my_class.calculate(int(in_line[1])))



if __name__ == "__main__":
    main()
