import math
def counting_sort(L):
    largest = -math.inf
    n = len(L)
    for i in range(n):
        if largest < L[i]:
            largest = L[i]
    frequencyArray = [0]*(largest+1)
    for i in range(n):
        frequencyArray[L[i]] = frequencyArray[L[i]]+1
    #sorting part
    j = 0
    for i in range(len(frequencyArray)):
        while(frequencyArray[i]>0):
            L[j] = i
            frequencyArray[i] = frequencyArray[i] - 1
            j+=1
    return L

L = [1, 4, 1, 3, 2, 4, 3, 7]
print(counting_sort(L))
#output: [1, 1, 2, 3, 3, 4, 4, 7]

