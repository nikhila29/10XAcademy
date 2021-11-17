from collections import Counter
def anagram(a,b):
    if (Counter(a)==Counter(b)):
        return (1)
    else:
        return 0
a=input()
b=input()
print(anagram(a,b))