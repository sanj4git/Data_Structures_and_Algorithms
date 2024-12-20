# Matrix Chain Multiplication
## Approach 1

def mcm_1(d, i, j):
    if i == j:
        return 0
    N = float("inf")
    for k in range(i, j):
        N = min(N, mcm_1(d, i, k) + mcm_1(d, k + 1, j) + d[i] * d[k + 1] * d[j + 1])
    return N


d = [30, 35, 15, 5, 10, 20, 25]
print(mcm_1(d, 0, len(d) - 2))

## Approach 2 with memoization
def mcm_2(d, i, j, cache):
    if i == j:
        return 0
    if cache[i][j] != -1:
        return cache[i][j]
    N = float("inf")
    for k in range(i, j):
        N = min(
            N,
            mcm_2(d, i, k, cache)
            + mcm_2(d, k + 1, j, cache)
            + d[i] * d[k + 1] * d[j + 1],
        )
    cache[i][j] = N
    return N


d = [30, 35, 15, 5, 10, 20, 25]
cache = [[-1 for _ in range(len(d) - 1)] for _ in range(len(d) - 1)]
print(mcm_2(d, 0, len(d) - 2, cache))

## Approach 3 with DP

def mcm_3(d):
    N = [[0 for _ in range(len(d) - 1)] for _ in range(len(d) - 1)]

    # Initializing diagonals to be 0
    for i in range(len(d) - 1):
        N[i][i] = 0

    for b in range(1, len(d) - 1):
        for i in range(0, len(d) - b - 1):
            j = i + b
            N[i][j] = float("inf")
            for k in range(i, j):
                N[i][j] = min(N[i][j], N[i][k] + N[k + 1][j] + d[i] * d[k + 1] * d[j + 1])

    return N[0][len(d) - 2]

d = [30, 35, 15, 5, 10, 20, 25]
print(mcm_3(d))
