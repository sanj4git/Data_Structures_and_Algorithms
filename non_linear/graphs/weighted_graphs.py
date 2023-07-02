class WeightedGraph:
    def __init__(self):
        self.aList = {}
        self.size = 0

    def isVertex(self, vertex):
        return vertex in self.aList

    def numVertices(self):
        return self.size

    def numEdges(self):
        return sum([len(self.aList[vertex]) for vertex in self.aList])

    def vertices(self):
        vertices = []
        for vertex in self.aList:
            vertices.append(vertex)
        return vertices

    def edges(self):
        edges = []
        for vertex in self.aList:
            for v, w in self.aList[vertex]:
                edges.append((vertex, v, w))
        return edges

    def insertVertex(self, vertex):
        if not self.isVertex(vertex):
            self.aList[vertex] = []
            self.size += 1
        else:
            print("Vertex already exists")

    def insertEdge(self, edge):
        u, v, w = edge
        if not self.isVertex(u):
            self.insertVertex(u)
        if not self.isVertex(v):
            self.insertVertex(v)

        if v not in self.aList[u] and u not in self.aList[v]:
            self.aList[u].append((v, w))
            self.aList[v].append((u, w))
        else:
            print("Invalid undirected edge")

    def insertDirectedEdge(self, edge):
        u, v, w = edge
        if not self.isVertex(u):
            self.insertVertex(u)
        if not self.isVertex(v):
            self.insertVertex(v)

        if v not in self.aList[u]:
            self.aList[u].append((v, w))
        else:
            print("Invalid directed edge")

    def removeVertex(self, vertex):
        if self.isVertex(vertex):
            for v in self.aList[vertex]:
                self.aList[v].remove(vertex)
            self.aList.pop(vertex)
            self.size -= 1
        else:
            print("Vertex does not exist")

    def removeEdge(self, edge):
        u, v = edge
        if self.isVertex(u) and self.isVertex(v):
            if v in self.aList[u]:
                self.aList[u].remove(v)
            if u in self.aList[v]:
                self.aList[v].remove(u)
            else:
                print("Invalid undirected edge")
        else:
            print("Invalid undirected edge")

    def isDijkstraSafe(self):
        edgeList = self.edges()
        for u, v, w in edgeList:
            if w < 0:
                return False
        return True

    def dijkstra(self, source):
        if not self.isDijkstraSafe():
            print("Graph is not Dijkstra safe")
            return

        if not self.isVertex(source):
            print("Invalid source vertex")
            return
        
        visited = {}
        for vertex in self.vertices():
            visited[vertex] = False
        
        distance = {}
        for vertex in self.vertices():
            distance[vertex] = float("inf")

        distance[source] = 0

        while False in visited.values():
            current_min_node = None
            for vertex in self.vertices():
                if not visited[vertex]:
                    if current_min_node is None:
                        current_min_node = vertex
                    elif distance[vertex] < distance[current_min_node]:
                        current_min_node = vertex
            
            for v, w in self.aList[current_min_node]:
                if distance[current_min_node] + w < distance[v]:
                    distance[v] = distance[current_min_node] + w

            visited[current_min_node] = True
        
        return distance


g = WeightedGraph()
edgeList = [
    (0, 1, 10),
    (0, 2, 80),
    (1, 2, 6),
    (1, 4, 20),
    (2, 3, 70),
    (4, 5, 50),
    (4, 6, 5),
    (5, 6, 10),
]
edgeList = [
    (1, 2, 7),
    (1, 6, 14),
    (1, 3, 9),
    (2, 1, 7),
    (2, 3, 10),
    (2, 4, 15),
    (3, 6, 2),
    (3, 1, 9),
    (3, 2, 10),
    (3, 4, 11),
    (4, 2, 15),
    (4, 3, 11),
    (4, 5, 6),
    (5, 4, 6),
    (5, 6, 9),
    (6, 1, 14),
    (6, 3, 2),
    (6, 5, 9)
]

for u, v, w in edgeList:
    g.insertDirectedEdge((u, v, w))

print("\n\n")
print("Adjacency List:", g.aList)
print("Number of vertices:", g.numVertices())
print("Number of edges:", g.numEdges())
print("Vertices:", g.vertices())
print("Edges:", g.edges())

print("\n\n")
print("Dijkstra:", g.dijkstra(1))
