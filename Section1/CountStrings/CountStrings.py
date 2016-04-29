from Section1.CountStrings.Operations import Operations, Type, RepeatBox, Repeat, Or, And, StringBox
from Section1.CountStrings.CountRemaining import ResultWrapper

class CountStrings:
    def __init__(self, regex_string, string_length):
        self.regex_string = regex_string
        self.string_length = string_length

    def calculate(self):
        matches = self.get_matches()
        count_object = matches.count_matches(self.string_length)
        return count_object

    def get_count(self, matches):
        count = 0
        if isinstance(matches, str):
            if len(matches) == self.string_length:
                return 1
            else:
                return 0
        else:
            for single_match in matches:
                count += self.get_count(single_match)
        return count

    def get_matches(self, index=0):
        result_set = ResultSet()
        while index < len(self.regex_string):
            my_char = self.regex_string[index]
            if my_char == '(':
                out_list, index = self.get_matches(index + 1)
                result_set.insert(out_list)
            elif my_char == ')':
                result = result_set.calculate_result()
                return result, index
            elif my_char == '|':
                result_set.set_or()
            else:
                result_set.insert(gen_string_box(my_char))
            index += 1
        return result_set.get_matches_object()

class ResultSet:
    def __init__(self):
        self.r1 = None
        self.r2 = None
        self.op = Operations.op_add
        self.has_or = False

    def get_matches_object(self):
        return Matches(ResultWrapper(self.r1))

    def set_or(self):
        self.op = Operations.op_or
        self.has_or = True

    def calculate_result(self):
        if self.r2 is None:
            return self.r1
        if self.r2.type == Type.type_repeat_box:
            return Repeat(self.r1)
        elif self.has_or:
            if self.r1 == self.r2:
                return self.r1
            else:
                return Or(self.r1, self.r2)
        elif self.r1.type == Type.type_string and self.r2.type == Type.type_string:
            return self.r1.collapse(self.r2)
        else:
            return And(self.r1, self.r2)

    def insert(self, value):
        if self.r1 is None:
            self.r1 = value
        else:
            self.r2 = value
        return self.r1, self.r2


def gen_string_box(my_string):
    if my_string == "*":
        return RepeatBox()
    else:
        return StringBox(my_string)

class Matches:
    def __init__(self, result):
        self.result = result

    def __str__(self):
        return "matches: " + str(self.result.result)

    def count_matches(self, str_len):
        content = {Type.type_string:0, Type.type_or:0,Type.type_repeat:0,Type.type_and:0}
        self.result.result.walk(content)
        if content[Type.type_repeat]<2:
            return self.count_simple_repeat(str_len)
        else:
            return self.count_complex_repeat(str_len)


    def count_complex_repeat(self, str_len):
        traverse_list = []
        self.result.result.traverse(traverse_list)
        granularity = 0
        matches = 0
        str_remaining = str_len
        repeat_matches = 0
        for traverse in traverse_list:
            current_matches, current_str_remaining = traverse.count_matches(str_remaining)
            if traverse.type == Type.type_repeat:
                granularity = max(granularity, len(traverse))
                repeat_matches = max(current_matches, repeat_matches)
            else:
                current_matches, current_str_remaining = traverse.count_matches(str_remaining)
                if len(current_str_remaining)>1:
                    raise IndexError
                str_remaining = current_str_remaining.pop()
                matches += current_matches
        if(str_remaining % granularity) == 0:
            matches += str_remaining//granularity
        else:
            matches = 0
        return matches

    def count_simple_repeat(self, str_len):
        return self.result.count_remaining(str_len)


def main():
    cases = int(input().strip())
    for i in range(cases):
        in_line = input().strip().split()
        my_class = CountStrings(in_line[0], int(in_line[1]))
        print(my_class.calculate())


if __name__ == "__main__":
    main()
