from random import randint

def maxHeapify(A, i, heap_size):
    l = 2 * i + 1
    r = 2 * i + 2

    if l < heap_size and A[l] > A[i]:
        largest = l
    else:
        largest = i

    if r < heap_size and A[r] > A[largest]:
        largest = r

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        maxHeapify(A, largest, heap_size)

def buildMaxHeap(A, heap_size):
    for i in range(heap_size//2, -1, -1):
        maxHeapify(A, i, heap_size)

def heapSort(A, heap_size):
    buildMaxHeap(A, heap_size)

    for i in range(heap_size-1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heap_size -= 1
        maxHeapify(A, 0, heap_size)

A = [randint(0, 100) for _ in range(10)]
print(A)
heapSort(A, len(A))
print(A)