# Print Powerset of a given set S

def powerSet(S, i):
    # Base Case
    if i == len(S):
        return [[]]
    
    dont_pick = powerSet(S, i + 1)

    pick = []
    for subset in dont_pick:
        pick.append([S[i]] + subset)
    
    return dont_pick + pick

S = [1, 2, 3]
print(powerSet(S, 0))