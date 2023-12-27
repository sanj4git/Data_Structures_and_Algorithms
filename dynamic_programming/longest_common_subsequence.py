# Longest Common Subsequence

import sys

sys.setrecursionlimit(2**31 - 1)

## Approach 1: Recursion
def lcs_1(i, j, X, Y):
    if i < 0 or j < 0:
        return 0
    if X[i] == Y[j]:
        return 1 + lcs_1(i - 1, j - 1, X, Y)
    else:
        return max(lcs_1(i - 1, j, X, Y), lcs_1(i, j - 1, X, Y))


X = "ABET"
Y = "ACST"

print(lcs_1(len(X) - 1, len(Y) - 1, X, Y))

## Approach 2: Memoization. 2D array cache

def lcs_2(i, j, X, Y, cache):
    if i < 0 or j < 0:
        return 0
    if cache[i][j] != -1:
        return cache[i][j]
    if X[i] == Y[j]:
        cache[i][j] = 1 + lcs_2(i - 1, j - 1, X, Y, cache)
    else:
        cache[i][j] = max(lcs_2(i - 1, j, X, Y, cache), lcs_2(i, j - 1, X, Y, cache))
    return cache[i][j]


X = "MANGROVEFOREST"
Y = "MULTIDIMENSIONAL"

cache = [[-1 for _ in range(len(Y))] for _ in range(len(X))]
print(lcs_2(len(X) - 1, len(Y) - 1, X, Y, cache))

## Approach 3: DP.

def lcs_3(X, Y):
    dp = [[0 for _ in range(len(Y) + 1)] for _ in range(len(X) + 1)]

    for i in range(1, len(X) + 1):
        for j in range(1, len(Y) + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[len(X)][len(Y)]


X = "MANGROVEFOREST"
Y = "MULTIDIMENSIONAL"

print(lcs_3(X, Y))
