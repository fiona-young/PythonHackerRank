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

class ResultWrapper:
    def __init__(self, result):
        self.result = result

class RepeatBox:
    type = Type.type_repeat_box

class StrLen:
    def __init__(self, in_type, in_len, in_value):
        self.type = in_type
        self.len = in_len
        self.value = in_value

    def __str__(self):
        return "t:%s l:%s v:%s"%(self.type.value, self.len, self.value)
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

    def traverse(self, traverse_list):
        traverse_list.append(self)

    def count_matches(self, length):
        remaining = length - len(self.my_string)
        if remaining >= 0:
            return 1, {remaining}
        else:
            return 0, {remaining}

    def count_matches2(self, length):
        remaining = length - len(self.my_string)
        if remaining >= 0:
            return 1, {remaining}
        else:
            return 0, {remaining}

    def __len__(self):
        return len(self.my_string)


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

    def count_matches2(self, length):
        count1, remaining1 = self.r1.count_matches(length)
        if len(remaining1) > 1:
            raise IndexError
        count2, remaining2 = self.r2.count_matches(length-remaining1.pop())
        return count2, remaining2

    def walk(self,content):
        content[self.type]+=1
        self.r1.walk(content)
        self.r2.walk(content)

    def traverse(self, traverse_list):
        self.r1.traverse(traverse_list)
        self.r2.traverse(traverse_list)


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
        count2, remaining2 = self.r2.count_matches(length)
        return count1 + count2, remaining1.union(remaining2)

    def count_matches2(self, length):
        count1, remaining1 = self.r1.count_matches(length)
        count2, remaining2 = self.r2.count_matches(length)
        return count1 + count2, remaining1.union(remaining2)

    def walk(self,content):
        content[self.type]+=1
        self.r1.walk(content)
        self.r2.walk(content)

    def traverse(self, traverse_list):
        traverse_list.append([self.r1,self.r2])

class CountRemainingReturn:
    def __init__(self,count, remaining):
        my_dict={remaining:count}

    def __or__(self, other):
        a = 1


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

    def count_matches2(self, length):
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

    def traverse(self, traverse_list):
        traverse_list.append(self)

    def __len__(self):
        return len(self.value)