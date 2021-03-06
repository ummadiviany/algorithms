from collections import OrderedDict

def explore(G,visited,v,pre_visit_nums,post_visit_nums,ccnums,clock,cnum):

    """
    Finding all nodes reachable from v
    """
    
    visited[v] = True
    pre_visit_nums[v] = clock
    clock += 1
    ccnums[v] = cnum
    print(f"Pre  Visited : {v}, prenum : {pre_visit_nums[v]}, postnum : {post_visit_nums[v]}, cnum : {ccnums[v]}")
    for x in G[v]:
        if not visited[x]:
            clock = explore(G,visited,x,pre_visit_nums,post_visit_nums,ccnums,clock,cnum)
    
    post_visit_nums[v] = clock
    clock += 1
    print(f"Post Visited : {v}, prenum : {pre_visit_nums[v]}, postnum : {post_visit_nums[v]}, cnum : {ccnums[v]}")

    return clock
    

    
    

def dfs(G):
    """
    Depth-first search for previsit, postvisit, and connected component numbers
    """

    visited = {v:False for v in G}
    pre_visit_nums = {v:None for v in G}
    post_visit_nums = {v:None for v in G}
    ccnums = {v:None for v in G}

    cnum = 0
    clock = 1

    for v in G:
        if not visited[v]:
            cnum += 1
            clock = explore(G,visited,v,pre_visit_nums,post_visit_nums,ccnums,clock,cnum)
        

    return pre_visit_nums,post_visit_nums,ccnums

    
if __name__ == "__main__":
    

    # G = {
    # 'a' : {'b', 'e'},
    # 'b' : {'a'},
    # 'e' : {'a', 'i', 'j'},
    # 'i' : {'e', 'j'},
    # 'j' : {'e', 'i'},
    # 'f' : {},
    # 'c' : {'d', 'h', 'g'},
    # 'g' : {'c', 'h', 'k'},
    # 'h' : {'c', 'g', 'k','d','l'},
    # 'k' : {'g', 'h'},
    # 'd' : {'c', 'h'},
    # 'l' : {'h'},
    # }

    # G1 = {
    #     'a' : {'b', 'c', 'f'},
    #     'b' : {'e'},
    #     'c' : {'d'},
    #     'd' : {'a','h'},
    #     'e' : {'f','g','h'},
    #     'f' : {'b','g'},
    #     'g' : {},
    #     'h' : {'g'}
    # }
    G = {
        'A' : {'D':3},
        'B' : {'E':2},
        'C' : {},
        'D' : {'A':3,'H':7},
        'E' : {'B':2,'G':7,'H':2},
        'F' : {'G':2},
        'G' : {'I':2,'E':7,'F':2},
        'H' : {'I':8,'D':7,'E':2},
        'I' : {'G':2,'H':8}
    }
    
    pre_visit_nums,post_visit_nums,ccnums = dfs(OrderedDict(G))
    print(f"Pre  Visited              : {pre_visit_nums}")
    print(f"Post Visited              : {post_visit_nums}")
    print(f"ConnectedComponents       : {ccnums}")