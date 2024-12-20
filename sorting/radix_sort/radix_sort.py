from random import randint

def insertionSort(A):
    for j in range(len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i -= 1
        A[i+1] = key

def radixSort(A):
    negative_A = []
    positive_A = []

    for i in range(len(A)):
        if A[i] < 0:
            negative_A.append(-A[i])
        else:
            positive_A.append(A[i])
    
    if len(negative_A) != 0:
        max_NA = max(negative_A)
        max_digits_NA = len(str(max_NA))

        buckets_NA = [[] for _ in range(10)]

        for digit in range(max_digits_NA):
            for num in negative_A:
                index = (num // (10 ** digit)) % 10
                buckets_NA[index].append(num)

            negative_A.clear()
            for bucket in buckets_NA:
                insertionSort(bucket)
                negative_A.extend(bucket)
                bucket.clear()

    if len(positive_A) != 0:
        max_PA = max(positive_A)
        max_digits_PA = len(str(max_PA))

        buckets_PA = [[] for _ in range(10)]

        for digit in range(max_digits_PA):
            for num in positive_A:
                index = (num // (10 ** digit)) % 10
                buckets_PA[index].append(num)

            positive_A.clear()
            for bucket in buckets_PA:
                insertionSort(bucket)
                positive_A.extend(bucket)
                bucket.clear()

    A.clear()

    for i in range(len(negative_A) - 1, -1, -1):
        negative_A[i] = -negative_A[i]
        A.append(negative_A[i])

    for i in range(len(positive_A)):
        A.append(positive_A[i])

    return A

A = [randint(-100, 100) for _ in range(10)]
print(A)
print(radixSort(A))