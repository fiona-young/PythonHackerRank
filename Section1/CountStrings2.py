
class CountStrings:
    def __init__(self, regex_string):
        self.regex_string = regex_string
        self.nfa_graph = self.translate_regex()

    def calculate(self, string_length):
        return self.nfa_graph.count_paths(string_length)

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

    def get_matches_object(self):
        return 0

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
            value = RegexGraph(value)
        if self.r1 is None:
            self.r1 = value
        else:
            self.r2 = value

class RegexGraph:
    node_count = 0

    def __init__(self, value = None):
        if value is None:
            return
        self.edges = {RegexGraph.node_count: [(RegexGraph.node_count + 1, value)],
                           RegexGraph.node_count + 1: []}
        self.head = RegexGraph.node_count
        self.tail = RegexGraph.node_count + 1
        RegexGraph.node_count +=2
        self.valid_ends = {self.tail}

    def graph_add(self, other):
        translation = {other.head: self.tail}
        other.translate(translation)
        self.join(other)
        self.tail = other.tail
        self.valid_ends = other.valid_ends

    def graph_repeat(self):
        self.valid_ends.add(self.head)
        self.edges[self.tail].extend(self.edges[self.head])

    def translate(self, translation):
        new_edges = {}
        for node, edge_list in self.edges.items():
            new_node = translation[node] if node in translation else node
            for i, edges in enumerate(edge_list):
                if edges[0] in translation:
                    edge_list[i] = translation[edges[0]], edges[1]
            new_edges[new_node] = edge_list
        new_ends = set()
        for end in self.valid_ends:
            new_end = translation[end] if end in translation else end
            new_ends.add(new_end)
        self.edges = new_edges
        self.valid_ends = new_ends

    def join(self, other):
        for node, edge in other.edges.items():
            if node in self.edges:
                self.edges[node].extend(edge)
            else:
                self.edges[node]=edge

    def graph_or(self, other):
        translation = {other.head: self.head, other.tail: self.tail}
        other.translate(translation)
        self.join(other)

    def count_paths(self, length):
        dist = 0
        current_state = {self.head: 1}
        valid_paths = self.find_paths(length, dist, current_state)
        count = 0
        for node in self.valid_ends.intersection(valid_paths):
            count = valid_paths[node]
        return count

    def find_paths(self, length, dist, last_state):
        if len(last_state) == 0:
            return {}
        if dist == length:
            return last_state
        current_state_set = {}
        for node, count in last_state.items():
            for edges in self.edges[node]:
                current_state_set[edges[0]] = current_state_set.get(edges[0],0)+ count
        return self.find_paths(length, dist+1, current_state_set)


def main():
    cases = int(input().strip())
    for i in range(cases):
        in_line = input().strip().split()
        my_class = CountStrings(in_line[0])
        print(my_class.calculate(int(in_line[1])))


if __name__ == "__main__":
    main()
