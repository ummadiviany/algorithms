def explore(G,visited,v,pre_visit_nums,post_visit_nums,ccnums,prenum,postnum,cnum):
    """
    Finding all nodes reachable from v
    """
    
    visited[v] = True
    pre_visit_nums[v] = prenum
    prenum += 1
    ccnums[v] = cnum
    for v in G[v]:
        if not visited[v]:
            explore(G,visited,v,pre_visit_nums,post_visit_nums,ccnums,prenum,postnum,cnum)
    
    post_visit_nums[v] = prenum + 1
    print(f"Visited : {v}, prenum : {pre_visit_nums[v]}, postnum : {post_visit_nums[v]}, cnum : {ccnums[v]}")

    
    

def dfs(G):
    visited = {edge:False for edge in G}
    pre_visit_nums = {v:None for v in G}
    post_visit_nums = {v:None for v in G}
    ccnums = {v:None for v in G}

    prenum = 1
    cnum = 0
    postnum = None

    for v in G:
        if not visited[v]:
            cnum += 1
            explore(G,visited,v,pre_visit_nums,post_visit_nums,ccnums,prenum,postnum,cnum)
        



    
if __name__ == "__main__":
    G = {
    'a': {'b', 'd', 'c'},
    'b': {'e', 'f', 'a'},
    'c': {'a', 'f'},
    'd': {'a', 'g', 'h'},
    'e': {'b', 'i', 'j'},
    'f': {'c', 'b'},
    'g': {'d', 'h'},
    'h': {'d', 'g'},
    'i': {'e', 'j'},
    'j': {'e', 'i'},
    'k': {'l'},
    'l': {'k'}
}

    G1 = {
    'a' : {'b', 'e'},
    'b' : {'a'},
    'e' : {'a', 'i', 'j'},
    'i' : {'e', 'j'},
    'j' : {'e', 'i'},
    'f' : {},
    'c' : {'d', 'h', 'g'},
    'g' : {'c', 'h', 'k'},
    'h' : {'c', 'g', 'k','d'},
    'k' : {'g', 'h'},
    'd' : {'c', 'h'},
    'l' : {'h'},
    }
    
    dfs(G1)