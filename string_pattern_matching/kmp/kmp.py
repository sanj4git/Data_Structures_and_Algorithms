# Failure Function
def build_failure_function(pattern):
    """
    f(j) -> Longest prefix of p that is also a suffix of p[1..j]
    """

    f = [0 for _ in range(len(pattern))]
    f[0] = 0
    i = 1
    j = 0

    while i < len(pattern):
        if pattern[i] == pattern[j]:
            f[i] = j + 1
            i += 1
            j += 1
        elif j > 0:
            j = f[j - 1]
        else:
            f[i] = 0
            i += 1

    return f

def kmp(text, pattern):
    """
    O(n + m)
    """

    f = build_failure_function(pattern)
    n = len(text)
    m = len(pattern)

    i = 0
    j = 0

    while i < n:
        if text[i] == pattern[j]:
            if j == m - 1:
                return i - m + 1
            else:
                i += 1
                j += 1
        elif j > 0:
            j = f[j - 1]
        else:
            i += 1

    return -1

text = "abacaabadcabacabaabb"
pattern = "abacab"

print(kmp(text, pattern))
