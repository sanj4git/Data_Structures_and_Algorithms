"""
In the art gallery guarding problem we are given a line L that represents a long hallway in an art gallery. We are also given a set X = {x0,x1,...,xn-1} of real numbers that specify the positions of paintings in this hallway. Suppose that a single guard can protect all the paintings within distance at most 1 of his or her position (on both sides). Design an algorithm for finding a placement of guards that uses the minimum number of guards to guard all the paintings with positions in X.
"""

# Approach 1
def minGuards(X):
    """
    Not Optimal.
    """
    X.sort()
    n = len(X)
    i = 0
    guards = []
    while i < n:
        guards.append(X[i])
        i += 1
        while i < n and X[i] <= guards[-1] + 1:
            i += 1
    return guards

X = [0.5, 1.5, 2.5, 3.5, 4.5]
print("Paintings:", X)
print("Guards:", minGuards(X))
print("Minimum number of guards required:", len(minGuards(X)))
