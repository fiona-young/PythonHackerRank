from math import ceil


def get_accurate_edges(nodes, clique_guess):
    calc_edges = (nodes ** 2 - (nodes % clique_guess) * ceil(nodes / clique_guess) ** 2 - (
                 clique_guess - (nodes % clique_guess)) * (nodes // clique_guess) ** 2) // 2
    return calc_edges


def get_result(nodes, edges):
    k = 1. / (1. - ((2. * edges) / (1. * nodes ** 2)))
    clique_guess = int(k)
    while clique_guess < nodes and edges > get_accurate_edges(nodes, clique_guess):
        clique_guess += 1
    return clique_guess


def main():
    cases = int(input())
    for i in range(cases):
        in_str = input()
        nodes, edges = [int(i) for i in in_str.strip().split()]
        print(get_result(nodes, edges))


if __name__ == "__main__":
    main()
