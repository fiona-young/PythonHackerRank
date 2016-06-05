
def read_input():
    n_product, n_employees = get_int_list()
    employee_process_time = get_int_list()

    return n_product, n_employees, employee_process_time

class Solution:
    def __init__(self):
        self.n_product, self.n_employees, self.employee_process_time = read_input()
        self.employee_process_time.sort()

    def calculate(self):
        high_guess = self.employee_process_time[0]*self.n_product
        low_guess = 0
        while (high_guess - low_guess) > 1:
            mid_guess = low_guess+((high_guess - low_guess)//2)
            if self.can_process_products_in_time(mid_guess):
                high_guess = mid_guess
            else:
                low_guess = mid_guess
        return high_guess

    def can_process_products_in_time(self, time):
        products = 0
        for process_time in self.employee_process_time:
            products += time//process_time
            if products >= self.n_product:
                return True
        return False

def main():
    my_object = Solution()
    print(my_object.calculate())


def get_int_list():
    return [int(i) for i in input().strip().split()]


if __name__ == "__main__":
    main()
