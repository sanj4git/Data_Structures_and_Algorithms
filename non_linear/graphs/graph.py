class Graph:
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
            for v in self.aList[vertex]:
                edges.append((vertex, v))
        return edges
    
    def sortAdjacencyList(self):
        # Sort keys
        self.aList = dict(sorted(self.aList.items()))
        # Sort values
        for vertex in self.aList:
            self.aList[vertex].sort()
    
    def insertVertex(self, vertex):
        if not self.isVertex(vertex):
            self.aList[vertex] = []
            self.size += 1
        else:
            print("Vertex already exists")

    def insertEdge(self, edge):
        u, v = edge
        if not self.isVertex(u):
            self.insertVertex(u)
        if not self.isVertex(v):
            self.insertVertex(v)
        
        if v not in self.aList[u]:
            self.aList[u].append(v)
        else:
            print(f"Edge ({u}, {v}) already exists")
        if u not in self.aList[v]:
            self.aList[v].append(u)
        else:
            print(f"Edge ({v}, {u}) already exists")
    
    def insertDirectedEdge(self, edge):
        u, v = edge
        if not self.isVertex(u):
            self.insertVertex(u)
        if not self.isVertex(v):
            self.insertVertex(v)
        
        if v not in self.aList[u] and u not in self.aList[v]:
            self.aList[u].append(v)
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
            print("Edge does not exist")
    
    def incidentEdges(self, vertex):
        if self.isVertex(vertex):
            return [(vertex, v) for v in self.aList[vertex]]
        else:
            print("Vertex does not exist")
    
    def degree(self, vertex):
        if self.isVertex(vertex):
            return len(self.aList[vertex])
        else:
            print("Vertex does not exist")
    
    def endVertices(self, edge):
        u, v = edge
        if self.isVertex(u) and self.isVertex(v):
            if v in self.aList[u] and u in self.aList[v]:
                return (u, v)
        else:
            print("Edge does not exist")
    
    def isDirected(self, edge):
        u, v = edge
        if self.isVertex(u) and self.isVertex(v):
            return v in self.aList[u] and u not in self.aList[v]
        else:
            print("Edge does not exist")
    
    def isOrigin(self, edge):
        u, v = edge
        if self.isVertex(u) and self.isVertex(v):
            return v in self.aList[u] and u not in self.aList[v]
        else:
            print("Edge does not exist")
    
    def isDestination(self, edge):
        u, v = edge
        if self.isVertex(u) and self.isVertex(v):
            return u in self.aList[v] and v not in self.aList[u]
        else:
            print("Edge does not exist")
    
    def opposite(self, vertex, edge):
        u, v = edge
        if self.isVertex(u) and self.isVertex(v):
            if vertex == u:
                return v
            elif vertex == v:
                return u
            else:
                print("Vertex is not incident to edge")
        else:
            print("Edge does not exist")
    
    def areAdjacent(self, edgeA, edgeB):
        uA, vA = edgeA
        uB, vB = edgeB
        if self.isVertex(uA) and self.isVertex(vA) and self.isVertex(uB) and self.isVertex(vB):
            return (uA, vA) in self.aList[uB] and (uA, vA) in self.aList[vB]
        else:
            print("Edge does not exist")
    
    def DFS(self, start_vertex):
        visited = {}
        for vertex in self.vertices():
            visited[vertex] = False

        dfs = []
        
        def DFS_visit(vertex):
            visited[vertex] = True
            dfs.append(vertex)
            for v in self.aList[vertex]:
                if not visited[v]:
                    DFS_visit(v)
        
        DFS_visit(start_vertex)
        return dfs

    def DFS_spanning_tree(self, start_vertex):
        visited = {}
        for vertex in self.vertices():
            visited[vertex] = False
        
        spanning_tree = {}

        def DFS_visit(vertex):
            visited[vertex] = True
            for v in self.aList[vertex]:
                if not visited[v]:
                    spanning_tree[v] = vertex
                    DFS_visit(v)
        
        DFS_visit(start_vertex)
        return spanning_tree
    
    def BFS(self, start_vertex):
        visited = {}
        for vertex in self.vertices():
            visited[vertex] = False
        
        bfs = []
        
        queue = [start_vertex]

        while queue:
            vertex = queue.pop(0)
            if not visited[vertex]:
                visited[vertex] = True
                bfs.append(vertex)
                for v in self.aList[vertex]:
                    queue.append(v)
        
        return bfs
    
    def BFS_spanning_tree(self, start_vertex):
        visited = {}
        for vertex in self.vertices():
            visited[vertex] = False
        
        spanning_tree = {}

        queue = [start_vertex]

        while queue:
            vertex = queue.pop(0)
            if not visited[vertex]:
                visited[vertex] = True
                for v in self.aList[vertex]:
                    if not visited[v]:
                        spanning_tree[v] = vertex
                        queue.append(v)
        return spanning_tree
    
    def findPath(self, start_vertex, end_vertex):
        spanning_tree = self.DFS_spanning_tree(start_vertex)
        path = []
        if end_vertex in spanning_tree:
            path.append(end_vertex)
            while path[-1] != start_vertex:
                path.append(spanning_tree[path[-1]])
            path.reverse()
        return path
    
    def detectCycleDFS(self):
        """
        The idea behind the function is to perform a depth-first search starting from each unvisited vertex in the graph. During the DFS traversal, if a vertex is encountered that has already been visited, it implies that there is a cycle in the graph. The function immediately returns "True" in that case.

        If the DFS traversal is completed without encountering a cycle, the function returns "False".
        """
        visited = {}
        for vertex in self.vertices():
            visited[vertex] = False
        
        def DFS_visit(vertex):
            visited[vertex] = True
            for v in self.aList[vertex]:
                if not visited[v]:
                    DFS_visit(v)
                else:
                    return True
            return False
        
        for vertex in self.vertices():
            if not visited[vertex]:
                if DFS_visit(vertex):
                    return True
        return False


