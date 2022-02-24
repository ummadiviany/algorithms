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
        



    
if __name__ == "__main__":
    

    G = {
    'a' : {'b', 'e'},
    'b' : {'a'},
    'e' : {'a', 'i', 'j'},
    'i' : {'e', 'j'},
    'j' : {'e', 'i'},
    'f' : {},
    'c' : {'d', 'h', 'g'},
    'g' : {'c', 'h', 'k'},
    'h' : {'c', 'g', 'k','d','l'},
    'k' : {'g', 'h'},
    'd' : {'c', 'h'},
    'l' : {'h'},
    }
    
    dfs(OrderedDict(G))