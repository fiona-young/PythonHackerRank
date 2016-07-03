class Solution:
    def __init__(self):
        self.K = int(input())
        self.A = int(input(),16)
        self.B = int(input(),16)
        self.C = int(input(),16)

    def calculate(self):
        changes = bin((self.A|self.B)^self.C).count("1")
        if changes > self.K:
            print(-1)
            return
        max_len = max(self.A.bit_length(),self.B.bit_length(),self.C.bit_length())
        a_str = '0'*(max_len-self.A.bit_length())+"{:b}".format(self.A)
        b_str = '0'*(max_len-self.B.bit_length())+"{:b}".format(self.B)
        c_str = '0'*(max_len-self.C.bit_length())+"{:b}".format(self.C)
        a = [int(i) for i in a_str]
        b = [int(i) for i in b_str]
        c = [int(i) for i in c_str]
        remaining_swaps = self.K
        #get to pass
        for i in range(max_len):
            if (a[i] | b[i])!=c[i]:
                if c[i] == 1:
                    b[i]=1
                    remaining_swaps -=1
                else:
                    if b[i]== 1:
                        b[i]=0
                        remaining_swaps -=1
                    if a[i]==1:
                        a[i]=0
                        remaining_swaps -=1
        if remaining_swaps < 0:
            print(-1)
            return
        if remaining_swaps == 0:
            print_hex(a,b)
            return

        #minimise a
        for i in range(max_len):
            if a[i] == 1:
                if b[i]==1:
                    a[i]=0
                    remaining_swaps -=1
                elif remaining_swaps >= 2:
                    b[i]=1
                    a[i]=0
                    remaining_swaps -=2
            if remaining_swaps == 0:
                break
        print_hex(a,b)
        return

def print_hex(a, b):
    print('{0:X}\n{1:X}'.format(int(''.join([str(i) for i in a]),2),int(''.join([str(i) for i in b]),2)))

def main():
    cases = int(input())
    for i in range(cases):
        my_object = Solution()
        my_object.calculate()


def get_int_list(in_str):
    return [int(i) for i in in_str.strip().split()]


if __name__ == "__main__":
    main()
