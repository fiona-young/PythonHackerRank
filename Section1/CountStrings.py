from enum import Enum


class Operations(Enum):
    op_add = 1
    op_or = 2
    op_repeat = 3


class Type(Enum):
    type_repeat_box = 1
    type_repeat = 2
    type_string = 3
    type_or = 4
    type_and = 5


class CountStrings:
    def __init__(self, regex_string, string_length):
        self.regex_string = regex_string
        self.string_length = string_length
        print("%s %s" % (self.regex_string, self.string_length))

    def calculate(self):
        matches = self.get_matches()
        print(matches)
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
        return Matches(self.r1)

    def set_or(self):
        self.op = Operations.op_or
        self.has_or = True

    def calculate_result(self):
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


# class Simple:
#    def __init__(self):
#        self.level = 0

#    def get_count_single(self):
#        return CountReturn(2,2)
def gen_string_box(my_string):
    if my_string == "*":
        return RepeatBox()
    else:
        return StringBox(my_string)
class Matches:
    def __init__(self, result):
        self.result = result

    def __str__(self):
        return "matches: " + str(self.result)

    def count_matches(self, str_len):
        content = {Type.type_string:0, Type.type_or:0,Type.type_repeat:0,Type.type_and:0}
        self.result.walk(content)
        print(content)
        if content[Type.type_repeat]<2:
            return self.count_simple_repeat(str_len)
        else:
            return self.count_complex_repeat(str_len)


    def count_complex_repeat(self, str_len):
        data = {}
        print(self.result.join_non_repeats(data))
        return 0

    def count_simple_repeat(self, str_len):
        matches, remaining = self.result.count_matches(str_len)
        if len(remaining) == 1 and remaining.pop() == 0:
            return matches
        else:
            return 0

class RepeatBox:
    type = Type.type_repeat_box


class StringBox:
    def __init__(self, my_string):
        self.type = Type.type_string
        self.level = 0
        self.my_string = my_string

    def __str__(self):
        return self.my_string

    def walk(self,content):
        content[self.type]+=1

    def collapse(self, string_box_2):
        return StringBox(self.my_string + string_box_2.my_string)

    def count_matches(self, length):
        remaining = length - len(self.my_string)
        if remaining >= 0:
            return 1, {remaining}
        else:
            return 0, {remaining}


class And:
    def __init__(self, r1, r2):
        self.type = Type.type_and
        self.r1 = r1
        self.r2 = r2

    def __str__(self):
        return "(%s)(%s)" % (self.r1, self.r2)

    def count_matches(self, length):
        count1, remaining1 = self.r1.count_matches(length)
        if len(remaining1) > 1:
            raise IndexError
        count2, remaining2 = self.r2.count_matches(length-remaining1.pop())
        return count2, remaining2

    def walk(self,content):
        content[self.type]+=1
        self.r1.walk(content)
        self.r2.walk(content)


class Or:
    def __init__(self, r1, r2):
        self.type = Type.type_or
        self.level = max(r1.level, r2.level) + 1
        self.r1 = r1
        self.r2 = r2

    def __str__(self):
        return "(%s)|(%s)" % (self.r1, self.r2)

    def count_matches(self, length):
        count1, remaining1 = self.r1.count_matches(length)
        count2, remaining2 = self.r1.count_matches(length)
        return count1 + count2, remaining1.union(remaining2)

    def walk(self,content):
        content[self.type]+=1
        self.r1.walk(content)
        self.r2.walk(content)

class Repeat:
    def __init__(self, value):
        self.type = Type.type_repeat
        self.value = value

    def get_count(self, str_len):
        return self

    def __str__(self):
        return "(%s)*" % self.value

    def count_matches(self, length):
        count, remaining = self.value.count_matches(length)
        if len(remaining) > 1:
            raise IndexError
        match_remaining = remaining.pop()
        match_length = length - match_remaining
        power = match_remaining//match_length + 1
        return count ** power, {0}

    def walk(self,content):
        content[self.type]+=1
        self.value.walk(content)


class CountReturn:
    def __init__(self, results=None, uses=0):
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
