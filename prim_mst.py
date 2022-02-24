from heapq import heappush, heappop, heapify
from math import inf
from collections import OrderedDict

def prim(G):
    cost = {v:inf for v in G}
    prev = {v:None for v in G}
    
    cost['A'] = 0

    H = []
    heapify(H)
    for v in G:
        heappush(H, (cost[v], v))

    while H:
        print(H)
        _, v = heappop(H)
        print(v)
        for z in G[v].keys():
            if cost[z] > G[v][z]:
                cost[z] = G[v][z]
                prev[z] = v
                heappush(H, (cost[z], z))

        print("Cost:", cost)
        print("Prev:", prev)
        print()
    return cost, prev


if __name__ == '__main__':
    G = {
        'A': {'B':5, 'C':6, 'D':4},
        'B': {'A':5, 'C':1, 'D':2},
        'C': {'A':6, 'B':1, 'D':2, 'E':5, 'F':3},
        'D': {'A':4, 'B':2, 'C':2, 'F':4},
        'E': {'C':5, 'F':4},
        'F': {'C':3, 'D':4, 'E':4}
    }
    G = OrderedDict(G)
    
    
    cost, prev= prim(G)

    
    print("Distance:", cost)
    print("Previous:", prev)
    
    # print("Shortest Path length:", dist[tgt])
    # short_path = []
    # while True:
    #     short_path.append(tgt)
    #     tgt = prev[tgt]
    #     if tgt is None:
    #         break
    # print("Shortest Path:", end=' ')
    # print(*short_path[::-1], sep=' -> ')