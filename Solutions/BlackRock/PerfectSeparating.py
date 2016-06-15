class WordProcessor:
    def __init__(self,word,a_count,b_count):
        self.word = word
        self.half_len = a_count+b_count
        self.a_count = a_count
        self.b_count = b_count
        self.my_node_dict = None
        self.my_node_dict_old = None

    def process(self,):
        self.my_node_dict = {('','',0,0):1}
        for i,letter in enumerate(self.word):
            self.my_node_dict_old = self.my_node_dict
            self.my_node_dict = {}
            for (str1,str2,a_count1,a_count2),count in self.my_node_dict_old.items():
                add_a_count = 1 if letter == 'a' else 0
                if self.can_add_to(str1,str2,a_count1,letter):
                    key = (str1+letter,str2,a_count1+add_a_count,a_count2)
                    self.my_node_dict[key]=self.my_node_dict.get((key),0)+count
                if self.can_add_to(str2,str1,a_count2,letter):
                    key = (str1,str2+letter,a_count1,a_count2+add_a_count)
                    self.my_node_dict[key]=self.my_node_dict.get((key),0)+count
        return self.my_node_dict

    def can_add_to(self,str1,str2,a_count,letter):
        if letter == 'a' and  a_count == self.a_count:
                return False
        if letter == 'b' and  (len(str1)-a_count) == self.b_count:
                return False
        if len(str1) == self.half_len:
            return False
        if len(str1)>=len(str2) or (str2[len(str1)]==letter):
            return True
        return False


class Solution:
    def __init__(self):
        self.word = ''
        for i in input().strip():
            if i == 'a' or i == 'b':
                self.word += i
        self.len = len(self.word)
        self.a_count = 0
        self.b_count = 0
        for i, letter in enumerate(self.word):
            if letter == "a":
                self.a_count += 1
            else:
                self.b_count += 1

    def calculate(self):
        if self.a_count % 2 == 1 or self.b_count % 2 == 1:
            return 0
        self.a_count //= 2
        self.b_count //= 2
        word_processor = WordProcessor(self.word,self.a_count,self.b_count)
        success_list = word_processor.process()
        return sum(success_list.values())


def main():
    my_object = Solution()
    print(my_object.calculate())


def get_int_list(in_str):
    return [int(i) for i in in_str.strip().split()]


if __name__ == "__main__":
    main()
