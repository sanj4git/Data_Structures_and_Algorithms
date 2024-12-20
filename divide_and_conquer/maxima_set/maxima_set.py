# Maxima-Set S

"""
Given a set S of points, the goal is to form a maxima set S such that there is no pair of points (x, y) and (x', y') in S such that x <= x' and y <= y'.
"""

# Brute Force
def maximaSet(S):
    S.sort(key= lambda x: x[0])

    maximaSet = []
    for i in range(len(S)):
        isMaxima = True
        for j in range(i + 1, len(S)):
            if S[i][1] < S[j][1]:
                isMaxima = False
                break
        if isMaxima:
            maximaSet.append(S[i])

    return maximaSet


# Divide and Conquer: Referred Goodrich textbook.
def maximaSetDC(S):
    if len(S) <= 1:
        return S

    M1 = maximaSetDC(S[:len(S) // 2])
    M2 = maximaSetDC(S[len(S) // 2:])

    q = M2[0]

    # Finding maxima
    for r in M1:
        if r[0] <= q[0] and r[1] <= q[1]:
            M1.remove(r)

    M1 += M2

    return M1

test_cases = [
    [(2, 7), (3, 9), (9, 2), (5, 8), (7, 5), (6, 4), (8, 6), (4, 3)],
    [(7, 13), (2, 5), (4, 4), (5, 1), (7, 7), (11, 5), (13, 3), (4, 11), (9, 10), (15, 7), (12, 12), (14, 10)]
]

for S in test_cases:
    print("S = {}".format(S))
    print("maximaSet(S) = {}".format(maximaSet(S)))
    print("maximaSetDC(S) = {}".format(maximaSetDC(S)))
    print()

