from collections import deque


def EKBreadthFirstSearch(Capacity, Edge, Src, Snk, mfMatrix):
    N = len(Capacity)
    parentTable = [-1] * N
    parentTable[Src] = -2
    newCapacity = [0] * N
    newCapacity[Src] = 0xFFFFFFFFFFFFFFF
    Q = deque()
    Q.append(Src)
    while len(Q) > 0:
        u = Q.popleft()
        curEdge = 0
        if u == Src:
            curEdge = sorted([x for x in Edge[u]], key=lambda v: len(Edge[v]))
        elif u % 2 == 0:
            curEdge = sorted([x for x in Edge[u]], key=lambda v: len(Edge[v - 1]))
        else:
            curEdge = Edge[u]
        for v in curEdge:
            if (Capacity[u][v] - mfMatrix[u][v] > 0) and (parentTable[v] == -1):
                parentTable[v] = u
                newCapacity[v] = min(newCapacity[u], Capacity[u][v] - mfMatrix[u][v])
                if v != Snk:
                    Q.append(v)
                else:
                    return newCapacity[Snk], parentTable
    return 0, parentTable


def EdmondsKarp(Capacity, Edge, Src, Snk):
    N = len(Capacity)
    maxflow = 0
    mfMatrix = [[0] * N for i in range(N)]
    while True:
        foundCapacity, parentTable = EKBreadthFirstSearch(Capacity, Edge, Src, Snk, mfMatrix)
        if foundCapacity == 0:
            break
        maxflow += foundCapacity
        # Backtrack search, and apply flow
        v = Snk
        while v != Src:
            # print(v,end=" ")
            u = parentTable[v]
            mfMatrix[u][v] += foundCapacity
            mfMatrix[v][u] -= foundCapacity
            v = u
    # print()
    return maxflow, mfMatrix

def main():
    T = int(input())
    for _ in range(T):
        iNumV, iMaxLeg, iNumE = tuple(map(int, input().split()))
    # Produce Initial condition
        mfNumV = 2 * iNumV + 2  # 2X for duplicating, +2 for source and sink
        Src = 2 * iNumV
        Snk = 2 * iNumV + 1
        Capacity = [[0] * mfNumV for i in range(mfNumV)]
        Edge = [[] for i in range(mfNumV)]
        for e in range(iNumE):
            v1, v2 = tuple(
                map(lambda x: int(x) - 1, input().split()))  # To make node index range from 0 to N-1 instead of 1 to N
            Edge[2 * v1].append(2 * v2 + 1)
            Edge[2 * v2].append(2 * v1 + 1)
            Capacity[2 * v1][2 * v2 + 1] = 1
            Capacity[2 * v2][2 * v1 + 1] = 1
        for i in range(len(Edge)):
            Edge[i].sort()
        # for c in Capacity:
    #	print(" ".join(map(str,c)))
    # print()
        for i in range(0, 2 * iNumV, 2):
            Edge[Src].append(i)  # Edge from Source to possible CrabHead
            Edge[i + 1].append(Snk)  # Edge from possible CrabLeg to sink
            Capacity[Src][i] = min(len(Edge[i]), iMaxLeg)
            Capacity[i + 1][Snk] = 1
        # for c in Capacity:
    #	print(" ".join(map(str,c)))
        maxflow, mfMatrix = EdmondsKarp(Capacity, Edge, Src, Snk)
        print(maxflow)

if __name__ == "__main__":
    main()