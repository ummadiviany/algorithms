from math import inf
from collections import OrderedDict

def toplogical_sort(v,stack,visited):
    visited[v] = True
    for i in G[v]:
        if not visited[i]:
            toplogical_sort(i,stack,visited)
    stack.append(v)

def shortest_path_dag(G, s):
    """
    The bellman-ford algorithm for single-source shortest paths in
    general graphs
    """
    visited = {v:False for v in G}
    stack = []

    for v in G:
        if not visited[v]:
            toplogical_sort(s,stack,visited)

    dist = {v:inf for v in G}
    prev = {v:None for v in G}
    dist[s] = 0

    while stack:
        u = stack.pop()
        for v in G[u]:
            if dist[u] + G[u][v] < dist[v]:
                dist[v] = dist[u] + G[u][v]
                prev[v] = u
        

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
    dist, prev = shortest_path_dag(G,src)
    print("Distance:", dist)
    print("Previous:", prev)
    print("Shortest Path length:", dist[tgt])
    short_path = []
    while True:
        short_path.append(tgt)
        tgt = prev[tgt]
        if tgt is None:
            break
    print("Shortest Path:", end=' ')
    print(*short_path[::-1], sep=' -> ')