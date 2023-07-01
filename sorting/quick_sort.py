import random

def quick_sort_extra_space(L):
    if len(L) <= 1:
        return L
    
    pivot = random.choice(L)
    left = []
    right = []
    equal = []

    for i in L:
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)
        else:
            equal.append(i)
    
    return quick_sort_extra_space(left) + equal + quick_sort_extra_space(right)

def partition(L, left, right):
    pivot_index = random.randint(left, right)
    pivot = L[pivot_index]
    L[pivot_index], L[right] = L[right], L[pivot_index]

    i = left - 1
    for j in range(left, right):
        if L[j] <= pivot:
            i += 1
            L[i], L[j] = L[j], L[i]
        
    L[i+1], L[right] = L[right], L[i+1]

    return i + 1


def quick_sort(L, left, right):
    if left < right:
        pivot_index = partition(L, left, right)
        quick_sort(L, left, pivot_index - 1)
        quick_sort(L, pivot_index + 1, right)

L = [i for i in range(100, 0, -1)]

print("[Extra Space] Before sorting: ", L)
print("[Extra Space] After sorting: ", quick_sort_extra_space(L))

print("[In-place] Before sorting: ", L)
quick_sort(L, 0, len(L)-1)
print("[In-place] After sorting: ", L)