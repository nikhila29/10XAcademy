# Intersection and Union

def merge(arr1, arr2, union, intersection):
    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            union.append(arr1[i])
            intersection.append(arr2[j])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            union.append(arr1[i])
            i += 1
        else:
            union.append(arr2[j])
            j += 1

    while i < len(arr1):
        union.append(arr1[i])
        i += 1

    while j < len(arr2):
        union.append(arr2[j])
        j += 1

# O(n + m)

arr1 = [2, 4, 5, 7, 8, 12, 13, 16, 18, 22, 25]
arr2 = [6, 7, 8, 10, 12, 15, 18, 22, 23, 26, 30]

union = []
intersection = []

merge(arr1, arr2, union, intersection)

print(union)
print(intersection)
