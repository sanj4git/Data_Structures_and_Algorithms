class DAG:

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
            else:
                print("Invalid directed edge")
        else:
            print("Invalid directed edge")
    
    def inDegree(self, vertex):
        if self.isVertex(vertex):
            return sum([1 for v in self.aList if vertex in self.aList[v]])
        else:
            print("Vertex does not exist")
    
    def outDegree(self, vertex):
        if self.isVertex(vertex):
            return len(self.aList[vertex])
        else:
            print("Vertex does not exist")
    
    def degree(self, vertex):
        if self.isVertex(vertex):
            return self.inDegree(vertex) + self.outDegree(vertex)
        else:
            print("Vertex does not exist")
    
    def neighbors(self, vertex):
        if self.isVertex(vertex):
            return self.aList[vertex]
        else:
            print("Vertex does not exist")
    
    def adjacent(self, u, v):
        if self.isVertex(u) and self.isVertex(v):
            return v in self.aList[u]
        else:
            print("Invalid directed edge")
    
    def DFS(self, start_vertex):
        visited = {}
        for v in self.aList:
            visited[v] = False
        
        dfs = []
        
        def DFS_visit(vertex):
            visited[vertex] = True
            dfs.append(vertex)
            for v in self.aList[vertex]:
                if not visited[v]:
                    DFS_visit(v)
        
        DFS_visit(start_vertex)

        return dfs

    def BFS(self, start_vertex):
        visited = {}
        for v in self.aList:
            visited[v] = False
        
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
    
    def topological_sort(self):
        """
            1. Compute the in-degree of each node in the graph.
            2. Enqueue all nodes with in-degree 0 to a queue.
            3. While the queue is not empty, dequeue a node from the front of the queue and add it to the sorted list.
            4. For each of the dequeued node's neighbors, decrement their in-degree by 1.
            5. If any of the dequeued node's neighbors now have in-degree 0, enqueue them to the queue.
            6. Repeat steps 3-5 until the queue is empty.
        """
        in_degrees = {}
        for vertex in self.vertices():
            in_degrees[vertex] = self.inDegree(vertex)
        
        topological_order = []
        queue = []

        for vertex in in_degrees:
            if in_degrees[vertex] == 0:
                queue.append(vertex)
        
        while queue:
            vertex = queue.pop(0)
            topological_order.append(vertex)
            for v in self.aList[vertex]:
                in_degrees[v] -= 1
                if in_degrees[v] == 0:
                    queue.append(v)
        
        return topological_order
    
    def isDAG(self):
        spanning_tree = self.DFS_spanning_tree(self.vertices()[0])
        for vertex in spanning_tree:
            if spanning_tree[vertex] == vertex:
                return False
        return True
    
    def longestPath(self):
        in_degrees = {}
        longest_paths = {}
        for v in self.aList:
            in_degrees[v] = self.inDegree(v)
            longest_paths[v] = 0
        
        topological_order = []
        queue = []

        for v in in_degrees:
            if in_degrees[v] == 0:
                queue.append(v)
        
        while queue:
            vertex = queue.pop(0)
            topological_order.append(vertex)
            for v in self.aList[vertex]:
                if longest_paths[v] < longest_paths[vertex] + 1:
                    longest_paths[v] = longest_paths[vertex] + 1
                in_degrees[v] -= 1
                if in_degrees[v] == 0:
                    queue.append(v)

        return longest_paths
    

g = DAG()

edgeList = [
    (1, 2), (1, 7),
    (2, 5),
    (0, 2), (0, 3), (0, 4),
    (3, 5), (3, 7),
    (6, 7),
    (5, 6),
    (4, 7)
]

for edge in edgeList:
    g.insertEdge(edge)

g.sortAdjacencyList()
print("\n")
print("Vertices:", g.vertices())
print("Edges:", g.edges())
print("Size:", g.size)
print("Adjacency List:", g.aList)
print("DFS:", g.DFS(0))
print("BFS:", g.BFS(0))
print("DFS Spanning Tree:", g.DFS_spanning_tree(0))
print("BFS Spanning Tree:", g.BFS_spanning_tree(0))
print("Is DAG:", g.isDAG())
print("Topological Sort:", g.topological_sort())
print("Longest Path:", g.longestPath())
print("Trace Longest Path:", g.traceLongestPath())
