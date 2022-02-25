from collections import OrderedDict, defaultdict

def find_path_compression(v, parent):
    """
    Find the root of the vertex
    using path compression technique
    """
    if v != parent[v]:
        parent[v] = find_path_compression(parent[v], parent)
    return parent[v]

def find(v, parent):
    """
    Find the root of the tree
    """
    if parent[v] is None:
        return v
    return find(parent[v], parent)

def union(x, y, parent, rank):
    """
    Union by rank
    """
    root_x = find(x,parent)
    root_y = find(y,parent)
    
    if root_x == root_y:
        return
    if rank[root_x] > rank[root_y]:
        parent[root_y] = root_x
    else:
        parent[root_x] = root_y
        if rank[root_x] == rank[root_y]:
            rank[root_y] += 1

def kruskal(G):
    """
    Kruskal's algorithm for finding minimum spanning tree
    Input : Graph G(V,E)
    Output: Minimum spanning tree
    """
    mst = defaultdict(dict)
    total_cost = 0

    edges = [(G[v][z],v,z) for v in G for z in G[v]]
    edges = sorted(edges, key = lambda x: x[0])

    parent = {v:None for v in G}
    rank = {v:0 for v in G}

    for edge in edges:
        cost,u,v = edge
        if find(u,parent) != find(v,parent):
            mst[u][v] = cost
            total_cost += cost
            union(u,v,parent,rank)
    
    return mst, total_cost


    

if __name__ == "__main__":
    G = {
        'A': {'B':5, 'C':6, 'D':4},
        'B': {'A':5, 'C':1, 'D':2},
        'C': {'A':6, 'B':1, 'D':2, 'E':5, 'F':3},
        'D': {'A':4, 'B':2, 'C':2, 'F':4},
        'E': {'C':5, 'F':4},
        'F': {'C':3, 'D':4, 'E':4}
    }
    G = OrderedDict(G)
    
    
    mst, total_cost = kruskal(G)

    print("Total cost of MST:", total_cost)
    print("Minimum Spanning Tree:", end='\n')
    for u in mst:
        print(f"{u} : {mst[u]}")