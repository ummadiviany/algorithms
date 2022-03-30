import numpy as np
from math import inf

def piv_col_zero(A, p_row, p_col):
    for i in range(len(A)):
        if i != p_row:
            zero_ele = A[i][p_col]
            A[i] = A[i] - zero_ele*A[p_row]
    return A


def simplex_tabular(A):
    # c = 0
    while any([1 for ele in A[-1] if ele<0]):
        print("\n---------New iteration---------------\n")
        # Step 1
        # Find most negative column in last row 
        # (i.e. the column with the most negative element in the last row) 
        row = A[-1]
        p_col = list(row).index(min(row[row<0]))
        print("pivot column: ", p_col)

        # Step 2
        # Ratio test for each row
        # Find smallest non-negative of the ratios
        # If all ratios are negative, then the problem is unbounded

        p_row_temp = [A[i][-1]/A[i][p_col] if (A[i][p_col] > 0) and (A[i][-1] > 0) else inf for i in range(len(A)-1)]
        print("Ratio test vals: ", p_row_temp)
        if all([x<0 for x in p_row_temp]):
            print("All ratios are negative. The problem is unbounded")
            break
        print("Moving ahead with ratio test for minimum")
        p_row = np.argmin([x for x in p_row_temp if x > 0])
        print("pivot row: ", p_row)

        # Step 3
        # Pivot element is located by pivot column and row
        # Make pivot element 1 by dividing with the pivot element
        # Make all elements in pivot column 0 by elemtary operations with pivot row

        pivot_element = A[p_row][p_col]
        print("pivot element: ", pivot_element)
        
        A[p_row] = A[p_row]/pivot_element
        print("pivot row: ", A[p_row])


        A = piv_col_zero(A, p_row, p_col)
        print("Modified A: ")
        print(A)

        print("\n--------------Iteration complete-----------------\n")
        
        # c += 1
        # if c > 2:
        #     break

    print("\n--------------Optimal Solution Reached-----------------\n")

    return A
if __name__ == '__main__':
    # A = np.array([[1,3,2,1,0,0,10], 
    #             [1,5,1,0,1,0,8], 
    #             [-8,-10,-7,0,0,1,0]], dtype=float)

    A  = np.array(
        [
            [2,3,1,0,0,0,0,6],
            [-3,2,0,1,0,0,0,3],
            [0,2,0,0,1,0,0,5],
            [2,1,0,0,0,1,0,4],
            [-4,-3,0,0,0,0,1,0]
        ], dtype=float)



    print(A)

    A = simplex_tabular(A)
    print("Optimal objective value: ", A[-1][-1])
    