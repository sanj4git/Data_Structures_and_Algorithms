class MinHeap:
    def __init__(self):
        self.heap = []
        self.size = 0
    
    def minHeapify(self, i):
        l = 2*i + 1
        r = 2*i + 2
        smallest = i
        if l < self.size and self.heap[l][0] < self.heap[i][0]:
            smallest = l
        if r < self.size and self.heap[r][0] < self.heap[smallest][0]:
            smallest = r
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.minHeapify(smallest)
    
    def buildMinHeap(self, A):
        self.heap = A
        self.size = len(A)
        for i in range(self.size//2, -1, -1):
            self.minHeapify(i)

    def extractMin(self):
        if self.size < 1:
            return None
        min = self.heap[0]
        self.heap[0] = self.heap[self.size-1]
        self.size -= 1
        self.minHeapify(0)
        return min
    
    def insert(self, key, value):
        self.heap.append((key, value))
        self.size += 1
        i = self.size-1
        while i > 0 and self.heap[(i-1)//2][0] > self.heap[i][0]:
            self.heap[i], self.heap[(i-1)//2] = self.heap[(i-1)//2], self.heap[i]
            i = (i-1)//2
    

def kruskal(G):
    E = [] # Edges
    C = {} # Components
    T = [] # MST

    for u in G:
        for v, w in G[u]:
            E.append((w, u, v))
        C[u] = u
    
    H = MinHeap()
    H.buildMinHeap(E)

    while H.size > 0:
        w, u, v = H.extractMin()
        if C[u] != C[v]:
            T.append((u, v, w))
            c = C[u]
            for w in G:
                if C[w] == c:
                    C[w] = C[v]

    return T

# def prim(n,adjacency_list):
#     q=[[0,0]] #starting node is 0 with 0 cost
#     mst=set()
#     cost=0
#     while len(mst)!=n:
#         q.sort()
#         node,weight=q.pop(0)
        
#         if node in mst:
#             continue
#         mst.add(node)
#         cost+=weight
#         for Weight,neighbor in adjacency_list[node]:
#             if neighbor not in mst:
#                 q.append([Weight,neighbor])
    
#     return cost

def prim(G):
    visited = {}
    d = {}
    T = []

    for u in G:
        visited[u] = False
        d[u] = float("inf")

    s = list(G.keys())[0]
    visited[s] = True
    for v, w in G[s]:
        d[v] = w
    
    for i in range(1, len(G)):
        min_dist = float("inf")
        next_vertex = None
        next_edge = None
        for u in G:
            for v, w in G[u]:
                if visited[u] and (not visited[v]) and w < min_dist:
                    min_dist = w
                    next_vertex = v
                    next_edge = (u, v, w)

        visited[next_vertex] = True
        T.append(next_edge)

        for v, w in G[next_vertex]:
            if not visited[v]:
                if w < d[v]:
                    d[v] = w

    return T
    
    




def extractMSTCost(T):
    return sum([w for u, v, w in T])

G = {
    0: [(1, 337), (2, 1235), (3, 2342)],
    1: [(0, 337), (2, 1464), (4, 1846), (7, 2704)],
    2: [(0, 1235), (1, 1464), (4, 802), (3, 1121), (6, 1391)],
    3: [(0, 2342), (2, 1121), (6, 1090), (5, 946), (7, 1258)],
    4: [(1, 1846), (2, 802), (6, 740), (5, 621), (7, 867), (8, 849)],
    5: [(3, 946), (4, 621), (6, 184)],
    6: [(2, 1391), (3, 1090), (4, 740), (5, 184), (7, 187), (8, 144)],
    7: [(1, 2704), (3, 1258), (4, 867), (6, 187)],
    8: [(4, 849), (6, 144)]
}


print("Kruskal")
T = kruskal(G)
print(T)
print(extractMSTCost(T))

print("Prim")
T = prim(G)
print(T)
print(extractMSTCost(T))