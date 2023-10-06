from random import randint

def partition(A, p, r):
    pivot_index = randint(p, r)
    if pivot_index != r:
        A[pivot_index], A[r] = A[r], A[pivot_index]

    pivot_index = r
    i = p - 1

    for j in range(p, r):
        if A[j] < A[pivot_index]:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i+1], A[pivot_index] = A[pivot_index], A[i+1]
    return i+1

def quickSort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quickSort(A, p, q-1)
        quickSort(A, q+1, r)


A = [randint(0, 100) for _ in range(10)]
print(A)
quickSort(A, 0, len(A)-1)
print(A)