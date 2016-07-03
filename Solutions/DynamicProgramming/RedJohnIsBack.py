
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
        a = [1,1,1,1]
        for i in range(4,41):
            a.append(a[i-1]+a[i-4])
        for n in self.n_array:
            print(self.primes.count_primes_up_to(a[n]))


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
