# Approach 1: Top Down with Memoization
def lis(i, prev_i, nums, dp):
    if i == len(nums):
        return 0
        
    if dp[i][prev_i + 1] != -1:
        return dp[i][prev_i + 1]

    total_length = lis(i + 1, prev_i, nums, dp)

    if (prev_i == -1) or nums[i] >= nums[prev_i]:
        total_length = max(total_length, 1 + lis(i + 1, i, nums, dp))


    dp[i][prev_i + 1] = total_length

    return dp[i][prev_i + 1]


# Approach 2: Bottom Up
def lengthOfLIS(nums):
    dp = [[0 for _ in range(len(nums) + 1)] for _ in range(len(nums) + 1)]

    for i in range(len(nums) - 1, -1, -1):
        for prev_i in range(i - 1, -2, -1):
            total_length = dp[i + 1][prev_i + 1]
            if (prev_i == -1) or nums[i] >= nums[prev_i]:
                total_length = max(total_length, 1 + dp[i + 1][i + 1])
                
            dp[i][prev_i + 1] = total_length
        
    return dp[0][0]

# Approach 3: LCS based approach
def lcs(X, Y):
    dp = [[0 for _ in range(len(Y) + 1)] for _ in range(len(X) + 1)]

    for i in range(1, len(X) + 1):
        for j in range(1, len(Y) + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[len(X)][len(Y)]

def lengthOfLIS_withLCS(nums):
    sorted_nums = sorted(nums)
    return lcs(nums, sorted_nums)

nums = [10,9,2,5,3,7,101,18]
print(lengthOfLIS(nums))
print(lengthOfLIS_withLCS(nums))

nums = [0,1,0,3,2,3]
print(lengthOfLIS(nums))
print(lengthOfLIS_withLCS(nums))

nums = [7,7,7,7,7,7,7]
print(lengthOfLIS(nums))
print(lengthOfLIS_withLCS(nums))
