def selection_sort(L):
    if len(L) <= 1:
        return L
    
    for i in range(len(L)):
        min_index = i
        for j in range(i+1, len(L)):
            if L[min_index] > L[j]:
                min_index = j
        L[i], L[min_index] = L[min_index], L[i]
    
    return L

L = [3, 2, 1, 5, 4]
print(selection_sort(L))