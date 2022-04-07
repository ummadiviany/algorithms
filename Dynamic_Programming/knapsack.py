# /**
#  * @author Vinay Ummadi
#  * @email ummadi.vinay2000@gmail.com
#  * @create date 2022-04-07 10:26:58
#  * @modify date 2022-04-07 10:26:58
#  * @desc [description]
#  */

from math import inf
import numpy as np
items = {
    6 : 30,
    3 : 14,
    4 : 16,
    2 : 9
}

# max knapsack capacity
W = 20

# optimal knapsack value for weight W array
n = len(items)
K = np.zeros(W+1, dtype=np.float32)
K[0] = 0
bag = {}

for w in range(1, W+1):
    for wi in items:
        if wi <= w:
            K[w] = max(K[w], K[w-wi] + items[wi])

    temp = {wi:K[w-wi] + items[wi] for wi in items if wi <= w}
    if len(temp) > 0:
        max_key = max(temp, key=temp.get)
        K[w] = temp[max_key]
        bag[w] = max_key

print("Knaapsack optimal list :", K)
print("Optimal knapsack value: ", K[W])

print("Items added to knapsack : ", bag)

while W > 0:
    if bag[W] in bag:
        print(f"{bag[W]} : {items[bag[W]]}")
        W -= bag[W]
    else:
        break
