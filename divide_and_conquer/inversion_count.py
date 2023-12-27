"""
For all i & j < size of array, if i < j then count number of pairs (A[i],A[j]) such that A[j] < A[i].
"""

def merge(A, l, mid, r):
    n1 = mid - l + 1
    n2 = r - mid

    L = []
    R = []

    for i in range(n1):
        L.append(A[l + i])

    for j in range(n2):
        R.append(A[mid + 1 + j])

    i = 0
    j = 0
    k = l

    inv_count = 0

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
            inv_count += (mid - i)

        k += 1

    while i < n1:
        A[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        A[k] = R[j]
        j += 1
        k += 1

    return inv_count

def merge_sort(A, l, r):
    inv_count = 0

    if l < r:
        mid = (l + (r - 1)) // 2

        inv_count += merge_sort(A, l, mid)
        inv_count += merge_sort(A, mid + 1, r)
        inv_count += merge(A, l, mid, r)

    return inv_count

def count_inversions(A):
    return merge_sort(A, 0, len(A) - 1)

A = [5, 4, 3, 2, 1]
print(count_inversions(A))