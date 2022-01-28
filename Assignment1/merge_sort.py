from insertion_sort import test_sort

def merge(x,y):
    if len(x) == 0:
        return y
    if len(y) == 0:
        return x
    if x[0] <= y[0]:
        # recursively concatenating 
        return [x[0]] + merge(x[1:], y)
    else:
        return [y[0]] + merge(x, y[1:])


def merge_sort(a):
    n = len(a)
    if n > 1:
        # recursive division
        return merge(merge_sort(a[:n//2]), merge_sort(a[n//2:]))
    else:
        return a

if __name__ == "__main__":
    test_cases_input = [
                        [], [1], [2, 1], [13, 7, 5], [23, 7, 13, 5], [1, 2, 2, 1, 0, 0, 15, 15], [135604, 1000000, 45, 78435, 456219832, 2, 546]
    ]

    for case in test_cases_input:
        #checkin against testcases
        test_sort(case,sorted(case),merge_sort)
        print("All test cases passed")