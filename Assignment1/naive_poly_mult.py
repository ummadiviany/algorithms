def naive_poly_mult(a,b):
    n1 = len(a)
    n2 = len(b)
    # if n1 >= n2:
    #     b += [0 for _ in range(n1-n2)]
    # else:
    #     a += [0 for _ in range(n2-n1)]
    a  += [0 for _ in range(n2-1)]
    b  += [0 for _ in range(n1-1)]
    c = [sum([a[i]*b[k-i] for i in range(k+1)]) for k in range(n1+n2-1)]

    return c

if __name__ == "__main__":
    A = [1,2,3]
    B = [2,1,4]
    print("A = ",A)
    print("B = ",B)
    print("Expected O/P : ",[2,5,12,11,12])
    print("Output : ",naive_poly_mult(A,B))