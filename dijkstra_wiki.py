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
        u = heappop(Q)
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
    G = {
        'A': {'B': 2, 'C': 3},
        'B': {'A': 2, 'C': 1, 'D': 3},
        'C': {'A': 3, 'B': 1, 'D': 2, 'E': 4},
        'D': {'B': 3, 'C': 2, 'E': 2, 'F': 4},
        'E': {'C': 4, 'D': 2, 'F': 3, 'G': 2},
        'F': {'D': 4, 'E': 3, 'G': 6},
        'G': {'E': 2, 'F': 6}
    }
    G = OrderedDict(G)
    src = 'A'
    tgt = 'G'
    
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