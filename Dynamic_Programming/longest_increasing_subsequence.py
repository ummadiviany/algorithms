# /**
#  * @author Vinay Ummadi
#  * @email ummadi.vinay2000@gmail.com
#  * @create date 2022-04-07 11:01:51
#  * @modify date 2022-04-07 11:01:51
#  * @desc [description]
#  */

import numpy as np
from collections import defaultdict

seq = [5,2,8,6,3,6,9,7]
n = len(seq)

lis_graph = defaultdict(dict)
for i,val in enumerate(seq):
    for j,another_val in enumerate(seq[i:],i):
        if val < another_val:
            lis_graph[i][j] = True
        else:
            lis_graph[i][j] = False

# print("LIS graph: ", lis_graph)

# print(lis_graph[0][1])

L = np.zeros([n], dtype=np.float32)
prev = {}

for j in range(n):
    temp = [L[i] if lis_graph[i][j] else 0 for i in range(j)]
    if len(temp) > 0:
        max_idx = np.argmax(temp)
        if temp[max_idx] > 0:
            prev[j] = max_idx
        else:
            prev[j] = None 
    L[j] = 1 + temp[max_idx] if len(temp) > 0 else 0

print("Prev: ", prev)

print("LIS: ", L)

tmp = seq[-1]
path = []
while tmp:
    path.append(tmp)
    tmp = prev[tmp]
    

print("Path: ", end="")
print(*path[::-1], sep=" -> ")