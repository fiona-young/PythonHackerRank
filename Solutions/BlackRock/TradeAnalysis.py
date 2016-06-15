class SetList:
    def __init__(self,size,s):
        self.s = s
        self.size = size
        self.num = 2**size

    def get_g(self):
        cum_sum=[[0]*self.size for i in range(2)]
        save_sum = 0
        for i in range(self.size-1,-1,-1):
            save_sum += self.s[i]
            cum_sum[0][i]=save_sum
        g = 0
        for i in range(self.size):
            if i == 0:
                g+=cum_sum[0][0]
            else:
                save_sum = 0
                for j in range(self.size-i-1,-1,-1):
                    new_val =(self.s[j]*cum_sum[(i+1)%2][j+1])%1000000007
                    save_sum += new_val
                    cum_sum[i%2][j]=save_sum
                    g=(g+new_val*(i+1))%1000000007
        return g%1000000007

class Solution:
    def __init__(self):
        self.size = int(input())
        self.s = get_int_list(input())[0:self.size]

    def calculate(self):
        set_list = SetList(self.size,self.s)
        result = set_list.get_g()
        return result


def main():
    my_object = Solution()
    print(my_object.calculate())


def get_int_list(in_str):
    return [int(i) for i in in_str.strip().split()]


if __name__ == "__main__":
    main()
