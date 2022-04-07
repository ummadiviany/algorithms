# /**
#  * @author Vinay Ummadi
#  * @email ummadi.vinay2000@gmail.com
#  * @create date 2022-04-07 07:41:27
#  * @modify date 2022-04-07 07:41:27
#  * @desc [description]
#  */

import numpy as np

matsize = dict()
matsize[1] =  (50,20)
matsize[2] =  (20,1)
matsize[3] =  (1,10)
matsize[4] =  (10,100)
# print("Matrx size", matsize)

n = len(matsize)
C = np.zeros([n+1,n+1], dtype=np.int32)
optimal_k = {}

# print("C: ", C)

for i in range(n+1):
    C[i, i] = 0

print("C: ", C)

for s in range(1,n-1+1):
    print("S: ", s)
    for i in range(1, n-s+1):
        print("I: ", i)
        j = i + s
        print("J: ", j)
        temp = [C[i, k] + C[k+1, j] + matsize[i][0]*matsize[k][1]*matsize[j][1] for k in range(i,j)]
        min_k = np.min(temp)
        print("Min k: ", min_k)
        C[i, j] = min_k
        optimal_k[(i,j)] = i + temp.index(min_k)

print("C: ")
print(C)
print("Optimal cost: ", C[1,n])

print("Optimal k: ", optimal_k)