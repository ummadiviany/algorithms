from math import inf
from collections import deque
def bfs(G,s):
    """
    Breadth-first search algorithm
    """
    dist = {v:inf for v in G}
    prev = {v:None for v in G}
    dist[s] = 0
    Q = deque([])
    Q.append(s)
    while Q:
        u = Q.popleft()
        for v in G[u]:
            if dist[v] == inf:
                dist[v] = dist[u] + 1
                prev[v] = u
                Q.append(v)

    return dist,prev

if __name__ == '__main__':
    G = {
        'E': {'S','D'},
        'S': {'A','E','C','D'},
        'A': {'S','B'},
        'B': {'A','C'},
        'C': {'S','B'},
        'D': {'S','E'}
    }
    dist,prev = bfs(G,'S')
    print(dist)
    print(prev)