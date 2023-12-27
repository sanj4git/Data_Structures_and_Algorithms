"""
Given an array of N elements, find the kth smallest element in the array.
"""

def partition(arr, l, r):
    pivot = arr[r]
    i = l - 1
    for j in range(l, r):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i + 1

def kth_smallest(arr, l, r, k):
    if k > 0 and k <= r - l + 1:
        pos = partition(arr, l, r)
        if pos - l == k - 1:
            return arr[pos]
        if pos - l > k - 1:
            return kth_smallest(arr, l, pos - 1, k)
        return kth_smallest(arr, pos + 1, r, k - pos + l - 1)

    return None

A = [7, 10, 4, 3, 20, 15]
k = 3
print(kth_smallest(A, 0, len(A) - 1, k))

A = [7, 10, 4, 20, 15]
k = 4
print(kth_smallest(A, 0, len(A) - 1, k))