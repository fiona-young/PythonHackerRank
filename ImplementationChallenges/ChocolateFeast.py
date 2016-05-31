
def main():
    cases = int(input())
    for i in range(cases):
        cash, price, bonus = get_int_list(input())
        bought = cash//price
        eaten = bought
        unclaimed = bought
        while unclaimed >= bonus:
            bonus_chocolates = unclaimed //bonus
            unclaimed = unclaimed%bonus + bonus_chocolates
            eaten += bonus_chocolates
        print(eaten)


def get_int_list(in_str):
    return [int(i) for i in in_str.strip().split()]


if __name__ == "__main__":
    main()
