def computeLps(pat):
    m = len(pat)
    lps = [0] * m

    i = 1
    j = 0

    while i < m:
        if pat[i] == pat[j]:
            lps[i] = j + 1
            i += 1
            j += 1
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return lps

# O(m + m) => O(2m)


def search(txt, pat):
    n = len(txt)
    m = len(pat)

    if m > n:
        return

    lps = computeLps(pat)

    i = 0
    j = 0

    while i < n:
        if txt[i] == pat[j]:
            i += 1
            j += 1

        if j == m:
            print('Pattern found at ', i - j)
            j = lps[j - 1]
        elif i < n and txt[i] != pat[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

        print("i = ", i, ", j = ", j)

# O(n + n) => )(2n)

txt = 'AAAAABAACAABAAAA'

pat = 'AAAA'

search(txt, pat)

# i = 0, j = 0
# i = 1, j = 1
# i = 2, j = 2
# i = 3, j = 3
# i = 4, j = 4

# i = 4, j = 3
# i = 5, j = 4

# i = 5, j = 3
# i = 5, j = 2
# i = 5, j = 1
# i = 5, j = 0
# i = 6, j = 0
# i = 7, j = 1
# i = 8, j = 2
# i = 8, j = 1
# i = 8, j = 0
# i = 9, j = 0


# [0, 1, 2, 3]




