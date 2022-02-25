from heapq import heappush, heappop, heapify
from math import inf
from collections import OrderedDict, defaultdict
from heapdict import heapdict

def prim(G):
    cost = {v:inf for v in G}
    prev = {v:None for v in G}
    selected = {v:False for v in G}
    
    cost['A'] = 0
    H = heapdict()

    for v in G:
        H[v] = cost[v]

    while H:
        v = H.popitem()[0]
        for z in G[v]:
            if cost[z] > G[v][z] and selected[z] == False:
                cost[z] = G[v][z]
                prev[z] = v
                H[z] = cost[z]

        selected[v] = True
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

    
    # print("Distance:", cost)
    # print("Previous:", prev)
    
    print("Total MST cost:", sum(cost.values()))
    print("Minimum Spanning Tree:")
    for v in G:
        print(prev[v], '<--->', v)