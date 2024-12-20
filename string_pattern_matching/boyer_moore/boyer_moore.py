# Boyer Moore

def build_last(text, pattern):
    last = {}

    for i in range(len(text)):
        last[text[i]] = -1
    
    for i in range(len(pattern)):
        last[pattern[i]] = i

    print(last)
    
    return last

def boyer_moore(text, pattern):
    last = build_last(text, pattern)
    n = len(text)
    m = len(pattern)

    if m > n:
        return -1

    i = m - 1
    j = m - 1

    while i < n:
        if text[i] == pattern[j]:
            if j == 0:
                return i
            else:
                i -= 1
                j -= 1
        else:
            i = i + m - min(j, last[text[i]] + 1)
            j = m - 1

    return -1

text = "abacaabadcabacabaabb"
pattern = "abacab"

print(boyer_moore(text, pattern))
