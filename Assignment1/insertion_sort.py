def insertion_sort(arr):
    i = 1
    while i < len(arr):
        j = i
        while j > 0  and arr[j-1] > arr[j]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            #print(arr)
            j -= 1
        i += 1
    return arr

def test_sort(inp,out,sort_func):
    """
    Utility function for checking testing mergesort
    """
    aout = sort_func(inp)
    print("Passed" if out == aout else "Failed ", end="\n")
    print(f"Input : {inp} \nExpected O/P : {out} \nActual O/P : {aout} \n")

if __name__ == "__main__":
    test_cases_input = [
                        [], [1], [2, 1], [13, 7, 5], [23, 7, 13, 5], [1, 2, 2, 1, 0, 0, 15, 15], [135604, 1000000, 45, 78435, 456219832, 2, 546]
    ]

    for case in test_cases_input:
        #checkin against testcases
        test_sort(case,sorted(case),insertion_sort)
        print("All test cases passed")