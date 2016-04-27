from enum import Enum


class Operations(Enum):
    op_add = 1
    op_or = 2


class CountStrings:
    def __init__(self, regex_string, string_length):
        self.regex_string = regex_string
        self.string_length = string_length
        print("%s %s" % (self.regex_string, self.string_length))

    def calculate(self):
        matches = self.get_matches()
        print(matches)
        #count_object = matches.process_one(self.string_length)
        #return count_object

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
                result_set.insert(StringBox(my_char))
            index += 1
        return result_set.r1

class ResultSet:
    def __init__(self):
        self.r1 = None
        self.r2 = None
        self.op = Operations.op_add

    def set_or(self):
        self.op = Operations.op_or

    def calculate_result(self):
        #self handle
        if self.op is Operations.op_add:
            if self.r2 == "*":
                result = Repeat(self.r1)
            else:
                result = And(self.r1, self.r2)
        else:
            if self.r1 == self.r2:
                result = self.r1
            else:
                result = Or(self.r1, self.r2)
        return result

    def insert(self, value):
        if self.r1 is None:
            self.r1 = value
        else:
            self.r2 = value
        return self.r1, self.r2

class Simple:
    def __init__(self):
        self.level = 0

    def get_count_single(self):
        return CountReturn(2,2)

class StringBox(Simple):
    def __init__(self, my_string):
        super().__init__()
        self.my_string = my_string

    def __str__(self):
        return self.my_string

class And(Simple):
    def __init__(self, r1, r2):
        super().__init__()
        self.level = max(r1.level, r2.level)+1
        self.r1 = r1
        self.r2 = r2

    def __str__(self):
        return "(%s)(%s)"%(self.r1, self.r2)

class Or(Simple):
    def __init__(self, r1, r2):
        self.level = max(r1.level, r2.level)+1
        super().__init__()
        self.r1 = r1
        self.r2 = r2

    def __str__(self):
        return "(%s)|(%s)"%(self.r1, self.r2)

class Repeat(Simple):
    def __init__(self, value):
        super().__init__()
        self.value = value

    def get_count(self, str_len):
        return self

    def __str__(self):
        return "(%s)*"%self.value

class CountReturn:
    def __init__(self,results = None, uses = 0):
        self.result = results
        self.uses = uses


def main():
    cases = int(input().strip())
    for i in range(cases):
        in_line = input().strip().split()
        my_class = CountStrings(in_line[0], int(in_line[1]))
        print(my_class.calculate())


if __name__ == "__main__":
    main()
