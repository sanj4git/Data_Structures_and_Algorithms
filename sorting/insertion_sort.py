from random import randint

def insertionSort(A):
    for j in range(1, len(A)):
        i = j - 1
        key = A[j]

        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i -= 1

        A[i+1] = key

A = [randint(0, 100) for _ in range(10)]
print(A)
insertionSort(A)
print(A)
