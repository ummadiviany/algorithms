# /**
#  * @author Vinay Ummadi
#  * @email ummadi.vinay2000@gmail.com
#  * @create date 2022-04-02 15:08:07
#  * @modify date 2022-04-02 15:08:07
#  * @desc [description]
#  */

import numpy as np
from math import inf

def revised_simplex(A, Acap, bcap ):

    bcap_variables = np.repeat(None, bcap.shape[0])
    bcap_variables[-1] = "Z"
    # print("bcap_variabls: \n", bcap_variables)

    # Step 4 : Find Bcapinv = [B^-1   0
    #                          CbB^-1 1]
    # Find inverse of 
    # B^-1 = inv(B) = 
    #      = inv([[1 0], [0 1]])

    B = np.identity(A.shape[0], dtype=float)
    Binv = np.linalg.inv(B)

    # Cb = [0 0]
    Cb = np.array([0 for _ in range(A.shape[0])],dtype=float)
    Cb_Binv = np.matmul(Cb, Binv)

    add_col = np.zeros((Acap.shape[0], 1), dtype=float)
    add_col[-1] = 1
    # print("add_col: \n", add_col)

    Bcapinv = np.vstack((
        Binv,Cb_Binv)
    )

    Bcapinv = np.hstack((Bcapinv, add_col))

    print("Bcapinv: \n", Bcapinv)
    c = 0
    while True:
        if c > 5:
            print("Max iterations reached.. Breaking...")
            break
        print(f"\n--------------Iteration {c+1} -----------------\n")
        # Step 5: Find (CbB^-1) x Acap ; (CbB^-1) = last row of Bcapinv
        zjcj = np.matmul(Bcapinv[-1], Acap)
        # print("zjcj: \n", zjcj)
        if all(zjcj >= 0):
            print("\n--------------Optimal solution found---------------------\n")

            XBcap = np.matmul(Bcapinv, bcap)
            bcap_variables = np.reshape(bcap_variables, XBcap.shape)
            result_coeff = np.hstack((bcap_variables, XBcap)) 
            print("Coefficients: \n", result_coeff)
            return result_coeff
        else:
            print("\n--------------Optimal solution not, Iterating the process---------------------\n")
            # Column with most negative element
            p_col = list(zjcj).index(min(zjcj[zjcj<0]))
            print("Most negative column: ", p_col+1)

            entering_variable = f"X{p_col+1}"
            print(entering_variable, "enters the basis")

            # Step 6 : Find Xkcap = Bcapinv x Akcap ; Akcap is column of A with index k.
            acap = np.reshape(Acap[:,p_col],(Acap.shape[0],1))
            Xkcap = np.matmul(Bcapinv, acap)
            # print("Xkcap: \n", Xkcap)
            if all(Xkcap <= 0):
                print("Unbounded solution")
                break
            else:
                XBcap = np.matmul(Bcapinv, bcap)
                # print("XBcap: \n", XBcap)

                # Step 7 : Revised simplex table ratio test
                # Ration of XBcap/Xkcap where Xkcap is positive.
                ratio = [x/y if x>0 and y>0 else inf for x,y in zip(XBcap, Xkcap)]
                # print("ratio: \n", ratio)
                min_row_idx = ratio.index(min(ratio))
                print("Minimum Ratio Row: ", min_row_idx+1)
                leaving_variable = "S"+str(min_row_idx+1) if min_row_idx+1<=A.shape[0] else "Z"
                print(leaving_variable, "leaves the basis")

                # Storing entring and leaving variables
                bcap_variables[min_row_idx] = entering_variable

                key_ele = Xkcap[min_row_idx].item()
                print("Key element: ", key_ele)

                # Step 8 : Update Bcapinv
                # Row matrix transformation
                # Make key element 1 and other elements zero
                Bcapinv[min_row_idx,:] = Bcapinv[min_row_idx,:]/key_ele

                for i in range(len(Acap)):
                    if i != min_row_idx:
                        Bcapinv[i,:] -= Xkcap[i].item() * Bcapinv[min_row_idx,:]

                # print("Bcapinv: \n", Bcapinv)

                c += 1


if __name__ == '__main__':
    # Step 1 : Convert into standard form
    # obj function
    #  max z = 6x1 - 2x2 + 3x3 + 0s1 + 0s2


    # subject to conditions
    # 2x1 - 1x2 + 2x3 + 1s1 <= 2
    # x1 + 0x2 + 4x3 + 1s2<= 4
    # x1, x2, x3 >= 0

    # Step 2 : Find the initial basis solution with B = I(n x n)
    # keep x1, x2, x3 zeros in all equation and find slack variables values 
    # s1 = 2 and s2 = 4


    # Step 3 : Find the below variables and their values
                # Z = Cx, Ax=b, Acap = [A -C]', bcap = [b 0]'
                #  Finda A,b,C,Acap,bcap


    # A = np.array([
    #     [2, -1,  2,  1,  0],
    #     [1,  0,  4,  0,  1]
    # ], dtype=float)

    
    A = np.array([
        [2,  3],
        [-3, 2],
        [0,  2],
        [2,  1]
    ],dtype=float)

    num_variables = A.shape[1]
    
    I = np.identity(A.shape[0], dtype=float)
    A = np.hstack((A, I))
    print("A: \n", A)

    

    # C = np.array([6, -2, 3, 0, 0],dtype=float)
    C = np.array([4, 3])
    C = np.hstack((C, np.zeros(A.shape[0], dtype=float)))
    print("C: \n", C)
    
    b = np.array([[6], [3], [5], [4]],dtype=float)
    # b = np.transpose(b)
    print("b \n", b)
    
    Acap = np.vstack((A,C))
    Acap[-1] = -1 * Acap[-1]
    print("Acap: \n", Acap)

    bcap = np.vstack((b,[0]))
    # bcap = np.transpose(bcap)
    print("bcap: \n", bcap)

    result_coeffecients = revised_simplex(A, Acap, bcap)
    result_dict = dict(result_coeffecients)
    
    print("Optimal solution with coefficients: ")
    
    print("Obejective function: Z = 4*X1  + 3*X2")
    print(f"Obejective function: Z = 4*{result_dict['X1']} + 3*{result_dict['X2']} = {result_dict['Z']}")
    print("Maxmimum value of objective function: ", result_dict['Z'])

