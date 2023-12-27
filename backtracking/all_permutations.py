# Print all permutations of a given string S

def permutations(S, i):
    # Base Case
    if i == len(S):
        print("".join(S))
        return
    
    for j in range(i, len(S)):
        S[i], S[j] = S[j], S[i]
        permutations(S, i + 1)
        S[i], S[j] = S[j], S[i]

    

S = "ABC"
permutations(list(S), 0)