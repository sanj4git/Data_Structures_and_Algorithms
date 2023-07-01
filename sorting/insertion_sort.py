def insertion_sort(L):
    if len(L) <= 1:
        return L
    
    for j in range(1, len(L)):
        key = L[j]
        i = j - 1
        while i >= 0 and L[i] > key:
            L[i + 1] = L[i]
            i -= 1
        L[i + 1] = key
    
    return L

L = [3, 2, 1, 5, 4]
print(insertion_sort(L))