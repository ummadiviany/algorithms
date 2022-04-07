from collections import OrderedDict, defaultdict
from itertools import combinations
from math import inf


def find_salesman_shotest_path(G,start):
    """
    This function finds the shortest path starting from a node and covering all the nodes and ends at start node
    Input : Graph G(V,E) and start node
    Output : Cost Map and Path Map
    """
    D = G
    C = {(tuple(start),start):0}
    prev = {(tuple(start),start):None}
    n = len(G)
    nodes = list(sorted(G.keys()))
    
    for s in range(2,n+1):
        for subset in sorted(combinations(nodes,s)):
            if start in subset:
                C[(tuple(subset),start)] = inf

                for node_j in subset:
                    if node_j != start:
                        temp_dict = {
                                (tuple(sorted(set(subset).difference(node_j))),node_i) : C[(tuple(sorted(set(subset).difference(node_j))),node_i)] + D[node_i][node_j] for node_i in subset if node_i != node_j
                        }
                        key, val = min(temp_dict.items(), key=lambda x: x[1]) 
                        C[(tuple(subset),node_j)] = val
                        prev[(tuple(subset),node_j)] = key


    return C, prev, nodes


if __name__ == '__main__':
    
    G = {
        'A' : {'A':inf, 'B':1, 'C':4, 'D':inf, 'E':inf, 'F':inf, 'G':inf},
        'B' : {'A':1, 'B':inf, 'C':inf, 'D':3, 'E':6, 'F':inf, 'G':inf},
        'C' : {'A':4, 'B':inf, 'C':inf, 'D':2, 'E':inf, 'F':5, 'G':inf},
        'D' : {'A':inf, 'B':3, 'C':2, 'D':inf, 'E':2, 'F':4, 'G':inf},
        'E' : {'A':inf, 'B':6, 'C':inf, 'D':2, 'E':inf, 'F':2, 'G':7},
        'F' : {'A':inf, 'B':inf, 'C':5, 'D':4, 'E':2, 'F':inf, 'G':6},
        'G' : {'A':inf, 'B':inf, 'C':inf, 'D':inf, 'E':7, 'F':6, 'G':inf}
    }
    G = OrderedDict(G)
    start = 'A'
    C, prev, nodes = find_salesman_shotest_path(G,start)
    

    # Finding the minimum cost path and printing it
    temp_dict = {
        (tuple(nodes),node_j) : C[(tuple(nodes),node_j)] + G[node_j][start] for node_j in nodes if node_j != start
    }
    path_end, min_len = min(temp_dict.items(), key=lambda x: x[1]) 
    print("Minimum path length : ",min_len)

    # Creating path from end to start by backtracking with the help of prev dict 
    salesman_path = [start]
    while path_end != (tuple(start),start):
        salesman_path.append(path_end[1])
        path_end = prev[path_end]
    salesman_path.append(start)

    print("Minimum path : ", end=" ")
    print(*salesman_path[::-1], sep=" -> ")

    