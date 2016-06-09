
def main():
    in_str = input()
    nodes, edges = get_int_list(in_str)
    dist = [[None]*nodes for i in range(nodes)]
    for i in range(nodes):
        dist[i][i] = 0
    for i in range(edges):
        edge_str = input()
        edge_list = get_int_list(edge_str)
        dist[edge_list[0] - 1][edge_list[1] - 1] = edge_list[2]
    for k in range(nodes):
        for i in range(nodes):
            for j in range(nodes):
                if dist[i][k] is not None and dist[k][j] is not None:
                    if dist[i][j] is None or dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
    case_str = input().strip()
    queries = int(case_str)
    for i in range(queries):
        origin, destination = get_int_list(input().strip())
        result = dist[origin-1][destination-1]
        print(result if result is not None else -1)

def get_int_list(in_str):
    return [int(i) for i in in_str.strip().split()]


if __name__ == "__main__":
    main()
