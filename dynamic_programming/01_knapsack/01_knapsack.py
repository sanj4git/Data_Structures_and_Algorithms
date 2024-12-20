# 0/1 Knapsack

# Approach 1: Recursion
recursive_calls = [0, 0]
def knapsack_1(weights, values, W, i):
    recursive_calls[0] += 1
    if i < 0:
        return 0
    if weights[i] > W:
        return knapsack_1(weights, values, W, i - 1)
    else:
        return max(
            knapsack_1(weights, values, W, i - 1),
            knapsack_1(weights, values, W - weights[i], i - 1) + values[i],
        )
    
weights = [10, 5, 5]
values = [60, 50, 50]

W = 10
print(knapsack_1(weights, values, W, len(weights) - 1))

# Approach 2: Memoization

def knapsack_2(weights, values, W, i, cache):
    recursive_calls[1] += 1
    if i < 0:
        return 0
    if cache[i][W] != -1:
        return cache[i][W]
    if weights[i] > W:
        cache[i][W] = knapsack_2(weights, values, W, i - 1, cache)
    else:
        cache[i][W] = max(
            knapsack_2(weights, values, W, i - 1, cache),
            knapsack_2(weights, values, W - weights[i], i - 1, cache) + values[i],
        )
    return cache[i][W]

weights = [10, 5, 5]
values = [60, 50, 50]

W = 10

cache = [[-1 for _ in range(W + 1)] for _ in range(len(weights))]
print(knapsack_2(weights, values, W, len(weights) - 1, cache))


# Approach 3: DP

def knapsack_3(weights, values, W):
    dp = [[0 for _ in range(W + 1)] for _ in range(len(weights) + 1)]

    for i in range(1, len(weights) + 1):
        for j in range(1, W + 1):
            if weights[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(
                    dp[i - 1][j], dp[i - 1][j - weights[i - 1]] + values[i - 1]
                )

    return dp[len(weights)][W]

weights = [10, 5, 5]
values = [60, 50, 50]

W = 10

print(knapsack_3(weights, values, W))


