
def main():
    chapters, max_problems_per_page = get_int_list(input())
    problems_per_chapter = get_int_list(input())
    page = 0
    special_count = 0
    for problem_count in problems_per_chapter:
        for problem in range(1, problem_count+1):
            if (problem-1)%max_problems_per_page == 0:
                page+=1
            if page == problem:
                special_count += 1
    print(special_count)


def get_int_list(in_str):
    return [int(i) for i in in_str.strip().split()]


if __name__ == "__main__":
    main()
