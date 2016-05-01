from Section1.CountStrings.Operations import Operations, Type, RepeatBox, Repeat, Or, And, StringBox

class ResultWrapper:
    def __init__(self, result):
        self.result = result
        self.case_dict = self.result.count_remaining()
        self.rep_list=set()
        self.val_list=[]
        self.collapse_obj = None
        self.repeat_num = 0
        print("case_dict ", self.case_dict)

    def count(self, str_len):
        print("str_len %s case_dict %s"% (str_len,self.case_dict))
        self.collapse_obj = self.collapse(self.case_dict)
        if len(self.rep_list) == 0:
            count = 0 if str_len not in self.collapse_obj else self.collapse_obj[str_len]
        elif len(self.rep_list) == 1:
            count = 0
            current_len = str_len
            for key, value in enumerate(self.val_list):
                if key not in self.rep_list:
                    print('not implemented:')
                else:
                    a = 1

            count = 0 if str_len not in self.collapse_obj else self.collapse_obj[str_len]

        a = 1
        count = 0
        return count


    def collapse(self, local_input, rep = False):

        if hasattr(local_input ,"items"):
            out = {}
            for key, value in local_input.items():
                if 'rep' == key:
                    out['rep'] = self.collapse(local_input['rep'], True)
                else:
                    if rep:
                        self.rep_list.add(len(self.val_list))
                    out[key] = self.count_matches(value)
                    self.val_list.append(value)
        else:
            out = []
            for value in local_input:
                out.append(self.collapse(value))

        return out



    def count_remaining(self, str_len):
        return self.count_cases(str_len, self.case_dict)

    def count_cases(self,str_len, local_dict):
        count = 0
        if "rep" in local_dict:
            rep_dict = local_dict["rep"]
            del local_dict["rep"]
            count += self.count_repeats(str_len, rep_dict)
        if hasattr(local_dict ,"items"):
            for key, value in local_dict.items():
                if key == str_len:
                    count += self.count_matches(value)
        else:
            for value in local_dict:
                count += self.count_cases(str_len, value)
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