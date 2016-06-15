import collections

#Spend = collections.namedtuple('Spend', 'max min')


class Solution:
    def __init__(self):
        array = input().strip().split()
        self.portfolio_value = int(array[0])
        self.rate = float(array[1])/100.
        self.time = int(array[2])
        self.threshold = int(array[3])
        self.spending_rate=tuple(get_int_list(input()))[0:self.time]
        self.total_spending_rate = sum(self.spending_rate)

    def calculate(self):
        spending_list = self.get_list()
        income_list = []
        current_income = self.calculate_income(self.spending_rate)
        for spend_rate in spending_list:
            income_list.append(self.calculate_income(spend_rate))
        income_list.sort(reverse=True)
        print("%.3f"%current_income[0])
        for i in range(3):
            print("%.3f - %s"%(income_list[i][0],income_list[i][1]) )

    def calculate_income(self, spend_rate):
        val = 1.
        income = 0
        for i in range(self.time):
            time = i+1
            income_add = (self.portfolio_value * spend_rate[i] * val *(1.+self.rate)**time)/(100.**time)
            income += income_add
            val *= 100-spend_rate[i]
        return (income, " ".join([str(x) for x in spend_rate]))

    def get_list(self,i=0,list_str = '',offset = 0):
        my_list = []
        if i == self.time:
            this_rate = get_int_list(list_str)
            if sum(this_rate)==self.total_spending_rate:
                return [this_rate]
            else:
                return None
        else:
            possible_change = (self.time-i-1)*self.threshold
            min_thresh = max(-offset-possible_change,-self.threshold)
            max_thresh = min(-offset+possible_change, self.threshold)
            for spending_rate in range(max(0,self.spending_rate[i]+min_thresh),self.spending_rate[i]+max_thresh+1):
                this_offset = offset + spending_rate-self.spending_rate[i]
                result = self.get_list(i+1,'%s %s'%(list_str,spending_rate),this_offset)
                if result is not None:
                    my_list.extend(result)
        return my_list

def main():
    my_object = Solution()
    my_object.calculate()


def get_int_list(in_str):
    return [int(i) for i in in_str.strip().split()]


if __name__ == "__main__":
    input_string = '''100000 5.5 5 15
99 27 96 29 32 74 85 1 43 37 32 56 46 8 48 85 1 37 79 94
'''
    import sys
    import io
    sys.stdin = io.StringIO(input_string)
    import cProfile
    cProfile.run("main()")
    #main()
