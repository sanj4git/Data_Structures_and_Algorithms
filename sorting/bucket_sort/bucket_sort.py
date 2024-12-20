from random import randint

def insertionSortForBucket(A):
    if len(A) <= 1:
        return A
    
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i -= 1

        A[i+1] = key

    return A


def bucketSort(A):
    n = len(A)
    B = [[] for i in range(n)]

    for i in range(n):
        index = min(n*A[i] // max(A), n - 1)
        B[index].append(A[i])

    for i in range(n):
        B[i] = insertionSortForBucket(B[i])

    k = 0
    for i in range(n):
        for j in range(len(B[i])):
            A[k] = B[i][j]
            k += 1


A = [randint(0, 100) for _ in range(10)]
print(A)
bucketSort(A)
print(A)
    
