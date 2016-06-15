import collections

class Security:
    def __init__(self,in_id, arr_in):
        self.id = in_id
        self.price = arr_in[0]
        self.confidence = arr_in[1]
        self.not_sure=self.price*self.confidence
        self.sure=self.price*100
        self.improvement = self.sure - self.not_sure
        self.actual= self.not_sure
        self.full_price = False
        self.on_default_list = False

    def __str__(self):
        return 'ID %s P %s C %s S %s NS %s IMP %s A %s FP %s DL %s'%(self.id,self.price,self.confidence,self.sure,self.not_sure,
                                                               self.improvement,self.actual,self.full_price,
                                                               self.on_default_list)

class Solution:
    def __init__(self):
        self.number,self.max_to_sell, self.min_can_sell = get_int_list(input())
        self.securities={}
        for i in range(self.number):
            self.securities[i]=Security(i,get_int_list(input()))

    def get_added_list(self):
        sure_list = sorted(self.securities.values(),reverse=True,key=lambda x:(x.sure,x.not_sure))
        added_vals = 0
        for sure in sure_list:
            a = 1
            if not sure.on_default_list:
                added_vals+=1
                sure.improvement = sure.sure - undoctored_list[len(undoctored_list)-added_vals].not_sure
        if added_vals > 1:
            sure_list = sorted(self.securities.values(),reverse=True,key=lambda x:(x.improvement,x.not_sure))[0:self.min_can_sell]
        for sure in sure_list:
            sure.full_price = True
            sure.actual = sure.sure

    def calculate(self):
        undoctored_list =sorted(self.securities.values(),reverse=True,key=lambda x:(x.not_sure))[0:self.max_to_sell]
        for sec in undoctored_list:
            sec.on_default_list = True
        added_list = self.get_added_list()
        final_tentative_list = sorted(self.securities.values(),reverse=True,key=lambda x:(x.actual))[0:self.max_to_sell]
        price = 0
        full_count = 0
        for final in final_tentative_list:
            price+=final.actual
            if final.full_price:
                full_count+=1
        return price

def main():
    my_object = Solution()
    print(my_object.calculate())


def get_int_list(in_str):
    return [int(i) for i in in_str.strip().split()]


if __name__ == "__main__":
    main()
