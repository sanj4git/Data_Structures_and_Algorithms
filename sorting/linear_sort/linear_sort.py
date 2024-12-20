def linear_sort(L):
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if L[i] > L[j]:
                L[i], L[j] = L[j], L[i]
    
    return L

L = [3, 2, 1, 5, 4]
print(linear_sort(L))