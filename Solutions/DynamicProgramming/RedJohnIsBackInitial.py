import collections
import math
class Solution:
    DIM = 4

    def __init__(self):
        self.primes = Primes()
        self.fact = {}
        self.size = int(input())
        self.n_array = []
        for i in range(self.size):
            self.n_array.append(int(input()))

    def calculate(self):
        for n in self.n_array:
            print(self.calculate_for_n(n))

    def calculate_for_n(self, n):

        combinations = 0
        for i in range((n // self.DIM)+1):
            combinations += self.get_combinations(i, n)
        return self.primes.count_primes_up_to(combinations)

    def get_combinations(self, index, count):
        remaining = count-(index*self.DIM)
        if index == 0 or remaining==0:
            return 1
        groups = Groups()
        groups = groups.get_group_counts(remaining,index+1)
        combinations = 0
        for group in groups:
            extra_combinations = self.get_factorial(index+1)
            denominator = 1
            for count in group.values():
                denominator*=self.get_factorial(count)
            extra_combinations//=denominator
            combinations += extra_combinations
        return combinations

    def get_factorial(self,val):
        if val not in self.fact:
            self.fact[val]=math.factorial(val)
        return self.fact[val]


Ongoing = collections.namedtuple('Ongoing','remaining, values')

class Groups:
    def get_group_counts(self, uprights, sides):
        groups = self.get_groups(uprights, sides)
        group_counts = []
        for values in groups:
            count = collections.defaultdict(int)
            for value in values:
                count[value]+=1
            group_counts.append(count)
        return group_counts


    def get_groups(self, uprights, sides):
        my_list = [Ongoing(uprights-i,(i,)) for i in range(1,uprights+1)]
        for i in range(1,sides):
            sides_remaining = sides-i
            my_list_old = my_list
            my_list = []
            for previous in my_list_old:
                last_value = previous.values[len(previous.values)-1]
                if i == sides-1:
                    if previous.remaining <= last_value:
                        my_list.append(previous.values+(previous.remaining,))
                else:
                    for j in range(min(last_value,previous.remaining)+1):
                        if j*sides_remaining >= previous.remaining:
                            my_list.append(Ongoing(previous.remaining-j,previous.values+(j,)))
        return my_list



class Primes:
    def __init__(self):
        self.cache = [0,0]
        self.primes = []
        self.last = 1

    def count_primes_up_to(self, value):
        if self.last < value:
            for i in range(self.last + 1, value + 1):
                self.cache.append(self.cache[i-1])
                if self.is_prime(i):
                    self.cache[i] += 1
            self.last = value
        return self.cache[value]

    def is_prime(self, value):
        if value != 2 and value%2 == 0:
            return False
        for i in range(3, int(value ** 0.5)+1, 2):
            if value % i == 0:
                return False
        self.primes.append(value)
        return True


def main():
    my_object = Solution()
    my_object.calculate()


def get_int_list(in_str):
    return [int(i) for i in in_str.strip().split()]


if __name__ == "__main__":
    main()
