from Section1.CountStrings.Operations import Operations, Type, RepeatBox, Repeat, Or, And, StringBox

class ResultWrapper:
    def __init__(self, result):
        self.result = result
        self.case_dict = {}

    def count_remaining(self, str_len):
        self.case_dict = self.result.count_remaining()
        return self.count_cases(str_len, self.case_dict)

    def count_cases(self,str_len, local_dict):
        count = 0
        if "rep" in local_dict:
            rep_dict = local_dict["rep"]
            del local_dict["rep"]
            count += self.count_repeats(str_len, rep_dict)
        for key, value in local_dict.items():
            if key == str_len:
               count += self.count_matches(value)
        return count

    def count_repeats(self, str_len, rep_dict):
        count = 0
        for key, value in rep_dict.items():
            if key <= str_len:
                match_count = self.count_matches(value)
                if str_len % key == 0:
                    count += match_count ** (str_len//key)
        return count

    def count_matches(self, value):
        if isinstance(value, str):
            return 1
        else:
            return len(value)

class CountRemainingReturn:
    def __init__(self, str_len):
        self.my_dict = {}
        self.initial_str_len = str_len

    def insert(self, count, remaining):
        if len(self.my_dict) == 0:
            self.my_dict = {remaining: count}

    def __or__(self, other):
        a = 1