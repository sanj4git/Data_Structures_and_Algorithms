"""
NASA wants to link n stations spread over the country using communication channels. Each pair of stations has a different bandwidth available, which is known a priori. NASA wants to select n-1 channels (the minimum possible) in such a way that all the stations are linked by the channels and the total bandwidth (defined as the sum of the individual bandwidths of the channels) is maximum. Give an efficient algorithm for this problem and determine its worst-case time complexity. Consider the weighted graph G = (V,E), where V is the set of stations and E is the set of channels between the stations. Define the weight w(e) of an edge e in E as the bandwidth of the corresponding channel.
"""


class MaxHeapForKruskal:
    def __init__(self):
        self.heap = []
        self.size = 0
    
    def maxHeapify(self, i):
        l = 2*i + 1
        r = 2*i + 2
        largest = i
        if l < self.size and self.heap[l][0] > self.heap[i][0]:
            largest = l
        if r < self.size and self.heap[r][0] > self.heap[largest][0]:
            largest = r
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.maxHeapify(largest)
    
    def buildMaxHeap(self, A):
        self.heap = A
        self.size = len(A)
        for i in range(self.size//2, -1, -1):
            self.maxHeapify(i)

    def extractMax(self):
        if self.size < 1:
            return None
        max = self.heap[0]
        self.heap[0] = self.heap[self.size-1]
        self.size -= 1
        self.maxHeapify(0)
        return max
    

def maxSpanningTree(G):
    E = [] # Edges
    C = {} # Components
    T = [] # MST

    for u in G:
        for v, w in G[u]:
            E.append((w, u, v))
        C[u] = u
    
    H = MaxHeapForKruskal()
    H.buildMaxHeap(E)

    while H.size > 0:
        w, u, v = H.extractMax()
        if C[u] != C[v]:
            T.append((u, v, w))
            c = C[u]
            for w in G:
                if C[w] == c:
                    C[w] = C[v]

    return T

def extractMSTCost(T):
    return sum([w for u, v, w in T])

G = {
    "LAX": [("SFO", 337), ("DFW", 1235), ("MIA", 2342)],
    "SFO": [("LAX", 337), ("DFW", 1464), ("ORD", 1846), ("BOS", 2704)],
    "DFW": [("LAX", 1235), ("SFO", 1464), ("ORD", 802), ("MIA", 1121), ("JFK", 1391)],
    "MIA": [("LAX", 2342), ("DFW", 1121), ("JFK", 1090), ("BWI", 946), ("BOS", 1258)],
    "ORD": [("SFO", 1846), ("DFW", 802), ("JFK", 740), ("BWI", 621), ("BOS", 867), ("PVD", 849)],
    "BWI": [("MIA", 946), ("ORD", 621), ("JFK", 184)],
    "JFK": [("DFW", 1391), ("MIA", 1090), ("ORD", 740), ("BWI", 184), ("BOS", 187), ("PVD", 144)],
    "BOS": [("SFO", 2704), ("MIA", 1258), ("ORD", 867), ("JFK", 187)],
    "PVD": [("ORD", 849), ("JFK", 144)]
}

print(maxSpanningTree(G))
print(extractMSTCost(maxSpanningTree(G)))
