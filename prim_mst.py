from heapq import heappush, heappop, heapify
from math import inf
from collections import OrderedDict, defaultdict
from heapdict import heapdict
from statistics import median

def prim(G):
    cost = {v:inf for v in G}
    prev = {v:None for v in G}
    selected = {v:False for v in G}
    
    cost['A'] = 0
    H = heapdict()

    for v in G:
        H[v] = cost[v]

    while H:
        print("Cost:    ", cost)
        print("Previous:", prev)

        print()
        v = H.popitem()[0]
        print("Current node:", v)
        print()
        for z in G[v]:
            if cost[z] > G[v][z] and selected[z] == False:
                cost[z] = G[v][z]
                prev[z] = v
                H[z] = cost[z]

        selected[v] = True
    return cost, prev


if __name__ == '__main__':
    # G = {
    #     'A': {'B':5, 'C':6, 'D':4},
    #     'B': {'A':5, 'C':1, 'D':2},
    #     'C': {'A':6, 'B':1, 'D':2, 'E':5, 'F':3},
    #     'D': {'A':4, 'B':2, 'C':2, 'F':4},
    #     'E': {'C':5, 'F':4},
    #     'F': {'C':3, 'D':4, 'E':4}
    # }
    # G = {
    #     'A' : {'D':3},
    #     'B' : {'E':2},
    #     'C' : {'F':1},
    #     'D' : {'A':3,'G':1,'H':7},
    #     'E' : {'B':2,'G':7,'H':2},
    #     'F' : {'C':1,'G':2,'H':1},
    #     'G' : {'I':2,'D':1,'E':7,'F':2},
    #     'H' : {'I':8,'D':7,'E':2,'F':1},
    #     'I' : {'G':2,'H':8}
    # }
    # G = {
    #     'A' : {'D':3},
    #     'B' : {'E':2},
    #     'C' : {},
    #     'D' : {'A':3,'H':7},
    #     'E' : {'B':2,'G':7,'H':2},
    #     'F' : {'G':2},
    #     'G' : {'I':2,'E':7,'F':2},
    #     'H' : {'I':8,'D':7,'E':2},
    #     'I' : {'G':2,'H':8}
    # }
    G ={
        'A' : {'B':1, 'E':4, 'F':8},
        'B' : {'A':1, 'C':2, 'G':6, 'F':6},
        'C' : {'B':2, 'D':3, 'G':2},
        'D' : {'C':3, 'G':1, 'H':4},
        'E' : {'A':4, 'F':5},
        'F' : {'A':8, 'B':6, 'E':5, 'G':1},
        'G' : {'B':6, 'C':2, 'D':1, 'F':1, 'H':1},
        'H' : {'D':4, 'G':1}
    }
    G = OrderedDict(G)
    
    
    cost, prev= prim(G)

    #print("median:",median(cost.values()))

    
    # print("Distance:", cost)
    # print("Previous:", prev)
    
    print("Total MST cost:", sum(cost.values()))
    print("Minimum Spanning Tree:")
    for v in G:
        print(prev[v], '<--->', v)