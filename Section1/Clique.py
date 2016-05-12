from math import ceil, floor


def get_accurate_edges(nodes, clique_guess):
    nodes = int(nodes)
    clique_guess = int(clique_guess)
    calc_edges = (nodes**2-(nodes%clique_guess)*ceil(nodes/clique_guess)**2-(clique_guess-(nodes%clique_guess))*(nodes//clique_guess)**2)//2
    return calc_edges

def get_result(nodes, edges):
    k =1./(1.-((2.*edges)/(1.*nodes**2)))
    clique_guess = max(min(nodes,ceil(k))-3,1)
    while clique_guess <nodes and edges > get_accurate_edges(nodes,clique_guess):
        clique_guess+=1
    return int(clique_guess)

def main():
    cases = int(input())
    for i in range(cases):
        in_str = input()
        nodes, edges = [int(i) for i in in_str.strip().split()]
        print(get_result(nodes,edges))

def get_int_list(in_str):
    return [int(i) for i in in_str.strip().split()]


if __name__ == "__main__":
    main()
