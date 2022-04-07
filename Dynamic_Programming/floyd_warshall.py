# /**
#  * @author Vinay Ummadi
#  * @email ummadi.vinay2000@gmail.com
#  * @create date 2022-04-07 08:39:57
#  * @modify date 2022-04-07 08:39:57
#  * @desc [description]
#  */

from collections import OrderedDict
from mimetypes import init
import numpy as np
from math import  inf

G = {
    1 : {1: 0, 2 : 3, 4: 5},
    2 : {1 : 2, 2:0, 4: 4},
    3 : {2 : 1, 3:0},
    4 : {3 : 2, 4:0}
}
G = OrderedDict(G)
print("G: ", G)

n = len(G)
dist = np.zeros([n+1, n+1, n+1], dtype=np.float32)
# prev = [[[None for _ in range(n+1)]for _ in range(n+1)] for _ in range(n+1)]
# prev = np.asarray(prev)
prev = {}
# print("Prev: ", prev)

for i in range(1,n+1):
    for j in range(1,n+1):
        dist[0,i,j] = inf

for start in G:
    for end in G[start]:
        dist[0,start, end] = G[start][end]


for k in range(1,n+1):
    temp_min_key = {0:(k-1,i,j), 1:(k-1,i,k), 2:(k-1,k,j)}
    for i in range(1,n+1):
        for j in range(1,n+1):
            idx = np.argmin([dist[k-1,i,j], dist[k-1,i,k] + dist[k-1,k,j]])
            dist[k,i,j] = min([dist[k-1,i,j], dist[k-1,i,k] + dist[k-1,k,j]])
            prev[(k,i,j)] = temp_min_key[idx]


# print("Dist: ")
# print(dist)

# print("Prev: ")
# print(prev)

start_node = 1
end_node = 3
print(f"Shortest path length from {start_node} to {end_node}: {dist[n,start_node,end_node]}")
print(f"Shortest path from {start_node} to {end_node}: ")

intial = prev[(n,start_node,end_node)]
path = [end_node]
while intial[0] != 0:
    print(intial)
    intial = prev[intial]
    path.append(intial[1])
print(path)
    

