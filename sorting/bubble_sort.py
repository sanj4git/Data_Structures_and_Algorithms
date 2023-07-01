def bubble_sort(L):
    if len(L) <= 1:
        return L
    
    for i in range(len(L)):
        for j in range(len(L)):
            if L[i] < L[j]:
                L[i], L[j] = L[j], L[i]
    
    return L

L = [3, 2, 1, 5, 4]
print(bubble_sort(L))