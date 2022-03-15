from collections import OrderedDict, defaultdict
from itertools import combinations
from math import inf


def find_salesman_shotest_path(G,start):
    """
    This function finds the shortest path starting from a node and covering all the nodes and ends at start node
    """
    D = G
    C = {(tuple(start),start):0}
    # print("C:",C)
    n = len(G)
    nodes = list(sorted(G.keys()))
    # print("n:",n)
    # print("nodes:",nodes)
    # print(list(combinations(nodes,2)))
    for s in range(2,n+1):
        # print("\ns:",s)
        for subset in sorted(combinations(nodes,s)):
            if start in subset:
                # print("subset:",subset)
                C[(tuple(subset),start)] = inf

                for node_j in subset:
                    if node_j != start:
                        # print("node_j:",node_j)
                        #print("C:",C)
                        C[(tuple(subset),node_j)] = min(
                            [
                                C[(tuple(sorted(set(subset).difference(node_j))),node_i)] + D[node_i][node_j] for node_i in subset if node_i != node_j
                            ]
                        )

    return C, nodes


if __name__ == '__main__':
    # G = {
    #     'A':{'B':2, 'C':2, 'D':1, 'E':4},
    #     'B':{'A':2, 'C':3, 'D':2, 'E':3},
    #     'C':{'A':2, 'B':3, 'D':2, 'E':2},
    #     'D':{'A':1, 'B':2, 'C':2, 'E':4},
    #     'E':{'A':4, 'B':3, 'C':2, 'D':4}
    # }
    G = {
        'A':{'B':2, 'C':2, 'D':inf, 'E':inf},
        'B':{'A':2, 'C':inf, 'D':inf, 'E':3},
        'C':{'A':2, 'B':inf, 'D':2, 'E':inf},
        'D':{'A':inf, 'B':inf, 'C':2, 'E':4},
        'E':{'A':inf, 'B':3, 'C':inf, 'D':4}
    }
    G = OrderedDict(G)
    start = 'A'
    C, nodes = find_salesman_shotest_path(G,start)
    print("C:",C)
    min_path_len = min(
        [
            C[(tuple(nodes),node_j)] + G[node_j][start] for node_j in nodes if node_j != start
        ]
    )
    print("min_path_len:",min_path_len)