from random import randint

def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    L = [0 for i in range(n1)]
    R = [0 for i in range(n2)]

    for i in range(n1):
        L[i] = A[p+i]

    for i in range(n2):
        R[i] = A[q+i+1]

    i = 0
    j = 0
    
    for k in range(p, r + 1):
        if i < n1 and j < n2:
            if L[i] <= R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1

        elif i < n1:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


def mergeSort(A, p, r):
    if p < r:
        q = (p + r) // 2
        mergeSort(A, p, q)
        mergeSort(A, q+1, r)
        merge(A, p, q, r)

A = [randint(0, 100) for _ in range(10)]
print(A)
mergeSort(A, 0, len(A)-1)
print(A)