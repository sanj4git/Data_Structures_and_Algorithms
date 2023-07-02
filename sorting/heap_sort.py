class MinHeap:
    def __init__(self):
        self.heap = []

    def heapify(self, i):
        l = 2*i + 1
        r = 2*i + 2
        smallest = i

        if l < len(self.heap) and self.heap[l] < self.heap[smallest]:
            smallest = l
        if r < len(self.heap) and self.heap[r] < self.heap[smallest]:
            smallest = r
        
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify(smallest)

    def build_heap(self, arr):
        self.heap = arr
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self.heapify(i)
    
    def insert(self, data):
        self.heap.append(data)
        i = len(self.heap) - 1

        while i > 0:
            parent = (i - 1) // 2
            if self.heap[i] < self.heap[parent]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                i = parent
            else:
                break
        
    def extract_min(self):
        if len(self.heap) == 0:
            return None
        
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        heap_min = self.heap.pop()
        self.heapify(0)

        return heap_min
    
    def delete(self, data):
        if len(self.heap) == 0:
            return None
        
        i = self.heap.index(data)
        self.heap[i], self.heap[-1] = self.heap[-1], self.heap[i]
        self.heap.pop()
        self.heapify(i)

    
    def __str__(self):
        return str(self.heap)

class MaxHeap:
    def __init__(self):
        self.heap = []

    def heapify(self, i):
        l = 2*i + 1
        r = 2*i + 2
        largest = i

        if l < len(self.heap) and self.heap[l] > self.heap[largest]:
            largest = l
        if r < len(self.heap) and self.heap[r] > self.heap[largest]:
            largest = r
        
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.heapify(largest)

    def build_heap(self, arr):
        self.heap = arr
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self.heapify(i)
    
    def insert(self, data):
        self.heap.append(data)
        i = len(self.heap) - 1

        while i > 0:
            parent = (i - 1) // 2
            if self.heap[i] > self.heap[parent]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                i = parent
            else:
                break
        
    def extract_max(self):
        if len(self.heap) == 0:
            return None
        
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        heap_max = self.heap.pop()
        self.heapify(0)

        return heap_max
    
    def delete(self, data):
        if len(self.heap) == 0:
            return None
        
        i = self.heap.index(data)
        self.heap[i], self.heap[-1] = self.heap[-1], self.heap[i]
        self.heap.pop()
        self.heapify(i)

    
    def __str__(self):
        return str(self.heap)
    

def heapSortMin(A):
    heap = MinHeap()
    heap.build_heap(A)
    sorted_arr = []
    for _ in range(len(A)):
        sorted_arr.append(heap.extract_min())
    return sorted_arr

def heapSortMax(A):
    heap = MaxHeap()
    heap.build_heap(A)
    sorted_arr = []
    for _ in range(len(A)):
        sorted_arr.append(heap.extract_max())
    return sorted_arr


L = [i for i in range(100, 0, -1)]
print("Min Heap Sort:", heapSortMin(L))

L = [i for i in range(100, 0, -1)]
print("Max Heap Sort:", heapSortMax(L))