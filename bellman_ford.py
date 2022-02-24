from math import inf
from collections import OrderedDict

def shortest_path(G, s):
    """
    The bellman-ford algorithm for single-source shortest paths in
    general graphs
    """
    
    dist = {v:inf for v in G}
    prev = {v:None for v in G}
    dist[s] = 0

    for i in range(len(G)-1):
        print(f"Iteration {i}: ", dist)
        for u in G:
            for v in G[u]:
                if dist[u] + G[u][v] < dist[v]:
                    dist[v] = dist[u] + G[u][v]
                    prev[v] = u
                #dist[v] = min(dist[v], dist[u] + G[u][v])
    print(f"Iteration {i+1}: ", dist)  
    return dist, prev


if __name__ == '__main__':
    G = {
        'S': {'A': 10, 'G': 8},
        'A': {'E':2},
        'B': {'A': 1, 'C': 1},
        'C': {'D': 3},
        'D': {'E': -1},
        'E': {'B': -2},
        'F': {'E': -1, 'A': -4},
        'G': {'F': 1}
    }
    G = OrderedDict(G)
    src = 'S'
    tgt = 'E'
    dist, prev = shortest_path(G,src)
    
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