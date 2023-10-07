def DFS(G, s):
    visited = {}
    for v in G:
        visited[v] = False

    dfs_order = []

    def DFS_visit(u):
        visited[u] = True
        dfs_order.append(u)
        for v in G[u]:
            if not visited[v]:
                DFS_visit(v)

    DFS_visit(s)

    return dfs_order, visited

def BFS(G, s):
    queue = [s]
    visited = {}
    for v in G:
        visited[v] = False

    bfs_order = []

    while len(queue) > 0:
        u = queue.pop(0)
        visited[u] = True
        bfs_order.append(u)
        for v in G[u]:
            if not visited[v]:
                queue.append(v)

    return bfs_order, visited


def isConnected(G):
    """
    Returns True if the graph G is connected, False otherwise.
    Just one DFS. If there is atleast one vertex that is not visited, then the graph is not connected.
    """
    v = list(G.keys())[0] # Pick any vertex. Assuming G is not empty.

    visited = DFS(G, v)[1]

    for u in G:
        if not visited[u]:
            return False
        
    return True

def findConnectedComponents(G):
    """
    Returns a list of connected components of the graph G. (Spanning Forest of G)
    """
    connected_components = []
    visited = {}
    for v in G:
        visited[v] = False

    for v in G:
        if not visited[v]:
            connected_components.append(DFS(G, v)[0])
            for u in connected_components[-1]:
                visited[u] = True
    
    return connected_components

def topologicalSort(G):
    in_degree = {}
    zero_degree_queue = []
    topologically_sorted_list = []

    for node in G:
        in_degree[node] = 0

    for node in G:
        for neighbour in G[node]:
            in_degree[neighbour] += 1

    for node in G:
        if in_degree[node] == 0:
            zero_degree_queue.append(node)

    while len(zero_degree_queue) > 0:
        current_node = zero_degree_queue.pop(0)
        topologically_sorted_list.append(current_node)
        in_degree[current_node] -= 1

        for neighbour in G[current_node]:
            in_degree[neighbour] -= 1
            if in_degree[neighbour] == 0:
                zero_degree_queue.append(neighbour)

    return topologically_sorted_list

def isDAG(G):
    """
    Returns True if the graph G is a DAG, False otherwise.
    """
    return len(topologicalSort(G)) == len(G)

def longestPath(G):
    if not isDAG(G):
        return "Graph is not a DAG."
    in_degree = {}
    zero_degree_queue = []
    longest_path = {}

    for node in G:
        in_degree[node] = 0
        longest_path[node] = 0

    for node in G:
        for neighbour in G[node]:
            in_degree[neighbour] += 1

    for node in G:
        if in_degree[node] == 0:
            zero_degree_queue.append(node)

    while len(zero_degree_queue) > 0:
        current_node = zero_degree_queue.pop(0)
        in_degree[current_node] -= 1

        for neighbour in G[current_node]:
            in_degree[neighbour] -= 1
            longest_path[neighbour] = max(longest_path[neighbour], longest_path[current_node] + 1) # Replace 1 with weight of edge (current_node, neighbour) if edge weights are given.
            if in_degree[neighbour] == 0:
                zero_degree_queue.append(neighbour)

    return longest_path

G = {
    "LAX": ["SFO", "DFW", "MIA"],
    "SFO": ["LAX", "DFW", "ORD", "BOS"],
    "DFW": ["LAX", "SFO", "ORD", "MIA", "JFK"],
    "MIA": ["LAX", "DFW", "JFK", "BWI", "BOS"],
    "ORD": ["SFO", "DFW", "JFK", "BWI", "BOS", "PVD"],
    "BWI": ["MIA", "ORD", "JFK"],
    "JFK": ["DFW", "MIA", "ORD", "BWI", "BOS", "PVD"],
    "BOS": ["SFO", "MIA", "ORD", "JFK"],
    "PVD": ["ORD", "JFK"]
}


G = {0: [2, 3, 4], 1: [2, 7], 2: [5], 3: [5, 7], 4: [7], 5: [6], 6: [7], 7: []}
print(isConnected(G)) 
print(findConnectedComponents(G))
print(isDAG(G))
print(topologicalSort(G))
print(longestPath(G))
