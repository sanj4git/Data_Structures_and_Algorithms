"""
Logic to handle negative numbers in counting sort was referred from the below link:
https://www.ripublication.com/ijaer18/ijaerv13n1_28.pdf
"""
def counting_sort(L):
    if not L:
        return L
    largest = max(L)
    min_value = min(L)
    offset = -min_value if min_value<0 else 0
    n = len(L)
    frequencyArray = [0]*(largest+1+offset)
    for i in range(n):
     # shift of the element  by the offset which ensures negative numbers are shifted to non-negative indices in frequencyArray
        frequencyArray[L[i]+offset] = frequencyArray[L[i]+offset]+1
    #sorting part
    j = 0
    for i in range(len(frequencyArray)):
        while(frequencyArray[i]>0):
            L[j] = i - offset #restores our original numbers after sorting
            frequencyArray[i] = frequencyArray[i] - 1
            j+=1
    return L

L = [1, 4, 1, 3, 2, 4, 3, 7]
print(counting_sort(L))
#output: [1, 1, 2, 3, 3, 4, 4, 7]

L2 = [5,-4,-3,-2,4,7,9]
print(counting_sort(L2))
#output:[-4, -3, -2, 4, 5, 7, 9]

L3 = []
print(counting_sort(L3))
#output:[]

