#### Q1. Recursive mergesort:
 a. We have seen in coding tutorial 2 that the mergesort algorithm is a recursive procedure that has three main sub-routines: **merge**, **mergesort** and **split**. In the tutorial the merge subroutine was iterative. **Implement mergesort algorithm such that both mergesort and merge are recursive procedures**.
b. Implement **insertion sort**. Read: https://en.wikipedia.org/wiki/Insertion_sort .
c. Compare the **running time of insertion sort with mergesort** using absolute running times
of your codes on the same inputs.

#### Q2. Inverse Fast Fourier Transform (IFFT):
a. Design a function called **poly_mult** which takes in two polynomials as input and
returns the result in coefficient form. Use the most naive algorithm taking O(n2) time.

b. Design a function **ifft** to perform inverse fourier transform.

c. Use the fft function to perform polynomial multiplication in the value representation
domain. Then use the ifft function to return to the coefficient domain. Show that it
obtains the same result as (a) but in a fraction of its time.