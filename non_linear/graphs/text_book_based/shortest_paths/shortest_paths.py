class PriorityQueue:
    def __init__(self):
        self.queue = []
        self.size = 0

    def min_heapify(self, i):
        l = 2*i + 1
        r = 2*i + 2
        smallest = i
        if l < self.size and self.queue[l][0] < self.queue[i][0]:
            smallest = l
        if r < self.size and self.queue[r][0] < self.queue[smallest][0]:
            smallest = r
        if smallest != i:
            self.queue[i], self.queue[smallest] = self.queue[smallest], self.queue[i]
            self.min_heapify(smallest)
    
    def insert(self, key, value):
        self.queue.append((key, value))
        self.size += 1
        i = self.size-1
        while i > 0 and self.queue[(i-1)//2][0] > self.queue[i][0]:
            self.queue[i], self.queue[(i-1)//2] = self.queue[(i-1)//2], self.queue[i]
            i = (i-1)//2

    def build_min_heap(self, A):
        self.queue = A
        self.size = len(A)
        for i in range(self.size//2, -1, -1):
            self.min_heapify(i)
    
    def extract_min(self):
        if self.size < 1:
            return None
        min = self.queue[0]
        self.queue[0] = self.queue[self.size-1]
        self.size -= 1
        self.min_heapify(0)
        return min
        

def dijkstra(G, v):
    d = {}
    for u in G:
        d[u] = float("inf")
    
    d[v] = 0
    Q = PriorityQueue()
    Q.build_min_heap([(d[u], u) for u in G])
    
    while Q.size > 0:
        _, u = Q.extract_min()
        for v, w in G[u]:
            if d[v] > d[u] + w:
                d[v] = d[u] + w
                Q.insert(d[v], v)

    return d

def bellmann_ford(G, v):
    """
    Relax all edges |V|-1 times
    """
    d = {}
    for u in G:
        d[u] = float("inf")
    
    d[v] = 0
    for i in range(len(G)-1):
        for u in G:
            for v, w in G[u]:
                if d[v] > d[u] + w:
                    d[v] = d[u] + w

    return d

# DAG
def topologicalSort(G):
    in_degree = {}
    zero_degree_queue = []
    topologically_sorted_list = []

    for u in G:
        in_degree[u] = 0
    
    for u in G:
        for (v, w) in G[u]:
            in_degree[v] += 1

    for u in G:
        if in_degree[u] == 0:
            zero_degree_queue.append(u)
    
    while len(zero_degree_queue) > 0:
        u = zero_degree_queue.pop(0)
        topologically_sorted_list.append(u)
        in_degree[u] -= 1

        for (v, w) in G[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                zero_degree_queue.append(v)

    return topologically_sorted_list

def isDAG(G):
    """
    Returns True if the graph G is a DAG, False otherwise.
    """
    return len(topologicalSort(G)) == len(G)


def shortest_path_dag(G, s):
    if not isDAG(G):
        return "Graph is not a DAG."
    topologically_sorted_list = topologicalSort(G)
    d = {}
    for u in G:
        d[u] = float("inf")
    d[s] = 0
    for u in topologically_sorted_list:
        for v, w in G[u]:
            if d[v] > d[u] + w:
                d[v] = d[u] + w
    return d

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

print("Dijkstra")
print(dijkstra(G, "BWI"))

print("\nBellmann-Ford")
print(bellmann_ford(G, "BWI"))

print("\nShortest path in DAG")
print(shortest_path_dag(G, "BWI"))

G = {
    "a": [("b", 1), ("c", 4)],
    "b": [("c", 2), ("d", 6)],
    "c": [("d", 3)],
    "d": []
}

print("\nShortest path in DAG")
print(shortest_path_dag(G, "a"))