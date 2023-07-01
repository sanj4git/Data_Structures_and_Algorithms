def merge(L, left, mid, right):
    left_size = mid - left + 1
    right_size = right - mid
    
    left_array = [0 for _ in range(left_size)]
    right_array = [0 for _ in range(right_size)]

    for i in range(left_size):
        left_array[i] = L[left + i]

    for i in range(right_size):
        right_array[i] = L[mid + 1 + i]
    
    i = 0
    j = 0
    k = left

    while (i < left_size) and (j < right_size):
        if left_array[i] <= right_array[j]:
            L[k] = left_array[i]
            i += 1
        else:
            L[k] = right_array[j]
            j += 1
        k += 1
        
    while i < left_size:
        L[k] = left_array[i]
        i += 1
        k += 1

    while j < right_size:
        L[k] = right_array[j]
        j += 1
        k += 1

def merge_sort(L, left, right):
    if len(L) <= 1:
        return L
    
    if left < right:
        mid = (left + right) // 2
        merge_sort(L, left, mid)
        merge_sort(L, mid+1, right)
        merge(L, left, mid, right)

L = [i for i in range(10000, 0, -1)]
merge_sort(L, 0, len(L)-1)
print(L)
