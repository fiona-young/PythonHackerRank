def get_result(set_max, target):
    my_target = min(target, set_max)
    while True:
        binary_str = format(my_target, 'b')
        if '0' in binary_str:
            my_list = list(binary_str)
            my_list[binary_str.rfind('0')] = '1'
            binary_str2 = ''.join(my_list)
        else:
            binary_str2 = '1' + binary_str
        if int(binary_str2, 2) <= set_max:
            return my_target
        else:
            my_target -= 1


def main():
    cases = int(input())
    for i in range(cases):
        in_str = input()
        set_max, target = [int(i) for i in in_str.strip().split()]
        target -= 1
        print(get_result(set_max, target))


if __name__ == "__main__":
    main()
