import collections

CLOSE = 10


class Solution:
    def __init__(self):
        self.number = int(input())
        self.rating = get_int_list(input())[0:self.number]
        self.tentative_reward = get_int_list(input())[0:self.number]
        self.rating_tup = list(zip(self.rating,range(self.number)))
        self.rating_tup.sort()
        self.change = 0

    def calculate(self):
        tentative_sum = 0
        for rating, i in self.rating_tup:
            current_rating = self.rating[i]
            current_tentative_reward = self.tentative_reward[i]
            self.tentative_reward[i] = self.get_update_reward(i, current_rating, current_tentative_reward)
            tentative_sum +=  self.tentative_reward[i]
        return tentative_sum


    def get_update_reward(self, i, current_rating, current_tentative_reward):
        new_tentative_reward = current_tentative_reward
        min_val1 = max(i - CLOSE, 0)
        min_val2 = min(i + 1, self.number)
        max_val2 = min(i + CLOSE + 1, self.number)
        available_keys = list(range(min_val1, i)) + list(range(min_val2, max_val2))
        for i in available_keys:
            if current_rating > self.rating[i] and self.tentative_reward[i] >= new_tentative_reward:
                new_tentative_reward = self.tentative_reward[i] + 1
        self.change += abs(current_tentative_reward-new_tentative_reward)
        return new_tentative_reward


def main():
    my_object = Solution()
    print(my_object.calculate())


def get_int_list(in_str):
    return [int(i) for i in in_str.strip().split()]


if __name__ == "__main__":
    main()
