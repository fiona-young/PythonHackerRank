
from collections import deque

# https://www.hackerrank.com/challenges/beautiful-path

# Turn the graph into unweighted, so you can run bfs on it.
# There are only 2**10 binary lengths between 2 vertices
# Turn
#
#
#

def make_graph():
    N, M = [int(x) for x in input().split()]
    graph = {x:[] for x in range(N)}
    for _ in range(M):
        start, finish, cost = [int(x) for x in input().split()]
        graph[start-1].append((finish-1, cost))
        graph[finish-1].append((start-1, cost))

    # assertEqual(N, len(graph))
    return graph


def bfs(graph, start, finish):
    visited = set()
    visited.add((start-1, 0))
    min_cost = 1025
    queue = deque([]) # make a queue from deque object
    queue.appendleft((start-1, 0))
    compare = 0
    while queue:
        v = queue.pop() # study the first out element from queue
        for idx in range(len(graph[v[0]])): # all v's children indices
            v2 = graph[v[0]][idx][0] # each child
            cost_v2 = graph[v[0]][idx][1] # and their cost
            v_next = (v2, v[1] | cost_v2) # next node to add to the queue
            compare += 1

            if v_next not in visited: # still hasn't been visited
                visited.add(v_next) # to get to the child we need one more step than to parent
                queue.appendleft(v_next)
                if v2 == finish-1:
                    min_cost = min(min_cost, v_next[1])
    print(compare)
    if min_cost != 1025:
        return min_cost
    else:
        return "-1"


def main():
    graph = make_graph()
    start, finish = map(int, input().split())
    print (bfs(graph, start, finish))

if __name__ == "__main__":
    main()