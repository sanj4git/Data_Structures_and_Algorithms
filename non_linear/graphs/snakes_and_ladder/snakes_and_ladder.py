class Board:
    def __init__(self, n, ladders, snakes, k):
        """
        n: dimension of the board (n x n)
        size: total number of squares on the board
        ladders: list of tuples representing the start and end of ladders
        snakes: list of tuples representing the start and end of snakes
        k: number of positions we can move from a given position
        """

        self.n = n
        self.size = n * n
        self.ladders = ladders
        self.snakes = snakes
        self.k = k
        self.a_list = self.createGraph()

    def createGraph(self):
        """
        Creates a graph representation of the board. Only snakes and ladders are considered edges.

        Complexity: O(n + m) where n is the number of vertices and m is the number of edges.
        """
        a_list = {i: [] for i in range(1, self.size + 1)}
        for ladder in self.ladders:
            a_list[ladder[0]].append(ladder[1])

        for snake in self.snakes:
            a_list[snake[0]].append(snake[1])

        return a_list

    def getNeighbors(self, position):
        """
        Returns the neighbors of a given position.
        Complexity: O(k) where k is the number of positions we can move from a given position.
        """

        if len(self.a_list[position]) > 0:
            return self.a_list[position]
        else:
            neighbors = []
            for neighbor in range(position + 1, position + self.k + 1):
                if neighbor <= self.size:
                    if len(self.a_list[neighbor]) > 0:
                        neighbors.append(self.a_list[neighbor][0])
                    else:
                        neighbors.append(neighbor)
            return neighbors

    # Question 1->1. Verify if there is at least one way to reach the goal.
    def canReachGoal(self):
        """
        Returns True if the goal can be reached from the start. Returns False otherwise.
        Complexity: O(n + m) where n is the number of vertices and m is the number of edges.
        """

        # Start at position 1
        visited = [False] * (self.size + 1)
        queue = [1]

        while queue:
            position = queue.pop(0)
            if position == self.size:
                return True
            if not visited[position]:
                visited[position] = True
                queue.extend(self.getNeighbors(position))

        print(f"Goal cannot be reached. No path from 1 to {self.size}")
        return False

    # Question 1->2. Verify that no two snakes/ladders start or end at the same grid position. (can’t process the input directly)
    def noSnakeLadderInSameSquare(self):
        """
        Returns True if the board is valid. Returns False otherwise.
        Complexity: O(n + m) where n is the number of vertices and m is the number of edges.
        """

        # Make sure no two snakes/ladders start or end at the same grid position. Maintain a dictionary. Key: position, Value: occurence
        occurence = [0 for _ in range(self.size + 1)]

        for i in range(1, self.size + 1):
            if len(self.a_list[i]) > 1:
                return False
            for neighbor in self.a_list[i]:
                occurence[neighbor] += 1
                occurence[i] += 1

        for i in range(1, self.size + 1):
            if occurence[i] > 1:
                print(f"Invalid board. Snake/Ladder found in same square: {i}")
                return False

        return True

    # Question 1->3. Verify that the board is not cyclic. (can’t process the input directly)
    def isCyclicBasedOnTopologicalSort(self):
        """
        Returns True if the board is cyclic. Returns False otherwise.

        Complexity: O(n + m) where n is the number of vertices and m is the number of edges.
        """

        # Detect snake in graph

        for i in range(1, self.size + 1):
            for neighbor in self.a_list[i]:
                if neighbor <= i:
                    print(f"Board is cyclic. Snake found: {i}->{neighbor}")
                    return True

        return False

        # # Check if there is a cycle in the graph
        # in_degree = {i: 0 for i in range(1, self.size + 1)}
        # for i in range(1, self.size + 1):
        #     for neighbor in self.a_list[i]:
        #         in_degree[neighbor] += 1

        # queue = []
        # for i in range(1, self.size + 1):
        #     if in_degree[i] == 0:
        #         queue.append(i)

        # count = 0
        # while queue:
        #     position = queue.pop(0)
        #     for neighbor in self.getNeighbors(position):
        #         in_degree[neighbor] -= 1
        #         if in_degree[neighbor] == 0:
        #             queue.append(neighbor)
        #     count += 1

        # return count != self.size

    # Question 1->4. Verify that there is no ladder from the start position to the destination directly.
    def noDirectPathFromStartToEnd(self):
        """
        Returns True if the board is unbiased (No path from 1 to 100). Returns False otherwise.
        Complexity: O(n + m) where n is the number of vertices and m is the number of edges.
        """

        # Check if there is a ladder from start to end
        return self.size not in self.getNeighbors(1)

    # Question 2. Find the shortest sequence of dice rolls to reach the goal from the start position on the input board above, considering that the maximum distance that can be moved is dictated by the dice aka 6 or the snake/ladder.
    def shortestPath(self):
        """
        Returns the shortest path from start to end. Returns None if the board is invalid.

        Complexity: O(n + m) where n is the number of vertices and m is the number of edges.

        Algorithm:
        1. Run BFS to find the shortest path from start to end.
        2. Backtrack to find the shortest path.

        Why not dijkstra's algorithm?
        1. Using priority queue doesn't make sense as we are moving in sequential order from visiting nodes with 1 distance then visiting nodes with 2 distance and so on.
        2. Then if (distance[destination] > dist[current] + 1) becomes useless as by visiting the node first time we have the shortest path, so this condition won't be true anytime in the travesal. Waste of time.
        3. Also, we are not considering the weights of the edges explicitly. So, dijkstra's algorithm is not required.
        4. We only care about the hops we are making. So, BFS is the best choice.
        """
        if (
            (self.canReachGoal() == False)
            or (self.noSnakeLadderInSameSquare() == False)
            or (self.noDirectPathFromStartToEnd() == False)
        ):
            print("Board is invalid. Cannot find shortest path.")
            return None

        # BFS
        visited = [False] * (self.size + 1)
        parent = [None] * (self.size + 1)
        queue = [(1, 0)]
        visited[1] = True

        while queue:
            position, distance = queue.pop(0)
            if position == self.size:
                break
            for neighbor in self.getNeighbors(position):
                if not visited[neighbor]:
                    visited[neighbor] = True
                    parent[neighbor] = position
                    queue.append((neighbor, distance + 1))

        # Backtrack to find the shortest path
        path = []
        position = self.size
        while position != 1:
            path.append(position)
            position = parent[position]
        path.append(1)
        path.reverse()

        return {"distance": len(path) - 1, "path": path}


