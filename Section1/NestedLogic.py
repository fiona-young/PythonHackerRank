from collections import namedtuple
Date = namedtuple("Date","day month year")


def no_charge(returned: Date, expected: Date):
    if returned.year < expected.year:
        return True
    if returned.month < expected.month and returned.year == expected.year:
        return True
    return returned.day <= expected.day and returned.month == expected.month and returned.year == expected.year


def get_charge():
    returned = Date(*get_int_list(input()))
    expected = Date(*get_int_list(input()))
    if no_charge(returned, expected):
        return 0
    if returned.month == expected.month and returned.year == expected.year:
        return (returned.day-expected.day) * 15
    if returned.year == expected.year:
        return (returned.month - expected.month) * 500
    return 10000


def main():
    print(get_charge())


def get_int_list(in_str):
    return [int(i) for i in in_str.strip().split()]


if __name__ == "__main__":
    main()
