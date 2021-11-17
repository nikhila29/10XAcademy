def search(txt, pat):
    n = len(txt)
    m = len(pat)

    if m > n:
        return

    for i in range(n - m + 1):
        j = 0

        while j < m:
            if pat[j] != txt[i + j]:
                break
            j += 1

        if j == m:
            print('Pattern found at index ', i)


txt = 'AABACAADAABAABA'
pat = 'AABA'

txt = "AAAAABAAABA" 
pat = "AAAA"

search(txt, pat)

# Pattern found at index  0
# Pattern found at index  9
# Pattern found at index  12

# Complexity of O(n) for worst case also

# KMP algo
