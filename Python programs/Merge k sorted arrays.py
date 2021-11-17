# Merge k sorted arrays

def divideArrays(arr, output, l, r, n):
    if l == r:
        for i in range(n):
            output[l * n + i] = arr[l][i]

        return

    mid = (l + r) // 2

    divideArrays(arr, output, l, mid, n)

    divideArrays(arr, output, mid + 1, r, n)

    mergeArrays(output, l, mid, r, n)


def mergeArrays(output, l, mid, r, n):
    l_st = l * n
    r_st = (mid + 1) * n

    l_c = (mid - l + 1) * n
    r_c = (r - mid) * n # r - (mid + 1) + 1

    l_arr = [0] * l_c
    r_arr = [0] * r_c

    for i in range(l_c):
        l_arr[i] = output[l_st + i]

    for j in range(r_c):
        r_arr[j] = output[r_st + j]

    l_idx = 0
    r_idx = 0

    # start of output array
    k = l_st

    # while (l_idx + r_idx) < (l_c + r_c):
    #     if r_idx == r_c or (l_idx != l_c and l_arr[l_idx] < r_arr[r_idx]):
    #         output[k] = l_arr[l_idx]
    #         l_idx += 1
    #         k += 1
    #     else:
    #         output[k] = r_arr[r_idx]
    #         r_idx += 1
    #         k += 1

    while l_idx < l_c and r_idx < r_c:
        if l_arr[l_idx] < r_arr[r_idx]:
            output[k] = l_arr[l_idx]
            l_idx += 1
        else: 
            output[k] = r_arr[r_idx]
            r_idx += 1

        k += 1

    while l_idx < l_c:
        output[k] = l_arr[l_idx]
        l_idx += 1
        k += 1

    while r_idx < r_c:
        output[k] = r_arr[r_idx]
        r_idx += 1
        k += 1


arr = [[1, 2, 3, 4, 5],
        [2, 4, 5, 9, 10],
        [1, 10, 20, 21, 22],
        [3, 4, 15, 16, 17]]

k = len(arr)
n = len(arr[0])

output = [0] * (n * k)

divideArrays(arr, output, 0, k - 1, n)

print(output)