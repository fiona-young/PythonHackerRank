import array


def main():
    mum = input().strip()
    dad = input().strip()
    str_len = len(mum)
    main_dp = [array.array('L', [0] * str_len) for i in range(2)]
    for i_mum in range(str_len):
        for i_dad in range(str_len):
            current_count = 1 if mum[i_mum] == dad[i_dad] else 0
            if i_mum == 0 or (i_dad == 0 and current_count == 1):
                above_count = 0
            elif current_count == 1:
                above_count = main_dp[(i_mum + 1) % 2][i_dad - 1]
            else:
                above_count = main_dp[(i_mum + 1) % 2][i_dad]
            if i_dad == 0:
                left_count = 0
            else:
                left_count = main_dp[i_mum % 2][i_dad - 1]
            main_dp[i_mum % 2][i_dad] = max(current_count + above_count, left_count)
    print(main_dp[(str_len + 1) % 2][-1])


def get_int_list(in_str):
    return [int(i) for i in in_str.strip().split()]


if __name__ == "__main__":
    main()
