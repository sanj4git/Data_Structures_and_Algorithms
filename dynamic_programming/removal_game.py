"""
Given a set of cards each with a value, two players take turns to pick a card from the set. The player with the highest value wins the game. Find the maximum possible score for the first player if both players play optimally and first player is the one to start the game.

The idea is this:
    1. Maximize the score of the first player
    2. Minimize the score of the second player

left -> i
right -> j

Cases:
    1. Player 1 picks left card, player 2 picks left card       (i, j) -> value[i] + (i + 2, j)
    2. Player 1 picks left card, player 2 picks right card      (i, j) -> value[i] + (i + 1, j - 1)

    3. Player 1 picks right card, player 2 picks left card      (i, j) -> value[j] + (i + 1, j - 1)
    4. Player 1 picks right card, player 2 picks right card     (i, j) -> value[j] + (i, j - 2)


Logic: max(left + min(1, 2), right + min(3, 4)) -> From the definition of the subproblem, we can see that we are trying to maximize the score of the first player and minimize the score of the second playerq
"""

def removal_game(cards, i, j):
    if i == j:
        return 0
    
    if i == j - 1:
        return max(cards[i], cards[j])
    
    return max(cards[i] + min(removal_game(cards, i + 2, j), removal_game(cards, i + 1, j - 1)),
               cards[j] + min(removal_game(cards, i + 1, j - 1), removal_game(cards, i, j - 2)))

cards = [4, 5, 1, 3]
print(removal_game(cards, 0, len(cards) - 1))


def removal_game(cards, i, j, dp):
    if i == j:
        return 0
    
    if i == j - 1:
        return max(cards[i], cards[j])
    
    if dp[i][j] != -1:
        return dp[i][j]
    
    dp[i][j] = max(cards[i] + min(removal_game(cards, i + 2, j, dp), removal_game(cards, i + 1, j - 1, dp)),
               cards[j] + min(removal_game(cards, i + 1, j - 1, dp), removal_game(cards, i, j - 2, dp)))
    
    return dp[i][j]

cards = [4, 5, 1, 3]
dp = [[-1 for _ in range(len(cards))] for _ in range(len(cards))]
print(removal_game(cards, 0, len(cards) - 1, dp))


def removal_game(cards):
    n = len(cards)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        dp[i][i] = cards[i]
    
    for i in range(n - 1):
        dp[i][i + 1] = max(cards[i], cards[i + 1])
    
    for gap in range(2, n):
        for i in range(n - gap):
            j = i + gap
            dp[i][j] = max(cards[i] + min(dp[i + 2][j], dp[i + 1][j - 1]),
                           cards[j] + min(dp[i + 1][j - 1], dp[i][j - 2]))
    
    return dp[0][n - 1]

cards = [4, 5, 1, 3]
print(removal_game(cards))


