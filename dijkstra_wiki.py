from heapq import heappush, heappop, heapify
from math import inf
from collections import OrderedDict

def dijkstra(G,src,tgt):
    dist = {v:inf for v in G}
    prev = {v:None for v in G}
    dist[src] = 0

    Q = []
    heapify(Q)
    for v in G:
        heappush(Q,(dist[v],v))

    while Q:
        print("Distance:", dist)
        print("Previous:", prev)
        print()
        u = heappop(Q)
        print("Current node:", u)
        u = u[1]
        if u == tgt:
            break
        for v in G[u]:
            alt = dist[u] + G[u][v]
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                heappush(Q, (alt,v))


    return dist, prev


if __name__ == '__main__':
    # G = {
    #     'A': {'B': 2, 'C': 3},
    #     'B': {'A': 2, 'C': 1, 'D': 3},
    #     'C': {'A': 3, 'B': 1, 'D': 2, 'E': 4},
    #     'D': {'B': 3, 'C': 2, 'E': 2, 'F': 4},
    #     'E': {'C': 4, 'D': 2, 'F': 3, 'G': 2},
    #     'F': {'D': 4, 'E': 3, 'G': 6},
    #     'G': {'E': 2, 'F': 6}
    # }
    # G = {
    #     'ABC' : {'D':3, 'E':2,'F':1},
    #     'D' : {'G':1,'H':7},
    #     'E' : {'G':7,'H':2},
    #     'F' : {'G':2,'H':1},
    #     'G' : {'I':2},
    #     'H' : {'I':8},
    #     'I' : {}
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
    src = 'A'
    tgt = None
    
    dist, prev = dijkstra(G, src, tgt)

    
    # print("Distance:", dist)
    # print("Previous:", prev)
    print("Shortest Path length:", dist[tgt])
    short_path = []
    while True:
        short_path.append(tgt)
        tgt = prev[tgt]
        if tgt is None:
            break
    print("Shortest Path:", end=' ')
    print(*short_path[::-1], sep=' -> ')