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
            for (v, w) in self.aList[vertex]:
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
    
    def mcst_prim(self):
        if len(self.edges()) == 0:
            return None
        
        visited = {}
        distance = {}
        mst = {}
        for vertex in self.aList:
            visited[vertex] = False
            distance[vertex] = float('inf')
            mst[vertex] = (-1, None)
        
        picked_v = self.vertices()[0]
        distance[picked_v] = 0

        for i in range(0, self.numVertices()):
            # Get the minimum distance of neighbours
            min_distance = min([distance[v] for v in self.aList if not visited[v]])

            # Find all vertices with that minimum distance that are not visited
            next_vertices = [v for v in self.aList if (not visited[v]) and (distance[v] == min_distance)]

            next_vertex = min(next_vertices)
            visited[next_vertex] = True

            for (v, w) in self.aList[next_vertex]:
                if not visited[v]:
                    if w < distance[v]:
                        mst[v] = (next_vertex, w)
                        distance[v] = w
        
        min_cost = 0
        for vertex in mst:
            if mst[vertex][1] != None:
                min_cost += mst[vertex][1]
    
        return (mst, min_cost)
    
    def mcst_kruskal(self):
        if len(self.edges()) == 0:
            return None
        
        # Create a disjoint set for each vertex
        components = {}
        for vertex in self.aList:
            components[vertex] = [vertex]
        
        mst = {}
        for vertex in self.aList:
            mst[vertex] = (-1, None)

        edgeList = self.edges()
        
        # Sort by weight
        edgeList.sort(key=lambda x: x[2])

        min_cost = 0
        for (u, v, w) in edgeList:
            # Insert into tree if it does not create a cycle. Try and trace components, you'll understand it's significance - Ashwin
            if components[u] != components[v]:
                # Add edge to mst
                mst[v] = (u, w)
                min_cost += w

                # Assign new component Leader
                new_leader = components[u]
                for vertex in self.aList:
                    if components[vertex] == new_leader:
                        components[vertex] = components[v]
        
        return (mst, min_cost)




edgeList = [('A', 'B', 1), ('A', 'D', 4), ('A', 'E', 3), ('B', 'E', 2), ('E', 'D', 4), ('B', 'D', 4), ('E', 'C', 4), ('E', 'F', 7), ('C', 'F', 5)]
# edgeList = [(0,1,10),(0,2,18),(1,2,6),(1,4,20),(2,3,70),(4,5,10),(4,6,10),(5,6,5)]
g = WeightedGraph()
for edge in edgeList:
    g.insertEdge(edge)

print("\n\n")
print("Adjacency List:", g.aList)

print("\n\n")
print("PRIM'S ALGORITHM")
print("Minimum Cost Spanning Tree:", g.mcst_prim()[0])
print("Minimum Cost:", g.mcst_prim()[1])

print("\n\n")
print("KRUSKAL'S ALGORITHM")
print("Minimum Cost Spanning Tree:", g.mcst_kruskal()[0])
print("Minimum Cost:", g.mcst_kruskal()[1])