# Test case 1
n = 6
ladders = [(2, 15), (14, 35)]
snakes = [(17, 13), (36, 2)]

board = Board(n, ladders, snakes, 6)

print("Test case 1")
print("Can reach goal:", board.canReachGoal())
print("Snake Ladder not found in same square:", board.noSnakeLadderInSameSquare())
print("Board is cyclic:", board.isCyclicBasedOnTopologicalSort())
print(f"Board has no 1->{board.size} path:", board.noDirectPathFromStartToEnd())
print("Shortest path:", board.shortestPath())
print()

# Test case 2 (Cannot reach goal)
n = 6
ladders = [(2, 15), (14, 35)]
snakes = [(17, 13), (36, 1)]

board = Board(n, ladders, snakes, 6)

print("Test case 2")
print("Can reach goal:", board.canReachGoal())
print("Snake Ladder not found in same square:", board.noSnakeLadderInSameSquare())
print("Board is cyclic:", board.isCyclicBasedOnTopologicalSort())
print(f"Board has no 1->{board.size} path:", board.noDirectPathFromStartToEnd())
print("Shortest path:", board.shortestPath())
print()

# Test case 3 (Snake and ladder in same square)
n = 6
ladders = [(2, 15), (14, 35)]
snakes = [(17, 13), (17, 1)]

board = Board(n, ladders, snakes, 6)

print("Test case 3")
print("Can reach goal:", board.canReachGoal())
print("Snake Ladder not found in same square:", board.noSnakeLadderInSameSquare())
print("Board is cyclic:", board.isCyclicBasedOnTopologicalSort())
print(f"Board has no 1->{board.size} path:", board.noDirectPathFromStartToEnd())
print("Shortest path:", board.shortestPath())
print()

# Test case 4 (Board is cyclic)
n = 6
ladders = [(2, 15), (14, 35)]
snakes = [(17, 13), (36, 1), (1, 17)]

board = Board(n, ladders, snakes, 6)

print("Test case 4")
print("Can reach goal:", board.canReachGoal())
print("Snake Ladder not found in same square:", board.noSnakeLadderInSameSquare())
print("Board is cyclic:", board.isCyclicBasedOnTopologicalSort())
print(f"Board has no 1->{board.size} path:", board.noDirectPathFromStartToEnd())
print("Shortest path:", board.shortestPath())
print()

# Test case 5 (Board has 1->{board.size} path)
n = 6
ladders = [(2, 15), (14, 35)]
snakes = [(17, 13), (36, 1), (1, 36)]

board = Board(n, ladders, snakes, 6)

print("Test case 5")
print("Can reach goal:", board.canReachGoal())
print("Snake Ladder not found in same square:", board.noSnakeLadderInSameSquare())
print("Board is cyclic:", board.isCyclicBasedOnTopologicalSort())
print(f"Board has no 1->{board.size} path:", board.noDirectPathFromStartToEnd())
print("Shortest path:", board.shortestPath())
print()

# Test case 6
n = 10
ladders = [(2, 15), (14, 35), (7, 27), (9, 29)]
snakes = [(17, 13), (1, 36), (19, 3), (21, 5)]

board = Board(n, ladders, snakes, 6)

print("Test case 6")
print("Can reach goal:", board.canReachGoal())
print("Snake Ladder not found in same square:", board.noSnakeLadderInSameSquare())
print("Board is cyclic:", board.isCyclicBasedOnTopologicalSort())
print(f"Board has no 1->{board.size} path:", board.noDirectPathFromStartToEnd())
print("Shortest path:", board.shortestPath())
print()
