#### Q1. Recursive mergesort:
 a. We have seen in coding tutorial 2 that the mergesort algorithm is a recursive procedure that has three main sub-routines: **merge**, **mergesort** and **split**. In the tutorial the merge subroutine was iterative. **Implement mergesort algorithm such that both mergesort and merge are recursive procedures**.
b. Implement **insertion sort**. Read: https://en.wikipedia.org/wiki/Insertion_sort .
c. Compare the **running time of insertion sort with mergesort** using absolute running times
of your codes on the same inputs.

#### Instructions for execution:
*test_merge_sort.py*  and *test_insertion_sort.py* contains 7 tests each for testing **merge_sort()** and **insertion_sort()** functions.

Open the terminal in the current folder and run

```
python test_merge_sort.py
```

```
python test_insertion_sort.py
```
You can also alternatively run 
```
python insertion_sort.py
```

```
python merge_sort.py
```
**Expected output** : All test cases passed

#### Q2. Inverse Fast Fourier Transform (IFFT):
a. Design a function called **poly_mult** which takes in two polynomials as input and
returns the result in coefficient form. Use the most naive algorithm taking O(n2) time.

b. Design a function **ifft** to perform inverse fourier transform.

c. Use the fft function to perform polynomial multiplication in the value representation
domain. Then use the ifft function to return to the coefficient domain. Show that it
obtains the same result as (a) but in a fraction of its time.

#### Instructions for execution:
*test_fft_poly_mult.py* contains 3 tests each for testing **fft_poly_mult()** function.

Open the terminal in the current folder and run


```
python naive_poly_mult.py
```

```
python test_fft_poly_mult.py
```


**Expected output** : All test cases passed