
class CountStrings:
    def __init__(self, regex_string):
        self.regex_string = regex_string

    def calculate(self, string_length):
        regex_object = self.translate_regex()
        process_regex = ProcessRegex(regex_object)
        return process_regex.count(string_length)

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


class ProcessRegex:
    def __init__(self, regex_object):

        self.regex_object = self.wrap_string(regex_object)
        print(self.regex_object)
        self. rep_list =set()
        self. val_list =[]

    def __str__(self):
        return str(self.regex_object)

    def wrap_string(self, input):
        if isinstance(input, str):
            input = {len(input): {input}}
        return input

    def collapse(self, local_input, rep = False):
        local_input = self.wrap_string(local_input)
        if hasattr(local_input ,"items"):
            out = {}
            for key, value in local_input.items():
                if 'rep' == key:
                    out['rep'] = self.collapse(local_input['rep'], True)
                else:
                    if rep:
                        self.rep_list.add(len(self.val_list))
                    out[key] = count_cases(value)
                    self.val_list.append(value)
        else:
            out = []
            for value in local_input:
                out.append(self.collapse(value))
        if len(out) == 1 and 'rep' in out:
            out = out['rep']
        return out

    def count(self, str_len):
        self.remove_duplicates(self.regex_object)
        self.collapse_obj = self.collapse(self.regex_object)
        if len(self.rep_list) == 0:
            return 0 if str_len not in self.collapse_obj else self.collapse_obj[str_len]
        if isinstance(self.regex_object, dict) and 'rep' in self.regex_object:
            return count_repeats(str_len, self.collapse_obj)
        else:
            return self.count_complex_repeats(str_len)

    def remove_duplicates(self, my_obj):
        if not isinstance(my_obj, dict):
            return my_obj
        out_obj = my_obj.copy()
        if 'rep' in my_obj:
            out_obj['rep'] = self.remove_sub_duplicates(my_obj['rep'])
        else:
            out_obj = my_obj
        return out_obj

    def remove_sub_duplicates(self, my_obj):
        key_list = sorted(my_obj.keys())
        for i_small in range(len(key_list)):
            for i_large in range(i_small+1,len(key_list)):
                key_small = key_list[i_small]
                key_large = key_list[i_large]
                if(key_large % key_small) == 0:
                    for val in my_obj[key_small]:
                        if val * (key_large//key_small) in my_obj[key_large]:
                            my_obj[key_large].remove(val * (key_large//key_small))

        return my_obj

    def count_complex_repeats(self, str_len):
        granularity = {}
        matches = 0
        len_set = {str_len}
        for key, value in enumerate(self.collapse_obj):
            if key in self.rep_list:
                for item_key, item_value in value.items():
                    if item_key not in granularity:
                        granularity[item_key] = set()
                    granularity[item_key].add(item_value)
            else:
                old_len_set = len_set
                len_set = set()
                for my_len in old_len_set:
                    for item_key, item_value in value.items():
                        len_set.add(my_len - item_key)
                        matches += item_value
        for my_len in len_set:
            for item_key, item_value in granularity.items():
                if my_len % item_key == 0:
                    matches += my_len // item_key ** len(item_value)
        return matches


def count_cases(value):
    if isinstance(value, str):
        return 1
    else:
        return len(value)


def count_repeats(str_len, rep_dict):
    count = 0
    for key, match_count in rep_dict.items():
        if key <= str_len:
            if str_len % key == 0:
                count += match_count ** (str_len // key)
    return count


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
            res = self.r1
        elif repeat:
            res = self.calculate_repeat()
        elif self.has_or:
            res = self.calculate_or()
        else:
            res = self.calculate_and()
        return res

    def calculate_repeat(self):
        return {'rep': self.r1}

    def calculate_or(self):
        if isinstance(self.r1, str):
            self.r1 = {len(self.r1): {self.r1}}
        if isinstance(self.r2, str):
            self.r2 = {len(self.r2): {self.r2}}
        res = self.add_sets(self.r1, self.r2)
        return res

    def add_sets(self, r1, r2):
        res = r1.copy()
        if (len(set(self.r1).intersection(self.r2))) == 0:
            res.update(r2)
        else:
            for key, value in r2.items():
                if key in r2:
                    if isinstance(value, dict):
                        res[key] = self.add_sets(res[key], value)
                    else:
                        res[key].update(value)
                else:
                    res[key] = value

        a = 1
        return res

    def calculate_and(self):
        if isinstance(self.r1, str) and isinstance(self.r2, str):
            return self.r1 + self.r2
        if isinstance(self.r1, list):
            res = self.r1
        else:
            res = [self.r1]
        if isinstance(self.r2, list):
            res.extend(self.r2)
        else:
            res.append(self.r2)
        return res

    def insert(self, value):
        if self.r1 is None:
            self.r1 = value
        else:
            self.r2 = value
        return self.r1, self.r2


def main():
    cases = int(input().strip())
    for i in range(cases):
        in_line = input().strip().split()
        my_class = CountStrings(in_line[0])
        print(my_class.calculate(int(in_line[1])))


if __name__ == "__main__":
    main()