if __name__ == "__main__":
    g = Graph()
    
    edgeList = [
        (0, 1),
        (0, 3),
        (1, 2),
        (2, 4),
        (2, 5),
        (4, 5),
        (4, 6),
        (4, 7),
        (6, 10),
        (7, 8),
        (7, 10),
        (10, 9),
        (10, 8)
    ]

    for edge in edgeList:
        g.insertEdge(edge)
    
    g.insertVertex(11)
    g.sortAdjacencyList()
    
    print("Vertices:", g.vertices())
    print("Edges:", g.edges())
    print("Size:", g.size)
    print("Adjacency List:", g.aList)

    print("DFS:", g.DFS(0))
    print("BFS:", g.BFS(0))

    print("DFS Spanning Tree:", g.DFS_spanning_tree(0))
    print("BFS Spanning Tree:", g.BFS_spanning_tree(0))

    print("Path from 0 to 10:", g.findPath(0, 10))
    print("Cyclic:", g.detectCycleDFS())

    print("\n\n")

    # list of acyclic graph nodes
    edgeList = [
        (1, 2),
        (1, 3),
        (2, 4),
        (3, 2),
        (3, 4)
    ]

    dag = Graph()
    for edge in edgeList:
        dag.insertDirectedEdge(edge)
    

    print("Vertices:", dag.vertices())
    print("Edges:", dag.edges())
    print("Size:", dag.size)
    print("Adjacency List:", dag.aList)

    print("DFS:", dag.DFS(1))
    print("BFS:", dag.BFS(1))

    print("DFS Spanning Tree:", dag.DFS_spanning_tree(1))
    print("BFS Spanning Tree:", dag.BFS_spanning_tree(1))

    print("Path from 1 to 4:", dag.findPath(1, 4))
    print("Cyclic:", dag.detectCycleDFS())

    print("\n\n")

    # list of cyclic graph nodes directed
    edgeList = [
        (1, 2),
        (2, 5),
        (5, 3),
        (3, 1),
        (3, 2),
        (4, 1),
        (4, 3)
    ]
    
    cyclic = Graph()
    for edge in edgeList:
        cyclic.insertDirectedEdge(edge)
    
    print("Vertices:", cyclic.vertices())
    print("Edges:", cyclic.edges())
    print("Size:", cyclic.size)
    print("Adjacency List:", cyclic.aList)
    
    print("DFS:", cyclic.DFS(1))
    print("BFS:", cyclic.BFS(1))

    print("DFS Spanning Tree:", cyclic.DFS_spanning_tree(1))
    print("BFS Spanning Tree:", cyclic.BFS_spanning_tree(1))

    print("Path from 1 to 4:", cyclic.findPath(1, 4))
    print("Path from 1 to 5:", cyclic.findPath(1, 5))
    print("Cyclic:", cyclic.detectCycleDFS())