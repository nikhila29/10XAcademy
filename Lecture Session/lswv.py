def isVowel(ch):
    return ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'


def longestSubStrWOVowel(s):
    n = len(s)

    count = 0
    res = 0

    for i in range(n):
        if isVowel(s[i]):
            count = 0
        else:
            count += 1

        res = max(res, count)

    return res

s = 'helloworldeabcdfe'

print(longestSubStrWOVowel(s))